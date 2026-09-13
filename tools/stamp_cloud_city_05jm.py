#!/usr/bin/env python3
"""Stamp Grok Imagine Cloud City sources → live assets (BUILD 20260905jm).

Magenta/hot-pink chroma (flood), BOX/AREA downsample, pink-chroma gate fail-closed.
cloudFloor: opaque seamless — square crop + AREA only (no key).
Atlas 1477 untouched.
"""
from __future__ import annotations

import shutil
import sys
from collections import Counter, deque
from pathlib import Path

import numpy as np
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "assets" / "generated-src" / "cloud-city"
PROPS = ROOT / "assets" / "props"
UI = ROOT / "assets" / "ui"
ACTORS = ROOT / "assets" / "actors"

# Per-sheet quadrant → facing (from visual inspect of keyed sheets)
FACING_MAP = {
    "nimbus": {"TL": "down", "TR": "right", "BL": "left", "BR": "up"},
    "cirrus": {"TL": "down", "TR": "left", "BL": "right", "BR": "up"},
    "cumulus": {"TL": "down", "TR": "left", "BL": "right", "BR": "up"},
    "dew": {"TL": "up", "TR": "left", "BL": "right", "BR": "down"},
    "breeze": {"TL": "down", "TR": "left", "BL": "right", "BR": "up"},
}

PROP_JOBS = [
    ("cloudFloor-src.png", PROPS / "cloudFloor.png", 32, 32, "floor"),
    ("cloudEdge-src.png", PROPS / "cloudEdge.png", 64, 64, "ground"),
    ("cloudWall-src.png", PROPS / "cloudWall.png", 64, 64, "ground"),
    ("cloudLedge-src.png", PROPS / "cloudLedge.png", 96, 48, "letterbox"),
    ("cloudShopFood-src.png", PROPS / "cloudShopFood.png", 96, 112, "ground"),
    ("cloudShopHat-src.png", PROPS / "cloudShopHat.png", 96, 112, "ground"),
    ("cloudShopPotion-src.png", PROPS / "cloudShopPotion.png", 96, 112, "ground"),
    ("cloudShopWeapons-src.png", PROPS / "cloudShopWeapons.png", 96, 112, "ground"),
    ("cloudShopWizard-src.png", PROPS / "cloudShopWizard.png", 96, 112, "ground"),
]

UI_JOBS = [
    ("cloudPuff-src.png", UI / "cloudPuff.png", 32, 32),
    ("skyJam-src.png", UI / "skyJam.png", 32, 32),
    ("fluffySoup-src.png", UI / "fluffySoup.png", 32, 32),
    ("starCookie-src.png", UI / "starCookie.png", 32, 32),
    ("heartPotion-src.png", UI / "heartPotion.png", 32, 32),
    ("redHat-src.png", UI / "redHat.png", 32, 32),
]


