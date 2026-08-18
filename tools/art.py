#!/usr/bin/env python3
"""One-sprite art inbox: preview, promote, restore.

See assets/ART.md. Does not rewrite the farm unless you pass promote/restore.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
INBOX = ASSETS / "inbox"
PREVIEW = ASSETS / "preview"
MANIFEST_PATH = ASSETS / "manifest.json"
ART_JSON_PATH = ASSETS / "art.json"

_pg_path = Path(__file__).resolve().parent / "process-generated.py"
_pg_spec = importlib.util.spec_from_file_location("process_generated", _pg_path)
pg = importlib.util.module_from_spec(_pg_spec)
_pg_spec.loader.exec_module(pg)


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def sprite_map(manifest):
    return {s["id"]: s for s in manifest["sprites"]}


def dest_rels(spr):
    rel = spr["file"]
    frames = int(spr.get("frames") or 1)
    if "{n}" in rel:
        return [rel.replace("{n}", str(i)) for i in range(frames)]
    return [rel]


def follow_from(sid, overrides):
    seen = set()
    while sid in overrides and "from" in overrides[sid]:
        if sid in seen:
            raise SystemExit("cycle in art.json from-chain at %s" % sid)
        seen.add(sid)
        sid = overrides[sid]["from"]
    return sid


def resolve_job(sid, sprites, art):
    overrides = art.get("overrides") or {}
    sid = follow_from(sid, overrides)
    if sid not in sprites:
        raise SystemExit("unknown sprite id %r (not in manifest.json)" % sid)
    ov = overrides.get(sid) or {}
    family = list(ov.get("family") or [sid])
    if sid not in family:
        family.insert(0, sid)
    for fid in family:
        if fid not in sprites:
            raise SystemExit("art.json family member %r is not in the manifest" % fid)
    first_rel = dest_rels(sprites[sid])[0]
    chroma = ov["chroma"] if "chroma" in ov else not first_rel.startswith("tiles/")
    quantize = ov["quantize"] if "quantize" in ov else chroma
    sources = []
    if ov.get("source"):
        sources.append(ov["source"])
    sources.append("%s.png" % sid)
    # unique, keep order
    seen = set()
    source_names = []
    for name in sources:
        if name not in seen:
            seen.add(name)
            source_names.append(name)
    flip = ov.get("flip")
    if flip and flip not in sprites:
        raise SystemExit("art.json flip target %r is not in the manifest" % flip)
    reuse = list(ov.get("reuse") or [])
    for rid in reuse:
        if rid not in sprites:
            raise SystemExit("art.json reuse target %r is not in the manifest" % rid)
    return {
        "id": sid,
        "family": family,
        "source_names": source_names,
        "chroma": chroma,
        "quantize": quantize,
        "wrap": bool(ov.get("wrap")),
        "stretch": bool(ov.get("stretch")),
        "flip": flip,
        "reuse": reuse,
        "sprites": sprites,
    }


def find_inbox(job):
    for name in job["source_names"]:
        path = INBOX / name
        if path.exists():
            return path
    return None


def job_dest_rels(job):
    sprites = job["sprites"]
    rels = []
    for fid in job["family"]:
        rels.extend(dest_rels(sprites[fid]))
    if job["flip"]:
        rels.extend(dest_rels(sprites[job["flip"]]))
    for rid in job["reuse"]:
        rels.extend(dest_rels(sprites[rid]))
    out = []
    seen = set()
    for rel in rels:
        if rel not in seen:
            seen.add(rel)
            out.append(rel)
    return out


def scale_game(pix, tw, th, stretch, quantize):
    out = pix.nn_scale(tw, th) if stretch else pix.fit_grounded(tw, th)
    if quantize:
        out = pg.quantize(out)
    return out


def actor_frames(pix, tw, th, quantize):
    f0 = scale_game(pix, tw, th, False, quantize)
    lifted = pix.shift(0, -max(1, pix.h // 80))
    f1 = scale_game(lifted, tw, th, False, quantize)
    if f0.opaque_count() and f1.opaque_count() == f0.opaque_count():
        f1 = f0.shift(0, 1)
    return [f0, f1]


def build_outputs(job, src_path):
    """Return list of (rel, Pix) for every dest this job writes."""
    sprites = job["sprites"]
    pix, kind, keyed, area = pg.prepare_source(src_path, chroma=job["chroma"])
    if pix is None:
        raise SystemExit("inbox %s is empty after chroma (key=%s)" % (src_path.name, kind))
    head = sprites[job["id"]]
    tw, th = int(head["w"]), int(head["h"])
    frames = int(head.get("frames") or 1)
    rels = dest_rels(head)
    first_rel = rels[0]
    is_actor = first_rel.startswith("actors/")
    outputs = []

    if job["wrap"] and len(job["family"]) >= 2:
        tile = pg.tile_square(pix).nn_scale(tw, th)
        if job["quantize"]:
            tile = pg.quantize(tile)
        wraps = [(0, 0), (8, 0), (0, 8), (8, 8)]
        for i, fid in enumerate(job["family"]):
            dx, dy = wraps[i] if i < len(wraps) else (0, 0)
            piece = tile.wrap(dx, dy) if (dx or dy) else tile
            for rel in dest_rels(sprites[fid]):
                outputs.append((rel, piece))
        return outputs

    if is_actor and frames >= 2:
        built = actor_frames(pix, tw, th, job["quantize"])
    elif frames >= 2:
        built = [scale_game(pix, tw, th, job["stretch"], job["quantize"])] * frames
    else:
        built = [scale_game(pix, tw, th, job["stretch"], job["quantize"])]

    for i, rel in enumerate(rels):
        outputs.append((rel, built[min(i, len(built) - 1)]))

    if job["flip"]:
        flip_rels = dest_rels(sprites[job["flip"]])
        for i, rel in enumerate(flip_rels):
            src = built[min(i, len(built) - 1)]
            outputs.append((rel, src.flip_h()))

    for rid in job["reuse"]:
        reuse_rels = dest_rels(sprites[rid])
        for i, rel in enumerate(reuse_rels):
            outputs.append((rel, built[min(i, len(built) - 1)]))

    return outputs


def nn_up(pix, scale):
    return pix.nn_scale(pix.w * scale, pix.h * scale)


def paste(dst: pg.Pix, src: pg.Pix, dx, dy):
    for y in range(src.h):
        for x in range(src.w):
            so = (y * src.w + x) * 4
            a = src.data[so + 3]
            if a <= 8:
                continue
            tx, ty = dx + x, dy + y
            if tx < 0 or ty < 0 or tx >= dst.w or ty >= dst.h:
                continue
            do = (ty * dst.w + tx) * 4
            dst.data[do : do + 4] = src.data[so : so + 4]


def fill_rect(dst: pg.Pix, x, y, w, h, rgba):
    r, g, b, a = rgba
    for yy in range(y, y + h):
        if yy < 0 or yy >= dst.h:
            continue
        for xx in range(x, x + w):
            if xx < 0 or xx >= dst.w:
                continue
            o = (yy * dst.w + xx) * 4
            dst.data[o : o + 4] = bytes((r, g, b, a))


def checker(w, h, cell=4):
    pix = pg.Pix(w, h)
    for y in range(h):
        for x in range(w):
            on = ((x // cell) + (y // cell)) & 1
            c = 48 if on else 36
            o = (y * w + x) * 4
            pix.data[o : o + 4] = bytes((c, c, c, 255))
    return pix


def write_compare(job, outputs, scale=4):
    PREVIEW.mkdir(parents=True, exist_ok=True)
    rows = []
    for rel, cand in outputs:
        shipped_path = ASSETS / rel
        if shipped_path.exists():
            cur = pg.Pix.load(shipped_path)
        else:
            cur = checker(cand.w, cand.h)
        rows.append((rel, nn_up(cur, scale), nn_up(cand, scale)))
        cand.save(PREVIEW / Path(rel).name)
    gap = 6
    header = 10
    col_w = max(a.w for _, a, b in rows) + max(b.w for _, a, b in rows) + gap + 8
    row_h = max(max(a.h, b.h) for _, a, b in rows) + gap
    sheet = pg.Pix(col_w, header + row_h * len(rows) + 4)
    fill_rect(sheet, 0, 0, sheet.w, sheet.h, (42, 26, 16, 255))
    fill_rect(sheet, 0, 0, sheet.w // 2, header, (58, 90, 44, 255))
    fill_rect(sheet, sheet.w // 2, 0, sheet.w - sheet.w // 2, header, (90, 42, 70, 255))
    y = header + 2
    for rel, cur, cand in rows:
        paste(sheet, cur, 4, y)
        paste(sheet, cand, 4 + cur.w + gap, y)
        y += row_h
    out = PREVIEW / ("compare-%s.png" % job["id"])
    sheet.save(out)
    return out


def pack_atlas():
    cmd = [sys.executable, str(ROOT / "tools" / "export-assets.py")]
    print("packing atlas…")
    r = subprocess.run(cmd, cwd=str(ROOT))
    if r.returncode != 0:
        raise SystemExit("export-assets.py failed (%s)" % r.returncode)


def git(*args, check=False):
    return subprocess.run(
        ["git", *args],
        cwd=str(ROOT),
        capture_output=True,
        text=True,
        check=check,
    )


def dest_dirty(rels):
    r = git("status", "--porcelain", "--", *[str(ASSETS / rel) for rel in rels])
    return bool(r.stdout.strip())


def cmd_status(sprites, art):
    print("inbox: %s" % INBOX)
    files = sorted(p for p in INBOX.iterdir() if p.suffix.lower() == ".png")
    if not files:
        print("  (empty)")
    mapped = set()
    overrides = art.get("overrides") or {}
    for path in files:
        stem = path.stem
        sid = stem if stem in sprites else None
        if sid is None:
            for oid, ov in overrides.items():
                if ov.get("source") == path.name:
                    sid = oid
                    break
        if sid is None:
            print("  %s  UNMAPPED" % path.name)
            continue
        job = resolve_job(sid, sprites, art)
        mapped.add(path.name)
        dests = ", ".join(job_dest_rels(job))
        print("  %s  → %s  [%s]" % (path.name, job["id"], dests))
    print("shipped sprites: %d" % len(sprites))
    refs = art.get("refs") or {}
    for key, rel in refs.items():
        ok = "ok" if (ASSETS / rel).exists() else "MISSING"
        print("  ref %s: %s (%s)" % (key, rel, ok))


def cmd_preview(job):
    src = find_inbox(job)
    if src is None:
        raise SystemExit(
            "no inbox file for %s (tried %s)" % (job["id"], ", ".join(job["source_names"]))
        )
    outputs = build_outputs(job, src)
    compare = write_compare(job, outputs)
    print("preview %s from %s" % (job["id"], src.relative_to(ROOT)))
    for rel, pix in outputs:
        print("  %s (%dx%d)" % (rel, pix.w, pix.h))
    print("  wrote %s" % compare.relative_to(ROOT))
    print("  left = shipped, right = inbox")
    print("shipped PNGs and atlas were not changed")


def cmd_promote(job):
    src = find_inbox(job)
    if src is None:
        raise SystemExit(
            "no inbox file for %s (tried %s)" % (job["id"], ", ".join(job["source_names"]))
        )
    outputs = build_outputs(job, src)
    for rel, pix in outputs:
        dest = ASSETS / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        pix.save(dest)
        print("  wrote %s (%dx%d)" % (rel, pix.w, pix.h))
    pack_atlas()
    print("promoted %s" % job["id"])


def cmd_restore(job):
    rels = job_dest_rels(job)
    paths = [str(ASSETS / rel) for rel in rels]
    if dest_dirty(rels):
        r = git("checkout", "HEAD", "--", *paths)
        if r.returncode != 0:
            raise SystemExit(r.stderr.strip() or "git checkout HEAD failed")
        print("reverted uncommitted %s to HEAD" % job["id"])
    else:
        log = git("log", "-2", "--pretty=%H", "--", *paths)
        commits = [line.strip() for line in log.stdout.splitlines() if line.strip()]
        if len(commits) < 2:
            raise SystemExit("no previous git version for %s" % ", ".join(rels))
        r = git("checkout", commits[1], "--", *paths)
        if r.returncode != 0:
            raise SystemExit(r.stderr.strip() or "git checkout failed")
        print("restored %s from %s" % (job["id"], commits[1][:10]))
    pack_atlas()


def main(argv=None):
    ap = argparse.ArgumentParser(description="Inbox → preview / promote / restore one sprite")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("status", help="list inbox files vs shipped sprites")
    p_prev = sub.add_parser("preview", help="process inbox to assets/preview, do not ship")
    p_prev.add_argument("id")
    p_prom = sub.add_parser("promote", help="write shipped PNG(s) and pack the atlas")
    p_prom.add_argument("id")
    p_rest = sub.add_parser("restore", help="put back the previous shipped PNG(s) and pack")
    p_rest.add_argument("id")
    args = ap.parse_args(argv)

    if not MANIFEST_PATH.exists():
        raise SystemExit("missing %s" % MANIFEST_PATH)
    manifest = load_json(MANIFEST_PATH)
    art = load_json(ART_JSON_PATH) if ART_JSON_PATH.exists() else {"overrides": {}, "refs": {}}
    sprites = sprite_map(manifest)
    INBOX.mkdir(parents=True, exist_ok=True)

    if args.cmd == "status":
        cmd_status(sprites, art)
        return

    job = resolve_job(args.id, sprites, art)
    if args.cmd == "preview":
        cmd_preview(job)
    elif args.cmd == "promote":
        cmd_promote(job)
    elif args.cmd == "restore":
        cmd_restore(job)


if __name__ == "__main__":
    main()
