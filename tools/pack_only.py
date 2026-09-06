#!/usr/bin/env python3
"""Pack assets/atlas.png from existing PNGs + manifest. No regen."""
from __future__ import annotations

import json
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
MANIFEST = ASSETS / "manifest.json"
ATLAS_PNG = ASSETS / "atlas.png"
ATLAS_JSON = ASSETS / "atlas.json"
PAD = 1

def scrub_chroma(im: Image.Image) -> Image.Image:
    """Key leftover generator pink / #FF00FF so it never ships opaque in the atlas."""
    im = im.convert("RGBA")
    pix = im.load()
    w, h = im.size
    for y in range(h):
        for x in range(w):
            r, g, b, a = pix[x, y]
            if a < 200:
                continue
            if (r >= 200 and b >= 200 and g <= 80) or (r > 180 and g < 50 and b > 80):
                pix[x, y] = (0, 0, 0, 0)
    return im




def frame_path(sprite, n):
    return sprite["file"].replace("{n}", str(n))


def pack():
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    sprites = data["sprites"]
    strips = []
    max_w = 0
    for spr in sprites:
        frames = []
        for n in range(spr.get("frames") or 1):
            im = scrub_chroma(Image.open(ASSETS / frame_path(spr, n)).convert("RGBA"))
            if im.size != (spr["w"], spr["h"]):
                # place into native canvas bottom-left if mismatch
                canvas = Image.new("RGBA", (spr["w"], spr["h"]), (0, 0, 0, 0))
                canvas.paste(im, (0, spr["h"] - im.size[1]))
                im = canvas
            frames.append(im)
        fw, fh = spr["w"], spr["h"]
        strip = Image.new("RGBA", (fw * len(frames), fh), (0, 0, 0, 0))
        for i, fr in enumerate(frames):
            strip.paste(fr, (i * fw, 0))
        strips.append((spr, strip))
        if strip.size[0] > max_w:
            max_w = strip.size[0]
    atlas_w = 256
    if max_w + PAD * 2 > atlas_w:
        atlas_w = max_w + PAD * 2
    strips.sort(key=lambda t: -t[1].size[1])
    x = PAD
    y = PAD
    row_h = 0
    placed = []
    for spr, strip in strips:
        sw, sh = strip.size
        if x + sw + PAD > atlas_w:
            x = PAD
            y += row_h + PAD
            row_h = 0
        placed.append((spr, strip, x, y))
        x += sw + PAD
        row_h = max(row_h, sh)
    atlas_h = y + row_h + PAD
    atlas = Image.new("RGBA", (atlas_w, atlas_h), (0, 0, 0, 0))
    out_sprites = []
    atlas_map = {}
    for spr, strip, px, py in placed:
        atlas.paste(strip, (px, py))
        rec = {
            "id": spr["id"],
            "file": spr["file"],
            "w": spr["w"],
            "h": spr["h"],
            "frames": spr.get("frames", 1),
            "anchor": spr.get("anchor", [0, 0]),
            "ox": spr.get("ox", 0),
            "oy": spr.get("oy", 0),
            "x": px,
            "y": py,
            "fw": spr["w"],
        }
        if spr.get("generated"):
            rec["generated"] = True
        out_sprites.append(rec)
        atlas_map[spr["id"]] = {
            "x": px, "y": py, "w": strip.size[0], "h": strip.size[1],
            "fw": spr["w"], "frames": spr.get("frames", 1),
            "anchor": spr.get("anchor", [0, 0]),
            "ox": spr.get("ox", 0), "oy": spr.get("oy", 0),
        }
    atlas.save(ATLAS_PNG)
    data["sprites"] = out_sprites
    MANIFEST.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    ATLAS_JSON.write_text(json.dumps({"image": "atlas.png", "sprites": atlas_map}, indent=2) + "\n", encoding="utf-8")
    print("packed %s (%dx%d) sprites=%d" % (ATLAS_PNG, atlas_w, atlas_h, len(out_sprites)))


if __name__ == "__main__":
    pack()
