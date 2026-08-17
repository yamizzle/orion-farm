#!/usr/bin/env python3
"""Chroma-key Imagine house furniture and emit native-size props (NN only)."""
from __future__ import annotations

import importlib.util
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
SRC_DIR = ASSETS / "generated-src"
PROPS = ASSETS / "props"
PREVIEW = Path("/tmp/house-furniture-preview")

spec = importlib.util.spec_from_file_location("pg", ROOT / "tools" / "process-generated.py")
pg = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pg)

AGENT = Path("/home/box/sand-data/agents/69b3f4ed-e3f8-4ba5-9073-59a5293c2321/assets")

SOURCES = {
    "window-night.png": "2d0a4f452cf1dc0c2b44e2814017850075eaaa54bd51b679ff9027f73f80b94b.png",
    "flowerbox.png": "dc1995a3515272020915120f7e79d997eb8acc72525f4c9f7471e8f356692be8.png",
    "fireplace.png": "5aa5ab92da92f5c2d4f968e304d0fcd7dc1594fb30410aa5a2ee0a52871b1777.png",
    "desk-chair.png": "c72b33f1ab5782d38f7adb8975e33393c1258d8489904c79165406785ef57218.png",
    "bed.png": "759cbdaa2d1b64ef40d27d7988e720ed3bbb9526408412cb2db27c78aa88d578.png",
    "rug.png": "829343e6fa9919ad8150e57f125ecbab7d9df31cbc65cbc5d3f2c4effa0f3f6f.png",
    "floor-lamp.png": "11bac05a8bae5e95095e5e1cae2f55f1bcd601b4d5b4a6d400e7feb50abb9aa1.png",
    "moon-table.png": "c9d7be33affab22a73184eaf88d446722256568fb8b0251af413b03cfe9107ab.png",
}


def keyed_crop(src_name: str, pad: int = 1) -> pg.Pix:
    pix, kind = pg.process_sprite(src_name)
    if pix is None:
        raise SystemExit("failed to process %s" % src_name)
    print("  keyed %s kind=%s crop=%dx%d" % (src_name, kind, pix.w, pix.h))
    return pix


def is_fire(r, g, b, a):
    if a <= 8:
        return False
    # warm flame / ember / candle
    if r >= 160 and g >= 40 and b <= 140 and r > b + 30:
        return True
    if r >= 200 and g >= 140 and b <= 120:
        return True
    return False


