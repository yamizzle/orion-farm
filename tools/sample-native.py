#!/usr/bin/env python3
"""Sample Grok Imagine chunky-pixel art down to native game pixels.

Imagine cannot emit a 16x16 file. It draws BIG blocks. Do NOT bilinear
resize the whole PNG — that is the muddy bug.

1. Chroma-key magenta #FF00FF
2. Crop each sprite from a sheet
3. Find the pixel-block size (image pixels per game pixel)
4. Sample the CENTER of each block
5. Write an exact WxH PNG (never interpolate)
"""
from __future__ import annotations

import importlib.util
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
SRC_DIR = ASSETS / "generated-src"
AGENT = Path("/home/box/sand-data/agents/69b3f4ed-e3f8-4ba5-9073-59a5293c2321/assets")
PREVIEW = Path("/tmp/native-sample-preview")

spec = importlib.util.spec_from_file_location("pg", ROOT / "tools" / "process-generated.py")
pg = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pg)


SOURCES = {
    "mine-tiles.png": "58098f37b6cd06d50a9227b596cb6bd57e893beccaba2fc93f05ae094c69c1d4.png",
    "mine-critters.png": "c48fe64b9514a51cf4c3167d8933ed97fa1f19f7839c8354069e4bf4de0e4b55.png",
    "mine-loot.png": "f57e97d3f166c6d9ed4b2c9136d7b265e4734188ec73f300c23bffec57f28555.png",
    "mine-props.png": "d42c918720f2fafa0b940bcee673afde58cc4324b06671634cb5ad9630fcddc7.png",
}

# Capped-wall sheets: LEFT = floor, RIGHT = 3/4 wall. Do not write stone0/1.
WALL_SHEETS = {
    "mine-floor-wall-f13.png": (
        "235bdd1aae77ac26e11ae859556e7d41c4518d17a0864a3d4cf1592dcbc29d6f.png",
        ["tiles/mineFloor.png", "tiles/mineWall.png"],
    ),
    "mine-floor-wall-f46.png": (
        "92b57ff4b7e8c9a8f5a4b0c75c72c1caf757887096985ba58831d0ad0c6fde6d.png",
        ["tiles/deepFloor.png", "tiles/deepWall.png"],
    ),
}


def chroma_magenta(pix: pg.Pix) -> pg.Pix:
    """Key #FF00FF and a tight pink fringe. Keep purples (deep wall / crystal bat)."""
    out = pix.copy()
    d = out.data
    for i in range(0, len(d), 4):
        r, g, b, a = d[i], d[i + 1], d[i + 2], d[i + 3]
        if a <= 8:
            d[i + 3] = 0
            continue
        if r >= 220 and b >= 220 and g <= 40:
            d[i + 3] = 0
            continue
        if r >= 200 and b >= 200 and g <= 70 and abs(r - b) <= 30:
            d[i + 3] = 0
            continue
        # generator fringe: hot pink, not crystal purple
        if g <= 80 and r >= 200 and b >= 180 and r + b - 2 * g >= 220:
            d[i + 3] = 0
    return out


def connected_boxes(pix: pg.Pix, min_pixels: int = 200):
    w, h = pix.w, pix.h
    seen = bytearray(w * h)
    boxes = []
    for y in range(h):
        row = y * w
        for x in range(w):
            i = row + x
            if seen[i] or pix.data[i * 4 + 3] <= 8:
                continue
            stack = [i]
            seen[i] = 1
            minx = maxx = x
            miny = maxy = y
            n = 0
            while stack:
                j = stack.pop()
                n += 1
                jx = j % w
                jy = j // w
                if jx < minx:
                    minx = jx
                if jx > maxx:
                    maxx = jx
                if jy < miny:
                    miny = jy
                if jy > maxy:
                    maxy = jy
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nx, ny = jx + dx, jy + dy
                    if nx < 0 or ny < 0 or nx >= w or ny >= h:
                        continue
                    k = ny * w + nx
                    if seen[k] or pix.data[k * 4 + 3] <= 8:
                        continue
                    seen[k] = 1
                    stack.append(k)
            if n >= min_pixels:
                boxes.append((minx, miny, maxx + 1, maxy + 1, n))
    return boxes


def sort_boxes(boxes, rows: int, cols: int, img_h: int):
    """Left-to-right, top-to-bottom by center, using expected row count."""
    if not boxes:
        return boxes
    if rows <= 1:
        return sorted(boxes, key=lambda b: (b[0] + b[2]) / 2)
    # bucket by center-y into `rows` bands
    labeled = []
    for b in boxes:
        cy = (b[1] + b[3]) / 2
        labeled.append((cy, (b[0] + b[2]) / 2, b))
    labeled.sort(key=lambda t: t[0])
    # split into `rows` groups of `cols` (or as even as possible)
    out = []
    n = len(labeled)
    for r in range(rows):
        lo = int(round(r * n / rows))
        hi = int(round((r + 1) * n / rows))
        band = labeled[lo:hi]
        band.sort(key=lambda t: t[1])
        out.extend(t[2] for t in band)
    return out


