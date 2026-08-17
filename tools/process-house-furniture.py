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
    "window-night.png": "da1aa3b38cbcbf0521bd81322ff20b88d1c6b4eea1b94e978df3fc03b3eb18dd.png",
    "fireplace.png": "2fff7c8bd10f149ea7202f192f993be826f5ebbeea55bc2350caa819375f3ce1.png",
    "desk-chair.png": "b3667dfe580ce2eed18c1e6b67004b71bbf090372c0d2ad8ab996f58c52b8340.png",
    "bed.png": "b32bd70b2c614f0cbcd5a7c73c9f6047210117e039cfb1911887d3f645f6ba5b.png",
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

    # --- window night: 32x40 (taller night casement, house only) ---
    win = keyed_crop("window-night.png")
    print("  window crop aspect %.3f (w/h)" % (win.w / max(1, win.h)))
    emit(win, "props/windowNight.png", 32, 40)
    win.fit_grounded(32, 40).save(PREVIEW / "windowNight.png")

    # --- fireplace 48x64, two fire frames ---
    fire = keyed_crop("fireplace.png")
    print("  fireplace crop aspect %.3f (w/h)" % (fire.w / max(1, fire.h)))
    f0 = fireplace_frame(fire, 0).fit_grounded(48, 64)
    f1 = fireplace_frame(fire, 1).fit_grounded(48, 64)
    f0.save(ASSETS / "props/fireplace-0.png")
    f1.save(ASSETS / "props/fireplace-1.png")
    f0.save(PREVIEW / "fireplace-0.png")
    f1.save(PREVIEW / "fireplace-1.png")
    print("  wrote props/fireplace-0/1.png (48x64)")

    # --- desk + chair stay one 64x48 sprite ---
    pair = keyed_crop("desk-chair.png")
    print("  desk crop aspect %.3f (w/h)" % (pair.w / max(1, pair.h)))
    emit(pair, "props/desk.png", 64, 48)
    pair.fit_grounded(64, 48).save(PREVIEW / "deskchair-64x48.png")
    print("  COMBINED desk 64x48 (chair tucked under)")

    # --- bed 48x48 (keep 2x2 collision) ---
    bed = keyed_crop("bed.png")
    print("  bed crop aspect %.3f (w/h)" % (bed.w / max(1, bed.h)))
    emit(bed, "props/bed.png", 48, 48)
    bed.fit_grounded(48, 48).save(PREVIEW / "bed.png")

    pg.print_report()
    print("done")


if __name__ == "__main__":
    main()