def fireplace_frame(pix: pg.Pix, frame: int) -> pg.Pix:
    out = pix.copy()
    if frame == 0:
        return out
    d = out.data
    for i in range(0, len(d), 4):
        r, g, b, a = d[i], d[i + 1], d[i + 2], d[i + 3]
        if not is_fire(r, g, b, a):
            continue
        # flicker: lift yellow core, pull some orange down
        if r >= 210 and g >= 160:
            d[i] = min(255, r + 18)
            d[i + 1] = min(255, g + 12)
            d[i + 2] = min(255, b + 8)
        else:
            d[i] = min(255, r + 10)
            d[i + 1] = max(0, g - 18)
            d[i + 2] = max(0, b - 8)
    # nudge a few fire pixels up by 1 for a second pose
    shifted = out.shift(0, -max(1, out.h // 48))
    # keep non-fire from original, fire from shifted where present
    mix = out.copy()
    for y in range(out.h):
        for x in range(out.w):
            r, g, b, a = shifted.get(x, y)
            if is_fire(r, g, b, a):
                so = (y * out.w + x) * 4
                mix.data[so : so + 4] = shifted.data[so : so + 4]
    return mix


def split_desk_chair(pix: pg.Pix):
    """Try left-chair / right-desk split. Returns (desk, chair) or (None, None)."""
    w, h = pix.w, pix.h
    # chair lives in the left ~38% and lower 75%
    chair_x1 = int(w * 0.40)
    chair_y0 = int(h * 0.28)
    chair = pix.crop(0, chair_y0, chair_x1, h)
    cbox = chair.opaque_bbox(pad=1)
    if cbox is None:
        return None, None
    chair = chair.crop(*cbox)

    # desk: skip the far-left chair-only strip, keep the tabletop + items
    desk_x0 = int(w * 0.18)
    desk = pix.crop(desk_x0, 0, w, int(h * 0.92))
    dbox = desk.opaque_bbox(pad=1)
    if dbox is None:
        return None, None
    desk = desk.crop(*dbox)

    # sanity: both should have a decent amount of pixels
    if chair.opaque_count() < 80 or desk.opaque_count() < 200:
        return None, None
    return desk, chair


def emit(pix: pg.Pix, rel: str, tw: int, th: int, stretch: bool = False):
    out = pix.nn_scale(tw, th) if stretch else pix.fit_grounded(tw, th)
    dest = ASSETS / rel
    out.save(dest)
    print("  wrote %s (%dx%d) from %dx%d stretch=%s" % (rel, tw, th, pix.w, pix.h, stretch))
    return out


def main():
    SRC_DIR.mkdir(parents=True, exist_ok=True)
    PREVIEW.mkdir(parents=True, exist_ok=True)
    for dest_name, src_name in SOURCES.items():
        src = AGENT / src_name
        dst = SRC_DIR / dest_name
        shutil.copy2(src, dst)
        print("copied", dest_name)

    # --- window night: 32x32 chunky 3/4 ---
    win = keyed_crop("window-night.png")
    emit(win, "props/windowNight.png", 32, 32)
    win.fit_grounded(32, 32).save(PREVIEW / "windowNight.png")

    # --- flower box: 32x16 under the window ---
    box = keyed_crop("flowerbox.png")
    emit(box, "props/flowerbox.png", 32, 16)
    box.fit_grounded(32, 16).save(PREVIEW / "flowerbox.png")

    # --- fireplace 32x48, two fire frames ---
    fire = keyed_crop("fireplace.png")
    f0 = fireplace_frame(fire, 0).fit_grounded(32, 48)
    f1 = fireplace_frame(fire, 1).fit_grounded(32, 48)
    f0.save(ASSETS / "props/fireplace-0.png")
    f1.save(ASSETS / "props/fireplace-1.png")
    f0.save(PREVIEW / "fireplace-0.png")
    f1.save(PREVIEW / "fireplace-1.png")
    print("  wrote props/fireplace-0/1.png (32x48)")

    # --- desk + chair ---
    pair = keyed_crop("desk-chair.png")
    # Chair tucks under the left of the desk — keep one 48x32 combo.
    emit(pair, "props/desk.png", 48, 32)
    pair.fit_grounded(48, 32).save(PREVIEW / "deskchair-48x32.png")
    desk, chair = split_desk_chair(pair)
    if chair:
        emit(chair, "props/chair.png", 16, 24)
        chair.fit_grounded(16, 24).save(PREVIEW / "chair.png")
    print("  COMBINED desk 48x32 (chair tucked under; chair PNG kept for collision)")

    # --- bed 32x32 (keep 2x2 collision) ---
    bed = keyed_crop("bed.png")
    emit(bed, "props/bed.png", 32, 32)
    bed.fit_grounded(32, 32).save(PREVIEW / "bed.png")

    # --- rug 48x32 walkable ---
    rug = keyed_crop("rug.png")
    emit(rug, "props/rug.png", 48, 32)
    rug.fit_grounded(48, 32).save(PREVIEW / "rug.png")

    # --- floor lamp 16x32 house-only ---
    lamp = keyed_crop("floor-lamp.png")
    emit(lamp, "props/houseLamp.png", 16, 32)
    lamp.fit_grounded(16, 32).save(PREVIEW / "houseLamp.png")

    # --- moon table 32x32 ---
    table = keyed_crop("moon-table.png")
    emit(table, "props/table.png", 32, 32)
    table.fit_grounded(32, 32).save(PREVIEW / "table.png")

    pg.print_report()
    print("done")


if __name__ == "__main__":
    main()