def crop_box(pix: pg.Pix, box) -> pg.Pix:
    return pix.crop(box[0], box[1], box[2], box[3])


def sample_native(pix: pg.Pix, tw: int, th: int) -> tuple[pg.Pix, float, float]:
    """Point-sample the CENTER of each game-pixel cell. No interpolation.

    Block size is (crop_w / tw, crop_h / th) — the Imagine sprite is one
    native WxH drawing made of big blocks.
    """
    box = pix.opaque_bbox(pad=0)
    if box is None:
        return pg.Pix(tw, th), 1.0, 1.0
    crop = pix.crop(*box)
    bx = crop.w / tw
    by = crop.h / th
    out = pg.Pix(tw, th)
    for y in range(th):
        sy = int((y + 0.5) * crop.h / th)
        if sy >= crop.h:
            sy = crop.h - 1
        for x in range(tw):
            sx = int((x + 0.5) * crop.w / tw)
            if sx >= crop.w:
                sx = crop.w - 1
            r, g, b, a = crop.get(sx, sy)
            o = (y * tw + x) * 4
            out.data[o : o + 4] = bytes((r, g, b, a))
    return out, bx, by


def nn_preview(pix: pg.Pix, scale: int = 8) -> pg.Pix:
    return pix.nn_scale(pix.w * scale, pix.h * scale)


def write_sprite(pix: pg.Pix, rel: str, tw: int, th: int) -> tuple[pg.Pix, float, float]:
    out, bx, by = sample_native(pix, tw, th)
    dest = ASSETS / rel
    dest.parent.mkdir(parents=True, exist_ok=True)
    out.save(dest)
    nn_preview(out).save(PREVIEW / Path(rel).name)
    print("  wrote %s  %dx%d  block=%.1fx%.1f  from %dx%d" % (rel, out.w, out.h, bx, by, pix.w, pix.h))
    return out, bx, by


def load_keyed(name: str) -> pg.Pix:
    pix = pg.Pix.load(SRC_DIR / name)
    keyed = chroma_magenta(pix)
    print("keyed %s %dx%d  opaque=%d" % (name, keyed.w, keyed.h, keyed.opaque_count()))
    return keyed