def chroma_flood(im: Image.Image) -> Image.Image:
    a = np.array(im.convert("RGBA"), dtype=np.uint8)
    h, w = a.shape[:2]
    r = a[:, :, 0].astype(np.int16)
    g = a[:, :, 1].astype(np.int16)
    b = a[:, :, 2].astype(np.int16)
    al = a[:, :, 3]
    rb = (r + b) // 2
    mag = (
        ((g < 90) & (r >= 170) & (b >= 155) & ((rb - g) >= 85))
        | ((r >= 180) & (g < 55) & (b >= 80))
        | ((r >= 200) & (g < 70) & (b >= 120) & ((r - g) >= 120))
        | ((r >= 210) & (g <= 50) & (b >= 100))
    )
    border = np.concatenate([a[0, :, :3], a[-1, :, :3], a[:, 0, :3], a[:, -1, :3]])
    keys = [tuple((p // 8 * 8).tolist()) for p in border]
    mode = np.array(Counter(keys).most_common(1)[0][0], dtype=np.int16)
    dist = (
        np.abs(a[:, :, 0].astype(np.int16) - mode[0])
        + np.abs(a[:, :, 1].astype(np.int16) - mode[1])
        + np.abs(a[:, :, 2].astype(np.int16) - mode[2])
    )
    near_mode = dist <= 48
    seed = mag | near_mode
    marked = np.zeros((h, w), dtype=bool)
    q: deque = deque()
    for x in range(w):
        for y in (0, h - 1):
            if seed[y, x]:
                marked[y, x] = True
                q.append((y, x))
    for y in range(h):
        for x in (0, w - 1):
            if seed[y, x] and not marked[y, x]:
                marked[y, x] = True
                q.append((y, x))
    while q:
        cy, cx = q.popleft()
        for dy, dx in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            ny, nx = cy + dy, cx + dx
            if 0 <= ny < h and 0 <= nx < w and not marked[ny, nx] and seed[ny, nx]:
                marked[ny, nx] = True
                q.append((ny, nx))
    marked |= mag
    loose = ((g < 130) & (r >= 140) & (b >= 100) & ((rb - g) >= 45)) | (
        (r >= 170) & (g < 80) & (b >= 70)
    )
    up = np.zeros_like(marked)
    up[1:] = marked[:-1]
    down = np.zeros_like(marked)
    down[:-1] = marked[1:]
    left = np.zeros_like(marked)
    left[:, 1:] = marked[:, :-1]
    right = np.zeros_like(marked)
    right[:, :-1] = marked[:, 1:]
    marked |= loose & (up | down | left | right)
    out = a.copy()
    out[marked | (al <= 8), 3] = 0
    return Image.fromarray(out)


def keep_largest_cc(im: Image.Image, min_frac: float = 0.02) -> Image.Image:
    """Drop label glyphs / tiny islands; keep largest opaque component (+ nearby mid-size)."""
    a = np.array(im)
    mask = a[:, :, 3] > 8
    h, w = mask.shape
    seen = np.zeros_like(mask, dtype=bool)
    comps = []
    for y in range(h):
        for x in range(w):
            if not mask[y, x] or seen[y, x]:
                continue
            q = deque([(y, x)])
            seen[y, x] = True
            cells = []
            while q:
                cy, cx = q.popleft()
                cells.append((cy, cx))
                for dy, dx in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                    ny, nx = cy + dy, cx + dx
                    if 0 <= ny < h and 0 <= nx < w and mask[ny, nx] and not seen[ny, nx]:
                        seen[ny, nx] = True
                        q.append((ny, nx))
            comps.append(cells)
    if not comps:
        return im
    comps.sort(key=len, reverse=True)
    keep = np.zeros_like(mask, dtype=bool)
    total = mask.sum()
    # always keep largest; also keep components >= min_frac of largest (particles near body)
    largest_n = len(comps[0])
    for cells in comps:
        if len(cells) >= max(40, int(largest_n * min_frac)) or len(cells) >= total * 0.01:
            # only keep if close to largest bbox (avoid distant labels)
            ys = [c[0] for c in cells]
            xs = [c[1] for c in cells]
            lys = [c[0] for c in comps[0]]
            lxs = [c[1] for c in comps[0]]
            lcy, lcx = sum(lys) / len(lys), sum(lxs) / len(lxs)
            cy, cx = sum(ys) / len(ys), sum(xs) / len(xs)
            if cells is comps[0] or (
                abs(cy - lcy) < h * 0.45 and abs(cx - lcx) < w * 0.45 and len(cells) > 80
            ):
                for cyi, cxi in cells:
                    keep[cyi, cxi] = True
    # always keep largest fully
    for cyi, cxi in comps[0]:
        keep[cyi, cxi] = True
    out = a.copy()
    out[~keep, 3] = 0
    return Image.fromarray(out)


def crop_opaque(im: Image.Image, pad: int = 1) -> Image.Image:
    bbox = im.getbbox()
    if not bbox:
        return im
    x0, y0, x1, y1 = bbox
    x0 = max(0, x0 - pad)
    y0 = max(0, y0 - pad)
    x1 = min(im.size[0], x1 + pad)
    y1 = min(im.size[1], y1 + pad)
    return im.crop((x0, y0, x1, y1))


def grounded_box(im: Image.Image, tw: int, th: int) -> Image.Image:
    """BOX downsample to fit, paste bottom-center (area_promote style)."""
    w, h = im.size
    if w <= 0 or h <= 0:
        return Image.new("RGBA", (tw, th), (0, 0, 0, 0))
    scale = min(tw / w, th / h)
    nw = max(1, min(tw, int(round(w * scale))))
    nh = max(1, min(th, int(round(h * scale))))
    mid_w = min(tw * 2, max(nw * 2, 1))
    mid_h = min(th * 2, max(nh * 2, 1))
    mid_scale = min(mid_w / w, mid_h / h)
    mw = max(1, int(round(w * mid_scale)))
    mh = max(1, int(round(h * mid_scale)))
    if mw > nw and mh > nh:
        mid = im.resize((mw, mh), Image.BOX)
        scaled = mid.resize((nw, nh), Image.NEAREST)
    else:
        scaled = im.resize((nw, nh), Image.BOX)
    canvas = Image.new("RGBA", (tw, th), (0, 0, 0, 0))
    ox = (tw - nw) // 2
    oy = th - nh
    canvas.paste(scaled, (ox, oy), scaled)
    return canvas


def letterbox_box(im: Image.Image, tw: int, th: int) -> Image.Image:
    """Keep aspect inside tw×th, centered (for cloudLedge)."""
    w, h = im.size
    if w <= 0 or h <= 0:
        return Image.new("RGBA", (tw, th), (0, 0, 0, 0))
    scale = min(tw / w, th / h)
    nw = max(1, min(tw, int(round(w * scale))))
    nh = max(1, min(th, int(round(h * scale))))
    scaled = im.resize((nw, nh), Image.BOX)
    canvas = Image.new("RGBA", (tw, th), (0, 0, 0, 0))
    ox = (tw - nw) // 2
    oy = (th - nh) // 2
    canvas.paste(scaled, (ox, oy), scaled)
    return canvas


def count_pink(im: Image.Image) -> int:
    a = np.array(im.convert("RGBA"))
    r, g, b, al = a[:, :, 0], a[:, :, 1], a[:, :, 2], a[:, :, 3]
    opaque = al >= 200
    pink = opaque & (
        ((r >= 200) & (b >= 200) & (g <= 80))
        | ((r > 180) & (g < 50) & (b > 80))
        | ((r >= 210) & (g <= 40) & (b >= 100))
    )
    return int(pink.sum())


def gate(im: Image.Image, label: str) -> None:
    n = count_pink(im)
    if n > 0:
        raise SystemExit("PINK-CHROMA GATE FAIL %s pink_px=%d" % (label, n))
    print("  pink gate PASS %s (0 pink)" % label)


def process_floor(src: Path, dest: Path, tw: int, th: int) -> None:
    im = Image.open(src).convert("RGBA")
    w, h = im.size
    side = min(w, h)
    x0 = (w - side) // 2
    y0 = (h - side) // 2
    sq = im.crop((x0, y0, x0 + side, y0 + side))
    out = sq.resize((tw, th), Image.BOX)
    # ensure fully opaque
    a = np.array(out)
    a[:, :, 3] = 255
    out = Image.fromarray(a)
    gate(out, dest.name)
    dest.parent.mkdir(parents=True, exist_ok=True)
    out.save(dest)
    print("  wrote %s %dx%d %d bytes" % (dest, out.size[0], out.size[1], dest.stat().st_size))


def process_keyed(src: Path, dest: Path, tw: int, th: int, mode: str) -> None:
    im = chroma_flood(Image.open(src))
    im = keep_largest_cc(im)
    im = crop_opaque(im)
    if mode == "letterbox":
        out = letterbox_box(im, tw, th)
    else:
        out = grounded_box(im, tw, th)
    gate(out, dest.name)
    dest.parent.mkdir(parents=True, exist_ok=True)
    out.save(dest)
    print("  wrote %s %dx%d opaque=%d %d bytes" % (
        dest, out.size[0], out.size[1],
        sum(1 for p in out.getdata() if p[3] > 8),
        dest.stat().st_size,
    ))


def process_folk_sheet(name: str) -> None:
    src = SRC / ("%s-sheet-src.png" % name)
    im = chroma_flood(Image.open(src))
    w, h = im.size
    mid_x, mid_y = w // 2, h // 2
    quads = {
        "TL": im.crop((0, 0, mid_x, mid_y)),
        "TR": im.crop((mid_x, 0, w, mid_y)),
        "BL": im.crop((0, mid_y, mid_x, h)),
        "BR": im.crop((mid_x, mid_y, w, h)),
    }
    fmap = FACING_MAP[name]
    for qn, face in fmap.items():
        q = quads[qn]
        q = keep_largest_cc(q, min_frac=0.03)
        q = crop_opaque(q)
        out = grounded_box(q, 32, 48)
        gate(out, "%s-%s" % (name, face))
        for fr in (0, 1):
            dest = ACTORS / ("%s-%s-%d.png" % (name, face, fr))
            out.save(dest)
        print("  %s-%s 32x48 (x2 frames) %d bytes" % (name, face, (ACTORS / ("%s-%s-0.png" % (name, face))).stat().st_size))


def main() -> None:
    print("=== Cloud City Imagine stamp 05jm ===")
    for src_name, dest, tw, th, mode in PROP_JOBS:
        src = SRC / src_name
        print("prop", src_name, "→", dest.name, "%dx%d" % (tw, th), mode)
        if mode == "floor":
            process_floor(src, dest, tw, th)
        else:
            process_keyed(src, dest, tw, th, mode)
    for src_name, dest, tw, th in UI_JOBS:
        print("ui", src_name, "→", dest.name)
        process_keyed(SRC / src_name, dest, tw, th, "ground")
    for name in ("nimbus", "cirrus", "cumulus", "dew", "breeze"):
        print("folk", name)
        process_folk_sheet(name)
    # atlas height guard
    atlas = Image.open(ROOT / "assets" / "atlas.png")
    assert atlas.size[1] == 1477, "atlas height changed %s" % (atlas.size,)
    print("atlas keep 256x1477 OK")
    print("DONE")


if __name__ == "__main__":
    main()