def boxes_for(pix: pg.Pix, expect: int, cols: int, rows: int = 1):
    boxes = connected_boxes(pix, min_pixels=max(80, pix.w * pix.h // 500))
    boxes = sort_boxes(boxes, rows, cols, pix.h)
    print("  components=%d expect=%d" % (len(boxes), expect))
    if len(boxes) != expect:
        boxes2 = connected_boxes(pix, min_pixels=80)
        boxes2 = sort_boxes(boxes2, rows, cols, pix.h)
        print("  components(loose)=%d" % len(boxes2))
        if len(boxes2) == expect:
            boxes = boxes2
    return boxes


def main():
    SRC_DIR.mkdir(parents=True, exist_ok=True)
    PREVIEW.mkdir(parents=True, exist_ok=True)

    for dest_name, src_name in SOURCES.items():
        src = AGENT / src_name
        dst = SRC_DIR / dest_name
        if not src.exists():
            raise SystemExit("missing source %s" % src)
        shutil.copy2(src, dst)
        print("copied", dest_name, "(%d bytes)" % dst.stat().st_size)

    report = []

    tiles = load_keyed("mine-tiles.png")
    tboxes = boxes_for(tiles, 4, 4, 1)
    tnames = [
        "tiles/stone0.png",
        "tiles/deepFloor.png",
        "tiles/mineWall.png",
        "tiles/deepWall.png",
    ]
    stone0 = None
    for i, rel in enumerate(tnames):
        if i >= len(tboxes):
            print("  MISSING", rel)
            continue
        out, bx, by = write_sprite(crop_box(tiles, tboxes[i]), rel, 16, 16)
        report.append((rel, bx, by, out.w, out.h))
        if i == 0:
            stone0 = out
    if stone0 is not None:
        v = stone0.wrap(5, 3)
        v.save(ASSETS / "tiles/stone1.png")
        nn_preview(v).save(PREVIEW / "stone1.png")
        print("  wrote tiles/stone1.png  16x16  wrap-shift variant")
        report.append(("tiles/stone1.png", 0, 0, 16, 16))

    crit = load_keyed("mine-critters.png")
    cboxes = boxes_for(crit, 4, 4, 1)
    cnames = ["slime", "rockgrub", "bat", "crystalbat"]
    for i, name in enumerate(cnames):
        if i >= len(cboxes):
            print("  MISSING", name)
            continue
        f0, bx, by = write_sprite(crop_box(crit, cboxes[i]), "actors/%s-0.png" % name, 16, 16)
        report.append(("actors/%s-0.png" % name, bx, by, f0.w, f0.h))
        if name in ("bat", "crystalbat"):
            f1 = f0.shift(0, -1)
        elif name == "rockgrub":
            f1 = f0.shift(1, 0)
        else:
            f1 = f0.shift(0, -1)
        dest = ASSETS / ("actors/%s-1.png" % name)
        f1.save(dest)
        nn_preview(f1).save(PREVIEW / ("%s-1.png" % name))
        print("  wrote actors/%s-1.png  16x16  1px shift" % name)
        report.append(("actors/%s-1.png" % name, bx, by, 16, 16))

    loot = load_keyed("mine-loot.png")
    lboxes = boxes_for(loot, 6, 3, 2)
    lnames = [
        "ui/copper.png",
        "ui/iron.png",
        "ui/gem.png",
        "ui/sapphire.png",
        "ui/goldPile.png",
        "ui/pebble.png",
    ]
    for i, rel in enumerate(lnames):
        if i >= len(lboxes):
            print("  MISSING", rel)
            continue
        out, bx, by = write_sprite(crop_box(loot, lboxes[i]), rel, 16, 16)
        report.append((rel, bx, by, out.w, out.h))

    props = load_keyed("mine-props.png")
    pboxes = boxes_for(props, 3, 3, 1)
    pnames = [
        ("props/ladder.png", 16, 24),
        ("props/hole.png", 16, 24),
        ("props/moonAltar.png", 16, 32),
    ]
    for i, (rel, tw, th) in enumerate(pnames):
        if i >= len(pboxes):
            print("  MISSING", rel)
            continue
        out, bx, by = write_sprite(crop_box(props, pboxes[i]), rel, tw, th)
        report.append((rel, bx, by, out.w, out.h))

    sample_capped_walls(report)

    print("\n=== native sample report ===")
    for rel, bx, by, w, h in report:
        print("  %-28s  block=%.1fx%.1f  out=%dx%d" % (rel, bx, by, w, h))
    print("previews in", PREVIEW)


def _is_key_pixel(r, g, b, a):
    if a <= 8:
        return True
    if r >= 220 and b >= 220 and g <= 40:
        return True
    if r >= 200 and b >= 200 and g <= 70 and abs(r - b) <= 30:
        return True
    if g <= 80 and r >= 200 and b >= 180 and r + b - 2 * g >= 220:
        return True
    return False


def fill_key_holes(pix: pg.Pix) -> int:
    """Replace leftover magenta / transparent samples with nearest opaque pixel."""
    bad = []
    good = []
    for y in range(pix.h):
        for x in range(pix.w):
            r, g, b, a = pix.get(x, y)
            if _is_key_pixel(r, g, b, a):
                bad.append((x, y))
            else:
                good.append((x, y, r, g, b))
    for x, y in bad:
        best = good[0][2:] if good else (20, 16, 14)
        bd = 10 ** 9
        for gx, gy, r, g, b in good:
            d = (gx - x) * (gx - x) + (gy - y) * (gy - y)
            if d < bd:
                bd = d
                best = (r, g, b)
        o = (y * pix.w + x) * 4
        pix.data[o : o + 4] = bytes((best[0], best[1], best[2], 255))
    return len(bad)


def sample_capped_walls(report):
    """Point-sample Imagine floor+capped-wall sheets. Never writes stone0/1."""
    for dest_name, (src_name, rels) in WALL_SHEETS.items():
        src = AGENT / src_name
        dst = SRC_DIR / dest_name
        if not src.exists():
            print("  missing capped-wall source", src_name)
            continue
        shutil.copy2(src, dst)
        keyed = chroma_magenta(pg.Pix.load(dst))
        print("keyed %s %dx%d  opaque=%d" % (dest_name, keyed.w, keyed.h, keyed.opaque_count()))
        boxes = boxes_for(keyed, 2, 2, 1)
        for i, rel in enumerate(rels):
            if i >= len(boxes):
                print("  MISSING", rel)
                continue
            out, bx, by = write_sprite(crop_box(keyed, boxes[i]), rel, 16, 16)
            n = fill_key_holes(out)
            if n:
                dest = ASSETS / rel
                out.save(dest)
                nn_preview(out).save(PREVIEW / Path(rel).name)
                print("  filled %d key holes in %s" % (n, rel))
            report.append((rel, bx, by, out.w, out.h))
        if rels[0] == "tiles/mineFloor.png":
            floor = pg.Pix.load(ASSETS / "tiles/mineFloor.png")
            v = floor.wrap(5, 3)
            v.save(ASSETS / "tiles/mineFloor1.png")
            nn_preview(v).save(PREVIEW / "mineFloor1.png")
            print("  wrote tiles/mineFloor1.png  16x16  wrap-shift variant")
            report.append(("tiles/mineFloor1.png", 0, 0, 16, 16))


if __name__ == "__main__":
    main()
