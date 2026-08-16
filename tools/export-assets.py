#!/usr/bin/env python3
"""Paint original 16-bit 3/4 sprites, write PNGs, and pack assets/atlas.png.

Usage:
  python3 tools/export-assets.py          # generate missing PNGs, pack atlas
  python3 tools/export-assets.py --regen  # rebuild built-in PNGs from this file

Add a sprite later:
  1. Drop a PNG under assets/tiles, assets/props, assets/actors, or assets/ui
  2. Add one object to assets/manifest.json (id, file, w, h, frames, anchor)
  3. Re-run this script to rebuild the atlas
"""
from __future__ import annotations

import argparse
import json
import math
import struct
import sys
import zlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
PALETTE_PATH = ASSETS / "palette.json"
MANIFEST_PATH = ASSETS / "manifest.json"
ATLAS_PNG = ASSETS / "atlas.png"
ATLAS_JSON = ASSETS / "atlas.json"
PREVIEW_PATH = ASSETS / "preview.png"


def parse_color(c):
    if c is None:
        return (0, 0, 0, 0)
    if isinstance(c, tuple):
        if len(c) == 3:
            return (c[0], c[1], c[2], 255)
        return c
    if isinstance(c, str) and c.startswith("rgba"):
        body = c[c.find("(") + 1 : c.rfind(")")]
        parts = [p.strip() for p in body.split(",")]
        r, g, b = int(parts[0]), int(parts[1]), int(parts[2])
        a = float(parts[3]) if len(parts) > 3 else 1.0
        return (r, g, b, max(0, min(255, int(round(a * 255)))))
    if isinstance(c, str) and c.startswith("#"):
        h = c[1:]
        if len(h) == 3:
            h = "".join(ch * 2 for ch in h)
        r = int(h[0:2], 16)
        g = int(h[2:4], 16)
        b = int(h[4:6], 16)
        a = int(h[6:8], 16) if len(h) == 8 else 255
        return (r, g, b, a)
    raise ValueError("bad color %r" % (c,))


def crc32(data: bytes) -> int:
    return zlib.crc32(data) & 0xFFFFFFFF


def write_png(path: Path, w: int, h: int, rgba: bytes) -> None:
    def chunk(tag: bytes, data: bytes) -> bytes:
        return struct.pack(">I", len(data)) + tag + data + struct.pack(">I", crc32(tag + data))

    raw = b"".join(b"\x00" + bytes(rgba[y * w * 4 : (y + 1) * w * 4]) for y in range(h))
    ihdr = struct.pack(">IIBBBBB", w, h, 8, 6, 0, 0, 0)
    png = b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", ihdr) + chunk(b"IDAT", zlib.compress(raw, 9)) + chunk(b"IEND", b"")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(png)


def paeth(a, b, c):
    p = a + b - c
    pa, pb, pc = abs(p - a), abs(p - b), abs(p - c)
    if pa <= pb and pa <= pc:
        return a
    if pb <= pc:
        return b
    return c


def read_png(path: Path):
    data = path.read_bytes()
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("not a PNG: %s" % path)
    pos = 8
    w = h = bit_depth = color_type = None
    idat = b""
    while pos + 8 <= len(data):
        length = struct.unpack(">I", data[pos : pos + 4])[0]
        tag = data[pos + 4 : pos + 8]
        chunk = data[pos + 8 : pos + 8 + length]
        pos += 12 + length
        if tag == b"IHDR":
            w, h, bit_depth, color_type, comp, filt, inter = struct.unpack(">IIBBBBB", chunk)
            if bit_depth != 8 or color_type not in (2, 6) or inter != 0:
                raise ValueError("unsupported PNG %s (need 8-bit RGB/RGBA)" % path)
        elif tag == b"IDAT":
            idat += chunk
        elif tag == b"IEND":
            break
    raw = zlib.decompress(idat)
    bpp = 4 if color_type == 6 else 3
    stride = w * bpp
    rows = []
    i = 0
    prev = bytearray(stride)
    for _y in range(h):
        ft = raw[i]
        row = bytearray(raw[i + 1 : i + 1 + stride])
        i += 1 + stride
        for x in range(stride):
            left = row[x - bpp] if x >= bpp else 0
            up = prev[x]
            ul = prev[x - bpp] if x >= bpp else 0
            if ft == 0:
                pass
            elif ft == 1:
                row[x] = (row[x] + left) & 255
            elif ft == 2:
                row[x] = (row[x] + up) & 255
            elif ft == 3:
                row[x] = (row[x] + ((left + up) // 2)) & 255
            elif ft == 4:
                row[x] = (row[x] + paeth(left, up, ul)) & 255
            else:
                raise ValueError("bad PNG filter %d in %s" % (ft, path))
        prev = row
        rows.append(row)
    out = bytearray(w * h * 4)
    for y, row in enumerate(rows):
        for x in range(w):
            o = (y * w + x) * 4
            if bpp == 4:
                out[o : o + 4] = row[x * 4 : x * 4 + 4]
            else:
                out[o : o + 3] = row[x * 3 : x * 3 + 3]
                out[o + 3] = 255
    return w, h, bytes(out)


class Pix:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.data = bytearray(w * h * 4)

    def _set(self, x, y, col):
        if x < 0 or y < 0 or x >= self.w or y >= self.h:
            return
        o = (y * self.w + x) * 4
        r, g, b, a = col
        if a <= 0:
            return
        if a >= 255:
            self.data[o : o + 4] = bytes((r, g, b, 255))
            return
        dr, dg, db, da = self.data[o], self.data[o + 1], self.data[o + 2], self.data[o + 3]
        inv = 255 - a
        self.data[o] = (r * a + dr * inv) // 255
        self.data[o + 1] = (g * a + dg * inv) // 255
        self.data[o + 2] = (b * a + db * inv) // 255
        self.data[o + 3] = min(255, a + da)

    def px(self, x, y, color):
        self._set(int(x), int(y), parse_color(color))

    def fill(self, x, y, w, h, color):
        col = parse_color(color)
        x, y, w, h = int(x), int(y), int(w), int(h)
        for yy in range(y, y + h):
            for xx in range(x, x + w):
                self._set(xx, yy, col)

    def blit(self, src: "Pix", dx, dy):
        for y in range(src.h):
            for x in range(src.w):
                o = (y * src.w + x) * 4
                a = src.data[o + 3]
                if a:
                    self._set(dx + x, dy + y, (src.data[o], src.data[o + 1], src.data[o + 2], a))

    def flip_h(self) -> "Pix":
        out = Pix(self.w, self.h)
        for y in range(self.h):
            for x in range(self.w):
                o = (y * self.w + x) * 4
                out._set(self.w - 1 - x, y, (self.data[o], self.data[o + 1], self.data[o + 2], self.data[o + 3]))
        return out

    def save(self, path: Path):
        write_png(path, self.w, self.h, bytes(self.data))

    @classmethod
    def load(cls, path: Path) -> "Pix":
        w, h, rgba = read_png(path)
        p = cls(w, h)
        p.data = bytearray(rgba)
        return p


def hash01(x, y, s):
    n = (int(x) * 374761393 + int(y) * 668265263 + int(s) * 1274126177) & 0xFFFFFFFF
    n = ((n ^ (n >> 13)) * 1274126177) & 0xFFFFFFFF
    return (n % 1000) / 1000.0


def blob(g: Pix, cx, cy, rx, ry, fill_c, sh_c, hi_c, out_c):
    for y in range(-ry - 1, ry + 2):
        for x in range(-rx - 1, rx + 2):
            dx = x / (rx + 0.2)
            dy = y / (ry + 0.2)
            if dx * dx + dy * dy <= 1.05:
                edge = dx * dx + dy * dy > 0.78
                hi = dx < -0.15 and dy < -0.1 and not edge
                sh = dx > 0.25 or dy > 0.35
                g.px(cx + x, cy + y, out_c if edge else hi_c if hi else sh_c if sh else fill_c)


C = {}


def load_palette():
    global C
    C = json.loads(PALETTE_PATH.read_text(encoding="utf-8"))
    return C


# --- tiles (16x16, slight 3/4 south lip) ------------------------------------

def gen_grass(v):
    g = Pix(16, 16)
    g.fill(0, 0, 16, 16, C["grassMid"])
    for i in range(22):
        r = hash01(v, i, 11)
        x = int(hash01(v, i, 3) * 16)
        y = int(hash01(v, i, 7) * 14)
        if r < 0.38:
            g.px(x, y, C["grassHi"])
        elif r < 0.62:
            g.px(x, y, C["grassSh"])
        elif r < 0.72:
            g.px(x, y, C["grassDp"])
    blades = [(2, 4), (7, 2), (12, 6), (4, 10), (10, 12), (14, 3), (1, 12), (8, 8)]
    for i, (bx, by) in enumerate(blades):
        if hash01(v, i, 21) < 0.55 + v * 0.08:
            x = (bx + v) & 15
            y = by
            g.px(x, y, C["grassHi"])
            g.px(x, y + 1, C["grassSh"])

    def tuft(x, y):
        g.px(x, y, C["grassHi"])
        g.px(x + 1, y, C["grassMid"])
        g.px(x, y + 1, C["grassSh"])
        g.px(x - 1, y + 1, C["grassSh"])
        g.px(x + 1, y + 1, C["grassDp"])

    if v == 0:
        tuft(3, 3)
        tuft(11, 9)
    elif v == 1:
        tuft(6, 5)
        tuft(12, 11)
        g.px(5, 6, C["flower"])
        g.px(13, 10, C["blossom"])
    elif v == 2:
        tuft(2, 10)
        tuft(9, 2)
    else:
        tuft(8, 8)
        tuft(14, 4)
        g.px(9, 4, C["flower"])
    # 3/4 lip: north catch-light, south shade so the grid has depth
    for x in range(16):
        if hash01(v, x, 90) < 0.35:
            g.px(x, 0, C["grassHi"])
        g.px(x, 14, C["grassSh"] if (x + v) % 3 else C["grassMid"])
        g.px(x, 15, C["grassDp"] if (x + v) % 2 else C["grassSh"])
    return g


def gen_dirt():
    g = Pix(16, 16)
    g.fill(0, 0, 16, 16, C["dirtMid"])
    for i in range(16):
        r = hash01(9, i, 4)
        x = int(hash01(9, i, 1) * 16)
        y = int(hash01(9, i, 2) * 14)
        if r < 0.4:
            g.px(x, y, C["dirtHi"])
        elif r < 0.7:
            g.px(x, y, C["dirtSh"])
    for x in range(16):
        if x % 3 == 0:
            g.px(x, 0, C["dirtHi"])
        g.px(x, 14, C["dirtSh"])
        g.px(x, 15, C["tillOut"] if x % 2 else C["dirtSh"])
    return g


def gen_till():
    g = Pix(16, 16)
    g.fill(0, 0, 16, 16, C["till"])
    g.fill(0, 0, 16, 1, C["tillOut"])
    g.fill(0, 0, 1, 16, C["tillOut"])
    g.fill(15, 0, 1, 16, C["tillOut"])
    # receding 3/4 furrows: far ridge thin, near ridge has a front face
    rows = [(3, 1), (7, 1), (11, 2)]
    for y, thick in rows:
        g.fill(2, y, 12, 1, C["tillSh"])
        g.fill(2, y + 1, 12, thick, C["tillOut"])
        for x in range(3, 14, 3):
            g.px(x, y - 1, C["dirtSh"])
    g.px(4, 5, C["dirtHi"])
    g.px(11, 9, C["dirtHi"])
    g.fill(0, 15, 16, 1, C["tillOut"])
    return g


def gen_water():
    g = Pix(16, 16)
    g.fill(0, 0, 16, 16, C["water"])
    for y in range(16):
        for x in range(16):
            r = hash01(x, y, 3)
            if r < 0.18:
                g.px(x, y, C["waterDp"])
            elif r < 0.24:
                g.px(x, y, C["waterFm"])
    # south lip
    g.fill(0, 14, 16, 1, C["waterDp"])
    g.fill(0, 15, 16, 1, C["woodOut"])
    g.px(4, 5, C["waterFm"])
    g.px(11, 9, C["waterFm"])
    return g


# --- props -----------------------------------------------------------------

def gen_pond():
    g = Pix(36, 32)
    for y in range(32):
        for x in range(36):
            dx = (x - 18) / 15.2
            dy = (y - 16) / 12.4
            d = dx * dx + dy * dy + 0.12 * math.sin(x * 0.7) * math.cos(y * 0.5)
            if d < 1.18:
                if d > 0.92:
                    # south bank thicker (3/4 near edge)
                    g.px(x, y, C["dirtSh"] if y > 18 else C["dirtMid"])
                elif d > 0.78:
                    g.px(x, y, C["dirtMid"] if (x + y) % 3 else C["grassSh"])
                elif d > 0.55:
                    g.px(x, y, C["water"])
                else:
                    g.px(x, y, C["waterDp"])
    g.px(12, 13, C["waterFm"])
    g.px(13, 13, C["waterFm"])
    g.px(21, 18, C["waterFm"])
    g.px(16, 20, C["waterFm"])
    g.px(24, 12, C["water"])
    g.fill(14, 16, 4, 2, C["leaf"])
    g.px(13, 16, C["grassDp"])
    g.px(18, 16, C["grassDp"])
    g.px(15, 15, C["grassHi"])
    return g


def gen_tree():
    g = Pix(48, 64)
    g.fill(14, 58, 20, 3, C["shadow"])
    g.fill(16, 57, 16, 1, C["shadowSoft"])
    # trunk: 3/4 post (top sliver + front)
    g.fill(21, 40, 6, 3, C["woodHi"])  # top plane
    g.fill(21, 43, 6, 16, C["woodMid"])
    g.fill(21, 43, 2, 16, C["woodHi"])
    g.fill(25, 43, 2, 16, C["woodSh"])
    g.fill(20, 40, 1, 19, C["woodOut"])
    g.fill(27, 40, 1, 19, C["woodOut"])
    g.px(23, 48, C["woodOut"])
    g.px(24, 54, C["woodSh"])
    # canopy clusters: each lump has a darker underside
    blob(g, 24, 16, 13, 10, C["grassMid"], C["grassSh"], C["grassHi"], C["grassDp"])
    blob(g, 13, 24, 10, 8, C["grassMid"], C["grassSh"], C["grassHi"], C["grassDp"])
    blob(g, 35, 23, 10, 8, C["grassMid"], C["grassSh"], C["grassHi"], C["grassDp"])
    blob(g, 24, 32, 11, 7, C["grassSh"], C["grassDp"], C["grassMid"], C["grassDp"])
    g.px(18, 14, C["grassHi"])
    g.px(19, 14, C["grassHi"])
    g.px(30, 18, C["grassHi"])
    g.px(10, 22, C["grassDp"])
    g.px(38, 26, C["grassDp"])
    return g


def _window(g, wx, wy):
    g.fill(wx - 1, wy - 1, 12, 12, C["woodOut"])
    g.fill(wx, wy, 10, 10, C["glass"])
    g.fill(wx, wy, 10, 1, C["woodHi"])
    g.fill(wx + 4, wy, 2, 10, C["woodOut"])
    g.fill(wx, wy + 4, 10, 2, C["woodOut"])
    g.px(wx + 1, wy + 1, C["parch"])
    g.fill(wx - 1, wy + 10, 12, 3, C["woodSh"])
    g.fill(wx - 1, wy + 10, 12, 1, C["woodHi"])
    g.px(wx + 1, wy + 9, C["leaf"])
    g.px(wx + 3, wy + 9, C["blossom"])
    g.px(wx + 5, wy + 9, C["leaf"])
    g.px(wx + 7, wy + 9, C["flower"])
    g.px(wx + 8, wy + 9, C["leaf"])


def gen_house():
    """3/4 cottage: visible roof plane, taller front wall, right-side sliver."""
    g = Pix(80, 80)
    g.fill(8, 76, 66, 4, C["shadow"])

    # chimney sits on the roof plane (top cap + front)
    g.fill(13, 2, 11, 3, C["stoneHi"])
    g.fill(14, 1, 9, 2, C["stone"])
    g.fill(15, 0, 7, 2, C["stoneSh"])
    g.fill(14, 5, 9, 18, C["stone"])
    g.fill(14, 5, 2, 18, C["stoneHi"])
    g.fill(21, 5, 2, 18, C["stoneSh"])
    g.fill(13, 5, 1, 18, C["woodOut"])
    g.fill(23, 5, 1, 18, C["woodOut"])
    g.fill(12, 10, 13, 2, C["stoneSh"])
    g.px(17, 3, C["stoneHi"])
    g.px(19, 12, C["stoneSh"])
    g.px(16, 16, C["stoneSh"])

    # roof top plane (you look down on the ridge)
    g.fill(30, 5, 20, 3, C["roofHi"])
    g.fill(34, 4, 12, 2, C["roof"])
    g.fill(36, 3, 8, 2, C["roofHi"])
    g.fill(28, 7, 24, 2, C["roof"])

    # front roof slope — shingles recede toward the ridge
    for y in range(8, 38):
        t = (y - 8) / 29.0
        half = 12 + t * 26
        x0 = int(round(40 - half))
        x1 = int(round(40 + half))
        color = C["roofSh"] if y % 5 == 0 else C["roof"]
        g.fill(x0, y, x1 - x0, 1, color)
        if (y + 2) % 5 == 0:
            for x in range(x0 + 2, x1 - 1, 4):
                g.px(x, y, C["roofHi"])
        g.px(x0, y, C["woodOut"])
        g.px(x1 - 1, y, C["woodOut"])
        # right roof side plane (3/4)
        if y >= 12:
            g.px(x1, y, C["roofSh"])
            if y >= 20:
                g.px(x1 + 1, y, C["roofSh"])

    # eaves
    g.fill(3, 37, 75, 3, C["woodSh"])
    g.fill(3, 37, 75, 1, C["woodHi"])
    g.fill(3, 39, 75, 1, C["woodOut"])

    # taller front wall
    g.fill(8, 40, 64, 34, C["woodMid"])
    for y in range(43, 72, 5):
        g.fill(8, y, 64, 1, C["woodSh"])
        g.fill(8, y + 1, 64, 1, C["woodHi"])
    g.fill(8, 40, 1, 34, C["woodOut"])
    g.fill(71, 40, 1, 34, C["woodOut"])
    g.fill(8, 40, 64, 1, C["woodHi"])  # top plate of the wall

    # right side wall sliver
    g.fill(72, 40, 6, 34, C["woodSh"])
    g.fill(72, 40, 1, 34, C["woodMid"])
    g.fill(77, 40, 1, 34, C["woodOut"])
    g.fill(72, 40, 6, 1, C["woodMid"])

    # foundation sill
    g.fill(6, 74, 72, 4, C["stone"])
    g.fill(6, 74, 72, 1, C["stoneHi"])
    g.fill(6, 77, 72, 1, C["stoneSh"])
    g.px(12, 75, C["stoneSh"])
    g.px(28, 76, C["stoneSh"])
    g.px(50, 75, C["stoneHi"])
    g.px(64, 76, C["stoneSh"])

    _window(g, 14, 46)
    _window(g, 56, 46)

    # Dutch door — taller to match the wall
    g.fill(33, 50, 14, 24, C["woodOut"])
    g.fill(34, 51, 12, 10, C["door"])
    g.fill(34, 62, 12, 11, C["woodMid"])
    g.fill(34, 61, 12, 1, C["woodOut"])
    g.fill(34, 51, 12, 1, C["woodHi"])
    g.px(40, 54, C["glass"])
    g.px(39, 55, C["glass"])
    g.px(40, 55, C["parch"])
    g.px(41, 55, C["glass"])
    g.px(40, 56, C["glass"])
    g.px(44, 57, C["woodHi"])
    g.px(44, 66, C["woodHi"])

    # two-step stoop
    g.fill(31, 76, 18, 3, C["stone"])
    g.fill(33, 78, 14, 2, C["stoneHi"])
    return g


def gen_well():
    g = Pix(16, 32)
    g.fill(2, 29, 12, 3, C["shadow"])
    # 3/4 roof: top plane + front slope
    g.fill(3, 0, 10, 2, C["roofHi"])
    g.fill(2, 1, 12, 1, C["roof"])
    for y in range(2, 8):
        inset = (y - 2) // 2
        g.fill(1 + inset, y, 14 - inset * 2, 1, C["roof"] if y % 2 else C["roofSh"])
        g.px(1 + inset, y, C["woodOut"])
        g.px(14 - inset, y, C["woodOut"])
    # posts
    g.fill(3, 8, 2, 10, C["woodMid"])
    g.fill(11, 8, 2, 10, C["woodMid"])
    g.fill(3, 8, 1, 10, C["woodHi"])
    g.fill(12, 8, 1, 10, C["woodSh"])
    g.fill(3, 8, 10, 2, C["woodSh"])
    g.fill(3, 8, 10, 1, C["woodHi"])
    # bucket
    g.fill(7, 11, 3, 4, C["woodMid"])
    g.fill(7, 11, 3, 1, C["woodHi"])
    # stone cylinder: elliptical rim (top) + front face
    g.fill(2, 20, 12, 9, C["stone"])
    g.fill(2, 20, 2, 9, C["stoneHi"])
    g.fill(12, 20, 2, 9, C["stoneSh"])
    g.fill(2, 28, 12, 1, C["woodOut"])
    # rim ellipse
    for x, y, col in (
        (4, 18, C["stoneHi"]), (5, 17, C["stoneHi"]), (6, 17, C["stoneHi"]),
        (7, 17, C["stone"]), (8, 17, C["stone"]), (9, 17, C["stoneHi"]),
        (10, 17, C["stoneHi"]), (11, 18, C["stone"]),
        (3, 19, C["stone"]), (12, 19, C["stoneSh"]),
        (3, 20, C["woodOut"]), (12, 20, C["woodOut"]),
        (4, 20, C["woodOut"]), (11, 20, C["woodOut"]),
    ):
        g.px(x, y, col)
    g.fill(5, 19, 6, 4, C["waterDp"])
    g.px(6, 20, C["water"])
    g.px(9, 21, C["waterFm"])
    return g


def gen_mailbox():
    g = Pix(16, 24)
    g.fill(4, 21, 8, 2, C["shadow"])
    # post with cap
    g.fill(7, 12, 3, 2, C["woodHi"])
    g.fill(7, 14, 3, 8, C["woodMid"])
    g.fill(7, 14, 1, 8, C["woodHi"])
    g.fill(9, 14, 1, 8, C["woodSh"])
    # 3/4 box: lid + front + side
    g.fill(3, 3, 10, 3, C["woodHi"])  # lid top
    g.fill(2, 5, 11, 1, C["woodMid"])
    g.fill(2, 6, 11, 6, C["woodMid"])
    g.fill(2, 6, 1, 6, C["woodOut"])
    g.fill(12, 6, 1, 6, C["woodOut"])
    g.fill(2, 11, 11, 1, C["woodOut"])
    g.fill(13, 4, 2, 7, C["woodSh"])  # right side
    g.fill(4, 8, 6, 1, C["woodOut"])
    g.fill(4, 7, 6, 1, C["woodSh"])
    g.fill(13, 5, 2, 4, C["flag"])
    g.px(14, 6, C["flagHi"])
    return g


def gen_mailbox_up():
    """Same 3/4 mailbox with a raised teal flag so unread mail is obvious."""
    g = Pix(16, 32)
    # body is the regular mailbox, shifted down 8px for flag headroom
    g.fill(4, 29, 8, 2, C["shadow"])
    g.fill(7, 20, 3, 2, C["woodHi"])
    g.fill(7, 22, 3, 8, C["woodMid"])
    g.fill(7, 22, 1, 8, C["woodHi"])
    g.fill(9, 22, 1, 8, C["woodSh"])
    g.fill(3, 11, 10, 3, C["woodHi"])
    g.fill(2, 13, 11, 1, C["woodMid"])
    g.fill(2, 14, 11, 6, C["woodMid"])
    g.fill(2, 14, 1, 6, C["woodOut"])
    g.fill(12, 14, 1, 6, C["woodOut"])
    g.fill(2, 19, 11, 1, C["woodOut"])
    g.fill(13, 12, 2, 7, C["woodSh"])
    g.fill(4, 16, 6, 1, C["woodOut"])
    g.fill(4, 15, 6, 1, C["woodSh"])
    # pole up from the lid
    g.fill(13, 2, 1, 10, C["woodMid"])
    g.fill(14, 2, 1, 10, C["woodOut"])
    g.px(13, 1, C["woodHi"])
    g.px(14, 1, C["woodMid"])
    # chunky pennant, original teal (not a copy of anyone's red flag)
    g.fill(5, 1, 8, 2, C["flagHi"])
    g.fill(4, 3, 9, 3, C["flag"])
    g.fill(5, 6, 8, 1, C["flag"])
    g.fill(7, 7, 6, 1, C["flag"])
    g.px(6, 2, C["parch"])
    g.px(8, 4, C["flagHi"])
    g.px(10, 4, C["flagHi"])
    return g


def gen_letter():
    """Sealed parchment envelope that bobs above unread mail."""
    g = Pix(16, 16)
    g.fill(3, 13, 10, 2, C["shadow"])
    # 3/4 envelope: lid plane + front
    g.fill(3, 3, 10, 1, C["woodOut"])
    g.fill(2, 4, 12, 1, C["woodHi"])
    g.fill(1, 5, 14, 1, C["parch"])
    g.fill(1, 6, 14, 6, C["parch"])
    g.fill(1, 6, 1, 6, C["woodHi"])
    g.fill(14, 6, 1, 6, C["woodOut"])
    g.fill(1, 12, 14, 1, C["woodOut"])
    # flap V
    g.px(2, 6, C["woodSh"])
    g.px(3, 7, C["woodSh"])
    g.px(4, 8, C["woodMid"])
    g.px(5, 9, C["woodMid"])
    g.px(13, 6, C["woodSh"])
    g.px(12, 7, C["woodSh"])
    g.px(11, 8, C["woodMid"])
    g.px(10, 9, C["woodMid"])
    g.fill(6, 9, 4, 1, C["woodMid"])
    # wax seal
    g.fill(7, 8, 2, 2, C["roof"])
    g.px(7, 8, C["roofHi"])
    return g


def gen_crate():
    """Lid (top plane) + front face + right side."""
    g = Pix(16, 16)
    g.fill(2, 14, 12, 2, C["shadow"])
    # lid parallelogram
    g.fill(4, 1, 8, 1, C["woodOut"])
    g.fill(3, 2, 10, 1, C["woodHi"])
    g.fill(2, 3, 11, 1, C["woodHi"])
    g.fill(1, 4, 12, 1, C["woodMid"])
    g.fill(1, 5, 12, 1, C["woodOut"])
    # front
    g.fill(1, 6, 11, 8, C["woodMid"])
    g.fill(1, 6, 1, 8, C["woodHi"])
    g.fill(11, 6, 1, 8, C["woodOut"])
    g.fill(1, 9, 11, 1, C["woodSh"])
    g.fill(5, 6, 2, 8, C["woodSh"])
    g.fill(1, 13, 11, 1, C["woodOut"])
    # right side
    g.fill(12, 3, 3, 3, C["woodSh"])
    g.fill(12, 6, 3, 8, C["woodSh"])
    g.fill(14, 3, 1, 11, C["woodOut"])
    g.px(3, 7, C["woodHi"])
    g.px(9, 11, C["woodOut"])
    return g


def gen_rock(v):
    g = Pix(16, 16)
    g.fill(4, 13, 8, 2, C["shadow"])
    if v == 0:
        # top plane + front face
        blob(g, 8, 9, 6, 3, C["stoneHi"], C["stone"], C["stoneHi"], C["stoneSh"])
        blob(g, 8, 12, 6, 3, C["stone"], C["stoneSh"], C["stone"], C["stoneSh"])
        g.px(6, 8, C["stoneHi"])
        g.px(10, 13, C["stoneSh"])
    else:
        blob(g, 8, 10, 5, 2, C["stoneHi"], C["stone"], C["stoneHi"], C["stoneSh"])
        blob(g, 8, 12, 5, 2, C["stone"], C["stoneSh"], C["stone"], C["stoneSh"])
        g.px(7, 10, C["stoneHi"])
        g.px(10, 13, C["stoneSh"])
    return g


def gen_weed(v):
    g = Pix(16, 16)
    if v == 0:
        g.px(7, 14, C["grassDp"])
        g.px(8, 13, C["grassSh"])
        g.px(8, 12, C["grassMid"])
        g.px(7, 11, C["grassHi"])
        g.px(9, 11, C["grassHi"])
        g.px(6, 12, C["grassMid"])
        g.px(10, 12, C["grassMid"])
        g.px(8, 9, C["grassSh"])
        g.px(8, 8, C["flower"])
    else:
        g.px(6, 14, C["grassDp"])
        g.px(7, 13, C["grassSh"])
        g.px(5, 12, C["grassMid"])
        g.px(8, 12, C["grassMid"])
        g.px(6, 11, C["grassHi"])
        g.px(9, 11, C["grassHi"])
        g.px(7, 10, C["leaf"])
        g.px(4, 13, C["grassSh"])
        g.px(10, 13, C["grassSh"])
    return g


def _post(g, px0):
    # cap (top plane) + front
    g.fill(px0, 2, 4, 2, C["woodHi"])
    g.fill(px0 - 1, 2, 6, 1, C["woodOut"])
    g.fill(px0, 4, 3, 11, C["woodMid"])
    g.fill(px0, 4, 1, 11, C["woodHi"])
    g.fill(px0 + 2, 4, 1, 11, C["woodSh"])
    g.fill(px0, 15, 3, 1, C["woodOut"])


def gen_fence_h():
    g = Pix(16, 16)
    _post(g, 1)
    g.fill(4, 6, 12, 2, C["woodMid"])
    g.fill(4, 6, 12, 1, C["woodHi"])
    g.fill(4, 10, 12, 2, C["woodSh"])
    g.fill(4, 10, 12, 1, C["woodMid"])
    return g


def gen_fence_l():
    g = Pix(16, 16)
    _post(g, 2)
    g.fill(5, 6, 11, 2, C["woodMid"])
    g.fill(5, 6, 11, 1, C["woodHi"])
    g.fill(5, 10, 11, 2, C["woodSh"])
    return g


def gen_fence_r():
    g = Pix(16, 16)
    _post(g, 10)
    g.fill(0, 6, 10, 2, C["woodMid"])
    g.fill(0, 6, 10, 1, C["woodHi"])
    g.fill(0, 10, 10, 2, C["woodSh"])
    return g


def gen_seed():
    g = Pix(16, 16)
    # packet: lid + front
    g.fill(4, 2, 8, 3, C["woodHi"])
    g.fill(3, 4, 10, 1, C["woodOut"])
    g.fill(3, 5, 10, 9, C["woodMid"])
    g.fill(3, 5, 1, 9, C["woodHi"])
    g.fill(12, 5, 1, 9, C["woodOut"])
    g.fill(3, 13, 10, 1, C["woodOut"])
    g.px(6, 9, C["dirtHi"])
    g.px(8, 10, C["dirtSh"])
    g.px(10, 9, C["dirtHi"])
    g.px(8, 7, C["leaf"])
    g.px(7, 6, C["grassHi"])
    g.px(9, 6, C["grassHi"])
    return g


def gen_sprout():
    g = Pix(16, 16)
    g.fill(7, 10, 2, 5, C["grassSh"])
    g.px(7, 10, C["leaf"])
    g.px(8, 11, C["grassMid"])
    g.fill(3, 7, 4, 3, C["leaf"])
    g.fill(4, 6, 3, 2, C["grassHi"])
    g.px(3, 8, C["grassSh"])
    g.px(6, 7, C["grassMid"])
    g.fill(9, 5, 4, 4, C["leaf"])
    g.fill(10, 4, 3, 2, C["grassHi"])
    g.px(12, 7, C["grassSh"])
    g.px(9, 6, C["grassMid"])
    return g


def gen_crop_young():
    """Taller leafy plant: more leaves than the sprout, no veggie yet."""
    g = Pix(16, 16)
    g.fill(7, 7, 2, 8, C["grassSh"])
    g.px(7, 7, C["leaf"])
    g.px(8, 8, C["grassMid"])
    # left leaf
    g.fill(1, 6, 5, 3, C["leaf"])
    g.fill(2, 5, 4, 2, C["grassHi"])
    g.px(1, 7, C["grassSh"])
    g.px(5, 6, C["grassMid"])
    # right leaf
    g.fill(9, 4, 5, 4, C["leaf"])
    g.fill(10, 3, 4, 2, C["grassHi"])
    g.px(13, 6, C["grassSh"])
    g.px(9, 5, C["grassMid"])
    # top leaf
    g.fill(5, 2, 4, 3, C["leaf"])
    g.fill(6, 1, 3, 2, C["grassHi"])
    g.px(5, 3, C["grassSh"])
    return g


def gen_crop_ready():
    """3/4 ready carrot: leafy crown, stem, orange shoulder in the soil."""
    g = Pix(16, 16)
    # leafy crown, top plane then front
    g.fill(5, 0, 6, 2, C["grassHi"])
    g.fill(4, 2, 8, 3, C["leaf"])
    g.fill(5, 1, 6, 2, C["grassMid"])
    g.px(4, 3, C["grassSh"])
    g.px(11, 3, C["grassSh"])
    g.px(3, 2, C["leaf"])
    g.px(2, 3, C["grassHi"])
    g.px(12, 2, C["leaf"])
    g.px(13, 3, C["grassHi"])
    g.px(7, 2, C["grassHi"])
    # stem into the carrot
    g.fill(7, 5, 2, 3, C["grassSh"])
    g.px(7, 5, C["leaf"])
    g.px(8, 6, C["grassMid"])
    # carrot shoulder (top + front), sitting in soil
    g.fill(5, 8, 6, 2, C["copperHi"])
    g.fill(4, 10, 8, 4, C["copperMid"])
    g.fill(4, 10, 2, 4, C["dirtHi"])
    g.fill(10, 10, 2, 4, C["copperSh"])
    g.fill(5, 13, 6, 1, C["copperSh"])
    g.px(6, 9, C["copperHi"])
    g.px(8, 11, C["dirtHi"])
    g.px(3, 14, C["dirtSh"])
    g.px(4, 14, C["till"])
    g.px(11, 14, C["till"])
    g.px(12, 14, C["dirtSh"])
    return g


def gen_veggie():
    """Harvested carrot: greens + tapered 3/4 orange root."""
    g = Pix(16, 16)
    g.fill(6, 1, 2, 4, C["leaf"])
    g.px(5, 2, C["grassHi"])
    g.px(8, 2, C["grassHi"])
    g.px(4, 3, C["leaf"])
    g.px(9, 3, C["leaf"])
    g.px(6, 1, C["grassHi"])
    g.px(7, 2, C["grassMid"])
    g.fill(5, 5, 6, 2, C["copperHi"])
    g.fill(4, 7, 8, 3, C["copperMid"])
    g.fill(5, 10, 6, 2, C["copperMid"])
    g.fill(6, 12, 4, 2, C["copperSh"])
    g.fill(7, 14, 2, 1, C["copperSh"])
    g.fill(4, 7, 1, 3, C["dirtHi"])
    g.fill(11, 7, 1, 3, C["copperSh"])
    g.px(6, 6, C["copperHi"])
    g.px(8, 8, C["dirtHi"])
    return g



def gen_stump():
    """Cut trunk: top rings + front face + little roots."""
    g = Pix(16, 16)
    g.fill(3, 14, 10, 2, C["shadow"])
    # cut top plane (rings)
    g.fill(5, 5, 6, 1, C["woodHi"])
    g.fill(4, 6, 8, 3, C["woodHi"])
    g.fill(5, 7, 6, 1, C["woodMid"])
    g.px(7, 7, C["woodOut"])
    g.px(8, 6, C["woodSh"])
    g.px(6, 6, C["dirtHi"])
    # front face
    g.fill(4, 9, 8, 5, C["woodMid"])
    g.fill(4, 9, 2, 5, C["woodHi"])
    g.fill(10, 9, 2, 5, C["woodSh"])
    g.fill(4, 13, 8, 1, C["woodOut"])
    g.fill(3, 9, 1, 5, C["woodOut"])
    g.fill(12, 9, 1, 5, C["woodOut"])
    # bark nick
    g.px(6, 11, C["woodOut"])
    g.px(9, 12, C["woodSh"])
    # roots
    g.fill(2, 12, 2, 2, C["woodSh"])
    g.px(2, 13, C["woodOut"])
    g.fill(12, 12, 2, 2, C["woodSh"])
    g.px(13, 13, C["woodOut"])
    return g


def gen_wood():
    """3/4 log for the hotbar and pickup."""
    g = Pix(16, 16)
    g.fill(3, 13, 10, 2, C["shadow"])
    # top of the cylinder
    g.fill(4, 4, 8, 1, C["woodOut"])
    g.fill(3, 5, 10, 1, C["woodHi"])
    g.fill(2, 6, 11, 2, C["woodHi"])
    g.fill(3, 7, 9, 1, C["woodMid"])
    # front
    g.fill(2, 8, 11, 5, C["woodMid"])
    g.fill(2, 8, 2, 5, C["woodHi"])
    g.fill(11, 8, 2, 5, C["woodSh"])
    g.fill(2, 12, 11, 1, C["woodOut"])
    # right end-grain
    g.fill(12, 6, 3, 6, C["woodSh"])
    g.fill(13, 7, 1, 4, C["woodOut"])
    g.px(13, 8, C["dirtHi"])
    g.px(4, 9, C["woodOut"])
    g.px(8, 11, C["woodSh"])
    return g


def gen_stone_item():
    """Small 3/4 stone chunk for the hotbar and pickup."""
    g = Pix(16, 16)
    g.fill(4, 13, 8, 2, C["shadow"])
    blob(g, 7, 8, 5, 3, C["stoneHi"], C["stone"], C["stoneHi"], C["stoneSh"])
    blob(g, 8, 11, 5, 3, C["stone"], C["stoneSh"], C["stone"], C["stoneSh"])
    blob(g, 11, 10, 3, 2, C["stone"], C["stoneSh"], C["stoneHi"], C["stoneSh"])
    g.px(5, 8, C["stoneHi"])
    g.px(10, 12, C["stoneSh"])
    return g


def gen_path():
    """Walkable cobble path, 3/4 south lip."""
    g = Pix(16, 16)
    g.fill(0, 0, 16, 16, C["stone"])
    cobbles = [
        (1, 1, 6, 5), (8, 1, 7, 4),
        (1, 6, 5, 4), (7, 6, 8, 5),
        (1, 11, 7, 3), (9, 12, 6, 2),
    ]
    for i, (x, y, w, h) in enumerate(cobbles):
        hi = C["stoneHi"] if i % 2 == 0 else C["stone"]
        sh = C["stoneSh"]
        g.fill(x, y, w, h, hi)
        g.fill(x, y + h - 1, w, 1, sh)
        g.fill(x + w - 1, y, 1, h, sh)
        if i % 3 == 0:
            g.px(x + 1, y + 1, C["stoneHi"])
    for x in range(16):
        if x % 4 == 0:
            g.px(x, 0, C["stoneHi"])
        g.px(x, 14, C["stoneSh"])
        g.px(x, 15, C["woodOut"] if x % 2 else C["stoneSh"])
    return g


# --- actors ----------------------------------------------------------------

def _person_colors(kind):
    if kind == "npc":
        return {
            "hair": C["npcHair"], "hairHi": C["npcHairHi"],
            "skin": C["skin"], "skinSh": C["skinSh"],
            "eye": C["npcEye"], "eyeHi": C["npcEyeHi"], "lip": C["npcLip"],
            "shirt": C["npcShirt"], "shirtHi": C["npcShirtHi"], "shirtSh": C["npcShirtSh"],
            "pants": C["npcPants"], "pantsSh": C["npcPantsSh"], "shoe": C["npcShoe"],
            "out": C["woodOut"],
            "hat": C["npcHat"], "hatHi": C["npcHatHi"], "hatSh": C["npcHatSh"],
            "hatBand": C["npcHatBand"], "apron": C["npcApron"],
        }
    return {
        "hair": C["playerHair"], "hairHi": C["playerHairHi"],
        "skin": C["skin"], "skinSh": C["skinSh"],
        "eye": C["playerEye"], "eyeHi": C["playerEyeHi"], "lip": C["playerLip"],
        "shirt": C["playerShirt"], "shirtHi": C["playerShirtHi"], "shirtSh": C["playerShirtSh"],
        "pants": C["playerPants"], "pantsSh": C["playerPantsSh"], "shoe": C["playerShoe"],
        "out": C["woodOut"],
    }


def gen_person(kind, face, frame):
    """16x32 chibi, 3/4 body (chest/head, not a top-down pancake)."""
    g = Pix(16, 32)
    p = _person_colors(kind)
    fr = 1 if frame else 0

    # legs / shoes
    if face in ("down", "up"):
        g.fill(4, 23 + fr, 3, 5, p["pants"])
        g.fill(4, 28 + fr, 3, 2, p["shoe"])
        g.fill(9, 23 - fr, 3, 5, p["pantsSh"] if face == "up" else p["pants"])
        g.fill(9, 28 - fr, 3, 2, p["shoe"])
    else:
        g.fill(6, 23 + fr, 3, 5, p["pantsSh"])
        g.fill(6, 28 + fr, 3, 2, p["shoe"])
        g.fill(8, 23 - fr, 3, 5, p["pants"])
        g.fill(8, 28 - fr, 3, 2, p["shoe"])

    # torso: top plate + front (3/4 box)
    if face == "down":
        g.fill(4, 13, 8, 10, p["shirt"])
        g.fill(4, 13, 8, 1, p["shirtHi"])
        g.fill(4, 13, 1, 10, p["shirtHi"])
        g.fill(11, 13, 1, 10, p["shirtSh"])
        g.fill(2, 14, 2, 6, p["shirt"])
        g.fill(12, 14, 2, 6, p["shirt"])
        g.fill(2, 19, 2, 2, p["skin"])
        g.fill(12, 19, 2, 2, p["skin"])
        if "apron" in p:
            g.fill(5, 16, 6, 6, p["apron"])
    elif face == "up":
        g.fill(4, 13, 8, 10, p["shirtSh"])
        g.fill(4, 13, 8, 1, p["shirt"])
        g.fill(2, 14, 2, 6, p["shirtSh"])
        g.fill(12, 14, 2, 6, p["shirtSh"])
        g.fill(2, 19, 2, 2, p["skin"])
        g.fill(12, 19, 2, 2, p["skin"])
    else:
        g.fill(5, 13, 6, 10, p["shirt"])
        g.fill(5, 13, 6, 1, p["shirtHi"])
        g.fill(10, 13, 1, 10, p["shirtSh"])
        g.fill(10, 14 + fr, 2, 6, p["shirt"])
        g.fill(10, 20 + fr, 2, 2, p["skin"])
        if "apron" in p:
            g.fill(6, 16, 4, 6, p["apron"])

    # head
    if face == "down":
        g.fill(3, 3, 10, 8, p["hair"])
        g.fill(4, 2, 8, 2, p["hair"])
        g.fill(4, 5, 8, 6, p["skin"])
        g.fill(5, 4, 6, 1, p["skin"])
        g.fill(4, 10, 8, 1, p["skinSh"])
        g.fill(4, 3, 8, 2, p["hair"])
        g.fill(4, 3, 2, 3, p["hair"])
        g.fill(10, 3, 2, 3, p["hair"])
        g.fill(5, 2, 6, 1, p["hairHi"])
        g.px(5, 7, p["eye"])
        g.px(6, 7, p["eyeHi"])
        g.px(9, 7, p["eye"])
        g.px(10, 7, p["eyeHi"])
        g.px(7, 9, p["skinSh"])
        g.px(8, 10, p["lip"])
        g.px(3, 7, p["skin"])
        g.px(12, 7, p["skin"])
        g.fill(6, 11, 4, 2, p["skin"])
        g.px(3, 2, p["out"])
        g.px(12, 2, p["out"])
    elif face == "up":
        g.fill(3, 3, 10, 8, p["hair"])
        g.fill(4, 2, 8, 2, p["hairHi"])
        g.fill(3, 4, 10, 7, p["hair"])
        g.fill(6, 11, 4, 2, p["hair"])
        g.px(3, 7, p["skin"])
        g.px(12, 7, p["skin"])
    else:
        g.fill(3, 3, 9, 8, p["hair"])
        g.fill(4, 2, 7, 2, p["hair"])
        g.fill(5, 5, 6, 6, p["skin"])
        g.fill(5, 4, 5, 1, p["skin"])
        g.fill(3, 3, 3, 8, p["hair"])
        g.fill(4, 2, 2, 2, p["hairHi"])
        g.px(8, 7, p["eye"])
        g.px(9, 7, p["eyeHi"])
        g.px(10, 8, p["skinSh"])
        g.px(9, 10, p["lip"])
        g.fill(7, 11, 3, 2, p["skin"])

    if "hat" in p:
        if face == "up":
            g.fill(5, 0, 6, 4, p["hat"])
            g.fill(5, 0, 6, 1, p["hatHi"])
            g.fill(2, 3, 12, 2, p["hat"])
            g.fill(1, 4, 14, 1, p["hatSh"])
        elif face == "down":
            g.fill(5, 0, 6, 3, p["hat"])
            g.fill(5, 0, 6, 1, p["hatHi"])
            g.fill(5, 2, 6, 1, p["hatBand"])
            g.fill(2, 3, 12, 2, p["hat"])
            g.fill(1, 4, 14, 1, p["hatSh"])
        else:
            g.fill(4, 0, 7, 3, p["hat"])
            g.fill(4, 0, 7, 1, p["hatHi"])
            g.fill(4, 2, 7, 1, p["hatBand"])
            g.fill(2, 3, 11, 2, p["hat"])
            g.fill(1, 4, 13, 1, p["hatSh"])
    return g


def gen_chicken(fr):
    g = Pix(16, 16)
    y = 0 if fr else 1
    blob(g, 7, 8 + y, 5, 4, C["chick"], C["chickSh"], C["chickHi"], C["chickOut"])
    blob(g, 12, 6 + y, 3, 3, C["chick"], C["chickSh"], C["chickHi"], C["chickOut"])
    g.px(15, 6 + y, C["chickBeak"])
    g.px(15, 7 + y, C["chickBeakSh"])
    g.px(12, 2 + y, C["chickComb"])
    g.px(13, 2 + y, C["chickComb"])
    g.px(12, 1 + y, C["chickCombHi"])
    g.px(13, 5 + y, C["chickEye"])
    g.px(2, 7 + y, C["chickSh"])
    g.px(1, 8 + y, C["chick"])
    g.fill(5, 8 + y, 4, 2, C["chickSh"])
    if fr:
        g.px(5, 12, C["chickFeet"])
        g.px(6, 13, C["chickFeet"])
        g.px(10, 12, C["chickFeet"])
        g.px(11, 13, C["chickFeet"])
    else:
        g.px(6, 13, C["chickFeet"])
        g.px(7, 14, C["chickFeet"])
        g.px(10, 13, C["chickFeet"])
        g.px(9, 14, C["chickFeet"])
    return g



def gen_stone_floor(v):
    """Dark mine floor, 3/4 south lip."""
    g = Pix(16, 16)
    mid = C.get("caveFloor", "#4A4840")
    hi = C.get("caveFloorHi", "#6A685C")
    sh = C.get("caveFloorSh", "#2C2A24")
    g.fill(0, 0, 16, 16, mid)
    for i in range(18):
        r = hash01(v + 3, i, 9)
        x = int(hash01(v, i, 1) * 16)
        y = int(hash01(v, i, 2) * 14)
        if r < 0.34:
            g.px(x, y, hi)
        elif r < 0.62:
            g.px(x, y, sh)
        elif r < 0.70:
            g.px(x, y, C["stoneSh"])
    # faint mortar cracks
    if v == 0:
        g.fill(5, 3, 1, 4, sh)
        g.fill(9, 8, 4, 1, sh)
    else:
        g.fill(3, 6, 5, 1, sh)
        g.fill(11, 2, 1, 5, sh)
    for x in range(16):
        if (x + v) % 4 == 0:
            g.px(x, 0, hi)
        g.px(x, 14, sh)
        g.px(x, 15, C["woodOut"] if (x + v) % 2 else sh)
    return g


def gen_hill():
    """Rocky grass for the northern hill."""
    g = gen_grass(2)
    pebbles = [(2, 4), (7, 3), (12, 6), (4, 9), (10, 11), (14, 8), (1, 12), (8, 7), (13, 13)]
    for i, (x, y) in enumerate(pebbles):
        col = C["stoneHi"] if i % 3 == 0 else C["stone"] if i % 3 == 1 else C["stoneSh"]
        g.px(x, y, col)
        if i % 2 == 0:
            g.px(x + 1, y, C["stoneSh"])
    g.px(5, 5, C.get("hillMid", "#7A7A68"))
    g.px(11, 9, C.get("hillMid", "#7A7A68"))
    return g


def gen_wall():
    """3/4 stone wall: top plane + front face."""
    g = Pix(16, 16)
    g.fill(0, 0, 16, 5, C["stoneHi"])
    g.fill(0, 1, 16, 1, C["stone"])
    g.fill(0, 4, 16, 1, C["stoneSh"])
    g.fill(0, 5, 16, 11, C["stone"])
    g.fill(0, 5, 16, 1, C["stoneHi"])
    # block mortar
    for y in (7, 11, 15):
        g.fill(0, y, 16, 1, C["stoneSh"])
    for x, y in ((3, 6), (10, 6), (6, 10), (13, 10), (2, 14), (9, 14)):
        g.fill(x, y, 1, 3 if y < 14 else 2, C["stoneSh"])
    g.fill(0, 5, 1, 11, C["stoneHi"])
    g.fill(15, 5, 1, 11, C["stoneSh"])
    g.px(4, 8, C["stoneHi"])
    g.px(12, 12, C["stoneSh"])
    g.fill(0, 15, 16, 1, C["woodOut"])
    return g


def gen_cave():
    """Original 3/4 rocky hill with a timber-framed mine mouth."""
    g = Pix(64, 48)
    dark = C.get("caveDark", "#14110E")
    g.fill(8, 45, 48, 3, C["shadow"])
    g.fill(14, 44, 36, 1, C["shadowSoft"])
    # back / top of the outcrop
    blob(g, 32, 16, 24, 11, C["stone"], C["stoneSh"], C["stoneHi"], C["stoneSh"])
    blob(g, 14, 20, 13, 9, C["stone"], C["stoneSh"], C["stoneHi"], C["stoneSh"])
    blob(g, 50, 20, 13, 9, C["stone"], C["stoneSh"], C["stoneHi"], C["stoneSh"])
    blob(g, 32, 24, 16, 8, C["stoneHi"], C["stone"], C["stoneHi"], C["stoneSh"])
    # front boulders
    blob(g, 12, 34, 11, 8, C["stone"], C["stoneSh"], C["stone"], C["woodOut"])
    blob(g, 52, 34, 11, 8, C["stone"], C["stoneSh"], C["stone"], C["woodOut"])
    blob(g, 32, 38, 20, 7, C["stone"], C["stoneSh"], C["stone"], C["woodOut"])
    # extra chips
    g.px(20, 12, C["stoneHi"])
    g.px(21, 12, C["stoneHi"])
    g.px(44, 14, C["stoneHi"])
    g.px(8, 28, C["stoneSh"])
    g.px(56, 26, C["stoneSh"])
    # carve the dark arch (front-center)
    for y in range(20, 46):
        for x in range(21, 44):
            dx = (x - 32) / 9.4
            dy = (y - 35) / 12.2
            if dx * dx + dy * dy <= 1.02:
                g.px(x, y, dark)
    # timber frame around the mouth
    g.fill(22, 24, 3, 20, C["woodMid"])
    g.fill(22, 24, 1, 20, C["woodHi"])
    g.fill(24, 24, 1, 20, C["woodSh"])
    g.fill(22, 43, 3, 1, C["woodOut"])
    g.fill(39, 24, 3, 20, C["woodMid"])
    g.fill(39, 24, 1, 20, C["woodHi"])
    g.fill(41, 24, 1, 20, C["woodSh"])
    g.fill(39, 43, 3, 1, C["woodOut"])
    g.fill(21, 21, 22, 4, C["woodMid"])
    g.fill(21, 21, 22, 1, C["woodHi"])
    g.fill(21, 24, 22, 1, C["woodOut"])
    g.fill(21, 21, 1, 4, C["woodOut"])
    g.fill(42, 21, 1, 4, C["woodOut"])
    g.px(26, 22, C["woodSh"])
    g.px(36, 23, C["woodSh"])
    # inner glow hint
    g.px(30, 32, C["woodSh"])
    g.px(33, 34, C["woodMid"])
    # grass tufts at the base
    for x, y in ((6, 40), (7, 39), (8, 41), (55, 40), (56, 39), (57, 41), (18, 43), (46, 43)):
        g.px(x, y, C["grassMid"] if y % 2 else C["grassHi"])
        g.px(x, y + 1, C["grassSh"])
    return g


def gen_lantern():
    g = Pix(16, 24)
    glow = C.get("lanternGlow", "#F0C060")
    g.fill(5, 22, 6, 2, C["shadow"])
    g.fill(7, 12, 2, 10, C["woodMid"])
    g.fill(7, 12, 1, 10, C["woodHi"])
    g.fill(8, 12, 1, 10, C["woodSh"])
    g.fill(3, 2, 10, 2, C["woodSh"])
    g.fill(4, 1, 8, 1, C["woodMid"])
    g.fill(5, 0, 6, 1, C["woodHi"])
    g.fill(4, 4, 8, 8, C["woodOut"])
    g.fill(5, 5, 6, 6, glow)
    g.fill(6, 6, 4, 4, C["parch"])
    g.px(7, 7, C["flower"])
    g.fill(4, 4, 8, 1, C["woodHi"])
    g.fill(4, 11, 8, 1, C["woodSh"])
    return g


def gen_ladder():
    """Hole in the stone floor with a wooden ladder down."""
    g = Pix(16, 24)
    dark = C.get("caveDark", "#14110E")
    # stone rim (top plane of the hole)
    for y in range(2, 12):
        for x in range(1, 15):
            dx = (x - 8) / 6.4
            dy = (y - 6) / 4.2
            d = dx * dx + dy * dy
            if d < 1.15:
                if d > 0.72:
                    g.px(x, y, C["stoneHi"] if y < 7 else C["stone"])
                else:
                    g.px(x, y, dark)
    # darker south lip of the rim
    for x in range(3, 13):
        g.px(x, 10, C["stoneSh"])
        g.px(x, 11, C["woodOut"])
    # rails
    g.fill(4, 8, 2, 15, C["woodMid"])
    g.fill(4, 8, 1, 15, C["woodHi"])
    g.fill(5, 8, 1, 15, C["woodSh"])
    g.fill(10, 8, 2, 15, C["woodMid"])
    g.fill(10, 8, 1, 15, C["woodHi"])
    g.fill(11, 8, 1, 15, C["woodSh"])
    # rungs
    for y in (10, 14, 18, 22):
        g.fill(4, y, 8, 2, C["woodMid"])
        g.fill(4, y, 8, 1, C["woodHi"])
    return g



def gen_copper():
    """3/4 copper nugget: top plane + front face."""
    g = Pix(16, 16)
    hi, mid, sh = C["copperHi"], C["copperMid"], C["copperSh"]
    g.fill(4, 13, 8, 2, C["shadow"])
    # top
    g.fill(5, 5, 6, 1, hi)
    g.fill(4, 6, 8, 2, hi)
    g.fill(5, 7, 6, 1, mid)
    g.px(6, 6, C["flower"])
    g.px(8, 7, sh)
    # front
    g.fill(4, 8, 8, 5, mid)
    g.fill(4, 8, 2, 5, hi)
    g.fill(10, 8, 2, 5, sh)
    g.fill(4, 12, 8, 1, C["woodOut"])
    g.fill(3, 8, 1, 5, C["woodOut"])
    g.fill(12, 8, 1, 5, C["woodOut"])
    g.px(7, 10, sh)
    g.px(9, 9, hi)
    return g


def gen_mushroom():
    """3/4 cave mushroom: cap top + front, pale stem."""
    g = Pix(16, 16)
    cap, caph, caps = C["mushCap"], C["mushCapHi"], C["mushCapSh"]
    stem, stems = C["mushStem"], C["mushStemSh"]
    g.fill(5, 14, 6, 2, C["shadow"])
    # stem
    g.fill(6, 9, 4, 5, stem)
    g.fill(6, 9, 1, 5, C["parch"])
    g.fill(9, 9, 1, 5, stems)
    g.fill(6, 13, 4, 1, C["woodOut"])
    # cap top plane
    g.fill(4, 3, 8, 2, caph)
    g.fill(3, 5, 10, 2, cap)
    g.fill(4, 4, 8, 1, cap)
    g.px(5, 3, C["parch"])
    g.px(7, 4, caph)
    # cap front
    g.fill(3, 7, 10, 3, cap)
    g.fill(3, 7, 10, 1, caph)
    g.fill(3, 9, 10, 1, caps)
    g.fill(2, 7, 1, 3, caps)
    g.fill(13, 7, 1, 3, C["woodOut"])
    g.px(6, 8, C["parch"])
    g.px(10, 8, caph)
    return g


def gen_moonshard():
    """3/4 moon shard crystal: top facet + glowing front."""
    g = Pix(16, 16)
    hi, mid, sh, glow = C["moonHi"], C["moonMid"], C["moonSh"], C["moonGlow"]
    g.fill(5, 14, 6, 2, C["shadow"])
    # diamond crystal, 3/4
    pts = [
        (7, 2, hi), (8, 2, hi),
        (6, 3, hi), (7, 3, hi), (8, 3, glow), (9, 3, mid),
        (5, 4, mid), (6, 4, hi), (7, 4, glow), (8, 4, hi), (9, 4, mid), (10, 4, sh),
        (4, 5, mid), (5, 5, hi), (6, 5, glow), (7, 5, hi), (8, 5, mid), (9, 5, mid), (10, 5, sh), (11, 5, sh),
        (4, 6, mid), (5, 6, mid), (6, 6, hi), (7, 6, mid), (8, 6, mid), (9, 6, sh), (10, 6, sh), (11, 6, C["woodOut"]),
        (5, 7, mid), (6, 7, mid), (7, 7, mid), (8, 7, sh), (9, 7, sh), (10, 7, C["woodOut"]),
        (5, 8, mid), (6, 8, sh), (7, 8, sh), (8, 8, sh), (9, 8, C["woodOut"]),
        (6, 9, sh), (7, 9, sh), (8, 9, C["woodOut"]),
        (6, 10, sh), (7, 10, C["woodOut"]), (8, 10, C["woodOut"]),
        (7, 11, C["woodOut"]),
    ]
    for x, y, col in pts:
        g.px(x, y, col)
    g.px(7, 5, glow)
    g.px(6, 4, hi)
    return g


def gen_note():
    """Wall note: wood slat + tacked parchment, 3/4."""
    g = Pix(16, 16)
    g.fill(3, 14, 10, 2, C["shadow"])
    # wood board
    g.fill(2, 2, 12, 3, C["woodHi"])
    g.fill(2, 5, 12, 9, C["woodMid"])
    g.fill(2, 5, 1, 9, C["woodHi"])
    g.fill(13, 5, 1, 9, C["woodSh"])
    g.fill(2, 13, 12, 1, C["woodOut"])
    # parchment
    g.fill(4, 4, 8, 8, C["parch"])
    g.fill(4, 4, 8, 1, C["flower"])
    g.fill(4, 11, 8, 1, C["dirtSh"])
    g.px(5, 6, C["uiText"])
    g.px(6, 6, C["uiText"])
    g.px(7, 6, C["uiText"])
    g.px(5, 8, C["uiText"])
    g.px(6, 8, C["uiText"])
    g.px(8, 8, C["uiText"])
    g.px(5, 10, C["uiText"])
    g.px(7, 10, C["uiText"])
    # tack
    g.px(7, 3, C["copperMid"])
    g.px(8, 3, C["copperHi"])
    return g


def gen_trophy():
    """Tiny 3/4 wood star for the achievement HUD."""
    g = Pix(16, 16)
    gold, hi, sh = C["flower"], C["parch"], C["dirtSh"]
    g.fill(5, 14, 6, 2, C["shadow"])
    # five-point star, chunky
    g.fill(7, 2, 2, 2, hi)
    g.fill(6, 4, 4, 2, gold)
    g.fill(2, 6, 12, 2, gold)
    g.fill(3, 6, 10, 1, hi)
    g.fill(5, 8, 6, 2, gold)
    g.fill(4, 10, 3, 3, gold)
    g.fill(9, 10, 3, 3, sh)
    g.fill(6, 8, 4, 3, gold)
    g.px(7, 5, hi)
    g.px(8, 7, C["dirtHi"])
    g.px(4, 7, sh)
    g.px(11, 7, sh)
    return g



def gen_woodfloor():
    """3/4 pine floor: plank tops + a darker south lip."""
    g = Pix(16, 16)
    g.fill(0, 0, 16, 16, C["woodMid"])
    # three receding planks
    bands = [(0, 5, C["woodHi"], C["woodMid"]), (5, 5, C["woodMid"], C["woodSh"]), (10, 4, C["woodMid"], C["woodSh"])]
    y0 = 0
    for i, (skip, h, hi, mid) in enumerate(bands):
        g.fill(0, y0, 16, h, mid)
        g.fill(0, y0, 16, 1, hi)
        g.fill(0, y0 + h - 1, 16, 1, C["woodSh"])
        # grain
        for x in (2 + i, 7 + i, 12 + (i % 2)):
            if 0 <= x < 16:
                g.px(x, y0 + 2, C["woodSh"])
                if y0 + 3 < y0 + h - 1:
                    g.px(x, y0 + 3, C["woodHi"] if i == 0 else C["woodSh"])
        # plank seams
        g.fill(5 + i * 3, y0 + 1, 1, h - 2, C["woodOut"])
        y0 += h
    # 3/4 south lip
    g.fill(0, 14, 16, 1, C["woodSh"])
    g.fill(0, 15, 16, 1, C["woodOut"])
    g.px(3, 1, C["woodHi"])
    g.px(11, 6, C["woodHi"])
    return g


def gen_inwall():
    """3/4 interior timber wall: top plate + front boards."""
    g = Pix(16, 16)
    g.fill(0, 0, 16, 5, C["woodHi"])
    g.fill(0, 1, 16, 1, C["woodMid"])
    g.fill(0, 4, 16, 1, C["woodSh"])
    g.fill(0, 5, 16, 11, C["woodMid"])
    g.fill(0, 5, 16, 1, C["woodHi"])
    # board seams
    for x in (3, 8, 13):
        g.fill(x, 6, 1, 9, C["woodSh"])
    g.fill(0, 9, 16, 1, C["woodSh"])
    g.fill(0, 10, 16, 1, C["woodHi"])
    g.fill(0, 5, 1, 11, C["woodHi"])
    g.fill(15, 5, 1, 11, C["woodSh"])
    g.px(5, 7, C["woodHi"])
    g.px(11, 12, C["woodSh"])
    g.fill(0, 15, 16, 1, C["woodOut"])
    return g


def gen_bed():
    """Original 3/4 bed: pine frame, two pillows, spring quilt. Not a Stardew copy."""
    g = Pix(32, 32)
    g.fill(3, 29, 26, 3, C["shadow"])
    # headboard (far): top cap + front
    g.fill(4, 2, 24, 3, C["woodHi"])
    g.fill(5, 1, 22, 2, C["woodMid"])
    g.fill(6, 0, 20, 2, C["woodHi"])
    g.fill(4, 4, 24, 5, C["woodMid"])
    g.fill(4, 4, 2, 5, C["woodHi"])
    g.fill(26, 4, 2, 5, C["woodSh"])
    g.fill(3, 2, 1, 7, C["woodOut"])
    g.fill(28, 2, 1, 7, C["woodOut"])
    g.fill(4, 8, 24, 1, C["woodOut"])
    # pillows (top plane + front)
    g.fill(6, 6, 9, 3, C["parch"])
    g.fill(17, 6, 9, 3, C["parch"])
    g.fill(6, 6, 9, 1, "#FFF0D0")
    g.fill(17, 6, 9, 1, "#FFF0D0")
    g.fill(6, 9, 9, 2, C["dirtHi"])
    g.fill(17, 9, 9, 2, C["dirtHi"])
    g.px(8, 7, C["blossom"])
    g.px(20, 7, C["flower"])
    # quilt top (receding patches of teal / blossom / gold)
    quilt = [
        (C["playerShirt"], C["playerShirtHi"], C["playerShirtSh"]),
        (C["blossom"], "#F0C0C8", C["roofSh"]),
        (C["flower"], C["parch"], C["dirtSh"]),
    ]
    for row in range(3):
        y = 11 + row * 4
        for col in range(4):
            q = quilt[(row + col) % 3]
            x = 5 + col * 5
            g.fill(x, y, 5, 3, q[0])
            g.fill(x, y, 5, 1, q[1])
            g.fill(x, y + 2, 5, 1, q[2])
    # quilt front face
    g.fill(5, 23, 22, 4, C["playerShirt"])
    g.fill(5, 23, 22, 1, C["playerShirtHi"])
    g.fill(5, 26, 22, 1, C["playerShirtSh"])
    g.fill(10, 24, 5, 2, C["blossom"])
    g.fill(20, 24, 5, 2, C["flower"])
    # side rails
    g.fill(3, 11, 2, 16, C["woodMid"])
    g.fill(3, 11, 1, 16, C["woodHi"])
    g.fill(27, 11, 2, 16, C["woodSh"])
    g.fill(28, 11, 1, 16, C["woodOut"])
    # footboard
    g.fill(3, 26, 26, 4, C["woodMid"])
    g.fill(3, 26, 26, 1, C["woodHi"])
    g.fill(3, 29, 26, 1, C["woodOut"])
    g.fill(3, 26, 1, 4, C["woodHi"])
    g.fill(28, 26, 1, 4, C["woodOut"])
    g.px(8, 27, C["woodHi"])
    g.px(22, 28, C["woodSh"])
    return g


def gen_table():
    """3/4 farm table with a clay pot of spring flowers."""
    g = Pix(32, 24)
    g.fill(4, 22, 24, 2, C["shadow"])
    # top plane
    g.fill(3, 6, 26, 4, C["woodHi"])
    g.fill(4, 5, 24, 2, C["woodHi"])
    g.fill(6, 4, 20, 2, C["parch"])
    g.fill(3, 9, 26, 1, C["woodOut"])
    g.px(8, 6, C["woodMid"])
    g.px(18, 7, C["woodMid"])
    # front apron
    g.fill(3, 10, 24, 4, C["woodMid"])
    g.fill(3, 10, 24, 1, C["woodHi"])
    g.fill(3, 13, 24, 1, C["woodSh"])
    g.fill(3, 10, 1, 4, C["woodHi"])
    g.fill(26, 10, 1, 4, C["woodOut"])
    # right side sliver
    g.fill(27, 6, 3, 4, C["woodSh"])
    g.fill(27, 10, 3, 4, C["woodSh"])
    g.fill(29, 6, 1, 8, C["woodOut"])
    # legs
    for x in (4, 23):
        g.fill(x, 14, 3, 8, C["woodMid"])
        g.fill(x, 14, 1, 8, C["woodHi"])
        g.fill(x + 2, 14, 1, 8, C["woodSh"])
        g.fill(x, 21, 3, 1, C["woodOut"])
    # clay pot + flowers (sits on the top plane)
    g.fill(14, 2, 5, 4, C["copperMid"])
    g.fill(14, 2, 5, 1, C["copperHi"])
    g.fill(14, 5, 5, 1, C["copperSh"])
    g.fill(15, 1, 3, 2, C["copperMid"])
    g.px(13, 0, C["leaf"])
    g.px(16, 0, C["blossom"])
    g.px(18, 0, C["flower"])
    g.px(15, 0, C["leaf"])
    g.px(17, 1, C["leaf"])
    return g


def gen_rug():
    """Plum oval rug with a blossom border. Walkable floor cloth."""
    g = Pix(48, 32)
    mid, hi, sh = C["npcShirt"], C["npcShirtHi"], C["npcShirtSh"]
    for y in range(32):
        for x in range(48):
            dx = (x - 23.5) / 21.0
            dy = (y - 16.0) / 12.5
            d = dx * dx + dy * dy
            if d <= 1.05:
                if d > 0.82:
                    g.px(x, y, C["parch"] if y < 18 else C["dirtHi"])
                elif d > 0.68:
                    g.px(x, y, hi if y < 15 else sh)
                else:
                    col = mid
                    if y < 12:
                        col = hi
                    elif y > 20:
                        col = sh
                    g.px(x, y, col)
    # inner diamond stitch
    for x, y in ((24, 10), (18, 16), (24, 16), (30, 16), (24, 21)):
        g.px(x, y, C["blossom"])
    g.px(24, 13, C["flower"])
    g.px(21, 16, C["parch"])
    g.px(27, 16, C["parch"])
    # south lip
    for x in range(8, 40):
        dx = (x - 23.5) / 21.0
        if dx * dx + (14.0 / 12.5) ** 2 <= 1.02:
            g.px(x, 27, sh)
            g.px(x, 28, C["woodOut"])
    return g


def gen_window():
    """Interior casement: sky glass, wood frame, sill flower."""
    g = Pix(16, 24)
    g.fill(1, 2, 14, 18, C["woodOut"])
    g.fill(2, 3, 12, 3, C["woodHi"])
    g.fill(2, 6, 12, 12, C["woodMid"])
    # glass
    g.fill(3, 5, 10, 11, C["sky"])
    g.fill(3, 5, 10, 3, "#A8D4F0")
    g.fill(3, 13, 10, 3, C["glass"])
    # distant hill hint
    g.fill(3, 14, 10, 2, C["grassMid"])
    g.px(5, 13, C["grassHi"])
    g.px(10, 13, C["leaf"])
    # muntins
    g.fill(7, 5, 2, 11, C["woodOut"])
    g.fill(3, 9, 10, 2, C["woodOut"])
    g.px(4, 6, C["parch"])
    g.px(11, 6, C["parch"])
    # sill
    g.fill(0, 17, 16, 3, C["woodMid"])
    g.fill(0, 17, 16, 1, C["woodHi"])
    g.fill(0, 19, 16, 1, C["woodOut"])
    g.px(4, 16, C["leaf"])
    g.px(6, 15, C["blossom"])
    g.px(8, 16, C["leaf"])
    g.px(10, 15, C["flower"])
    return g


def gen_doormat():
    """Woven rush mat on the floor in front of the door."""
    g = Pix(16, 16)
    g.fill(1, 4, 14, 9, C["dirtMid"])
    g.fill(1, 4, 14, 1, C["dirtHi"])
    g.fill(1, 12, 14, 1, C["dirtSh"])
    for y in range(5, 12):
        col = C["dirtHi"] if y % 2 == 0 else C["dirtSh"]
        g.fill(2, y, 12, 1, col)
    g.fill(1, 4, 1, 9, C["tillOut"])
    g.fill(14, 4, 1, 9, C["tillOut"])
    g.px(4, 7, C["parch"])
    g.px(11, 9, C["parch"])
    g.fill(2, 13, 12, 1, C["woodOut"])
    return g


def gen_inndoor():
    """Interior pine door in a frame, 3/4, matching the cottage (not Stardew)."""
    g = Pix(16, 24)
    # frame
    g.fill(1, 0, 14, 23, C["woodOut"])
    g.fill(2, 1, 12, 2, C["woodHi"])
    g.fill(2, 3, 12, 19, C["woodMid"])
    # door slab
    g.fill(3, 3, 10, 18, C["door"])
    g.fill(3, 3, 10, 1, C["woodHi"])
    g.fill(3, 3, 1, 18, C["woodMid"])
    g.fill(12, 3, 1, 18, C["woodOut"])
    g.fill(3, 11, 10, 1, C["woodOut"])
    g.fill(3, 20, 10, 1, C["woodOut"])
    # window pane
    g.fill(6, 5, 4, 4, C["glass"])
    g.fill(6, 5, 4, 1, C["parch"])
    g.fill(7, 6, 2, 2, C["sky"])
    # knob
    g.px(11, 13, C["flower"])
    g.px(11, 14, C["dirtHi"])
    return g


GENERATORS = {
    "grass0": lambda: gen_grass(0),
    "grass1": lambda: gen_grass(1),
    "grass2": lambda: gen_grass(2),
    "grass3": lambda: gen_grass(3),
    "dirt": gen_dirt,
    "till": gen_till,
    "water": gen_water,
    "pond": gen_pond,
    "tree": gen_tree,
    "house": gen_house,
    "well": gen_well,
    "mailbox": gen_mailbox,
    "mailboxUp": gen_mailbox_up,
    "letter": gen_letter,
    "crate": gen_crate,
    "rock0": lambda: gen_rock(0),
    "rock1": lambda: gen_rock(1),
    "weed0": lambda: gen_weed(0),
    "weed1": lambda: gen_weed(1),
    "fenceH": gen_fence_h,
    "fenceL": gen_fence_l,
    "fenceR": gen_fence_r,
    "seed": gen_seed,
    "sprout": gen_sprout,
    "cropYoung": gen_crop_young,
    "cropReady": gen_crop_ready,
    "veggie": gen_veggie,
    "stump": gen_stump,
    "wood": gen_wood,
    "stoneItem": gen_stone_item,
    "path": gen_path,
    "player-down-0": lambda: gen_person("player", "down", 0),
    "player-down-1": lambda: gen_person("player", "down", 1),
    "player-up-0": lambda: gen_person("player", "up", 0),
    "player-up-1": lambda: gen_person("player", "up", 1),
    "player-right-0": lambda: gen_person("player", "right", 0),
    "player-right-1": lambda: gen_person("player", "right", 1),
    "player-left-0": lambda: gen_person("player", "right", 0).flip_h(),
    "player-left-1": lambda: gen_person("player", "right", 1).flip_h(),
    "npc-down-0": lambda: gen_person("npc", "down", 0),
    "npc-down-1": lambda: gen_person("npc", "down", 1),
    "npc-up-0": lambda: gen_person("npc", "up", 0),
    "npc-up-1": lambda: gen_person("npc", "up", 1),
    "npc-right-0": lambda: gen_person("npc", "right", 0),
    "npc-right-1": lambda: gen_person("npc", "right", 1),
    "npc-left-0": lambda: gen_person("npc", "right", 0).flip_h(),
    "npc-left-1": lambda: gen_person("npc", "right", 1).flip_h(),
    "chicken-right-0": lambda: gen_chicken(0),
    "chicken-right-1": lambda: gen_chicken(1),
    "chicken-left-0": lambda: gen_chicken(0).flip_h(),
    "chicken-left-1": lambda: gen_chicken(1).flip_h(),
    "stone0": lambda: gen_stone_floor(0),
    "stone1": lambda: gen_stone_floor(1),
    "hill": gen_hill,
    "wall": gen_wall,
    "cave": gen_cave,
    "lantern": gen_lantern,
    "ladder": gen_ladder,
    "copper": gen_copper,
    "mushroom": gen_mushroom,
    "moonshard": gen_moonshard,
    "note": gen_note,
    "trophy": gen_trophy,
    "woodfloor": gen_woodfloor,
    "inwall": gen_inwall,
    "bed": gen_bed,
    "table": gen_table,
    "rug": gen_rug,
    "window": gen_window,
    "doormat": gen_doormat,
    "inndoor": gen_inndoor,
}


def builtin_sprites():
    A = [8, 28]
    Ck = [8, 14]
    return [
        {"id": "grass0", "file": "tiles/grass0.png", "w": 16, "h": 16, "frames": 1, "anchor": [0, 0], "ox": 0, "oy": 0, "generated": True},
        {"id": "grass1", "file": "tiles/grass1.png", "w": 16, "h": 16, "frames": 1, "anchor": [0, 0], "ox": 0, "oy": 0, "generated": True},
        {"id": "grass2", "file": "tiles/grass2.png", "w": 16, "h": 16, "frames": 1, "anchor": [0, 0], "ox": 0, "oy": 0, "generated": True},
        {"id": "grass3", "file": "tiles/grass3.png", "w": 16, "h": 16, "frames": 1, "anchor": [0, 0], "ox": 0, "oy": 0, "generated": True},
        {"id": "dirt", "file": "tiles/dirt.png", "w": 16, "h": 16, "frames": 1, "anchor": [0, 0], "ox": 0, "oy": 0, "generated": True},
        {"id": "till", "file": "tiles/till.png", "w": 16, "h": 16, "frames": 1, "anchor": [0, 0], "ox": 0, "oy": 0, "generated": True},
        {"id": "water", "file": "tiles/water.png", "w": 16, "h": 16, "frames": 1, "anchor": [0, 0], "ox": 0, "oy": 0, "generated": True},
        {"id": "house", "file": "props/house.png", "w": 80, "h": 80, "frames": 1, "anchor": [0, 0], "ox": 0, "oy": -16, "generated": True},
        {"id": "tree", "file": "props/tree.png", "w": 48, "h": 64, "frames": 1, "anchor": [0, 0], "ox": -16, "oy": -48, "generated": True},
        {"id": "well", "file": "props/well.png", "w": 16, "h": 32, "frames": 1, "anchor": [0, 0], "ox": 0, "oy": -16, "generated": True},
        {"id": "mailbox", "file": "props/mailbox.png", "w": 16, "h": 24, "frames": 1, "anchor": [0, 0], "ox": 0, "oy": -8, "generated": True},
        {"id": "mailboxUp", "file": "props/mailbox-up.png", "w": 16, "h": 32, "frames": 1, "anchor": [0, 0], "ox": 0, "oy": -16, "generated": True},
        {"id": "letter", "file": "ui/letter.png", "w": 16, "h": 16, "frames": 1, "anchor": [0, 0], "ox": 0, "oy": 0, "generated": True},
        {"id": "crate", "file": "props/crate.png", "w": 16, "h": 16, "frames": 1, "anchor": [0, 0], "ox": 0, "oy": 0, "generated": True},
        {"id": "pond", "file": "props/pond.png", "w": 36, "h": 32, "frames": 1, "anchor": [0, 0], "ox": -2, "oy": 0, "generated": True},
        {"id": "rock0", "file": "props/rock0.png", "w": 16, "h": 16, "frames": 1, "anchor": [0, 0], "ox": 0, "oy": 0, "generated": True},
        {"id": "rock1", "file": "props/rock1.png", "w": 16, "h": 16, "frames": 1, "anchor": [0, 0], "ox": 0, "oy": 0, "generated": True},
        {"id": "weed0", "file": "props/weed0.png", "w": 16, "h": 16, "frames": 1, "anchor": [0, 0], "ox": 0, "oy": 0, "generated": True},
        {"id": "weed1", "file": "props/weed1.png", "w": 16, "h": 16, "frames": 1, "anchor": [0, 0], "ox": 0, "oy": 0, "generated": True},
        {"id": "fenceH", "file": "props/fenceH.png", "w": 16, "h": 16, "frames": 1, "anchor": [0, 0], "ox": 0, "oy": 0, "generated": True},
        {"id": "fenceL", "file": "props/fenceL.png", "w": 16, "h": 16, "frames": 1, "anchor": [0, 0], "ox": 0, "oy": 0, "generated": True},
        {"id": "fenceR", "file": "props/fenceR.png", "w": 16, "h": 16, "frames": 1, "anchor": [0, 0], "ox": 0, "oy": 0, "generated": True},
        {"id": "seed", "file": "ui/seed.png", "w": 16, "h": 16, "frames": 1, "anchor": [0, 0], "ox": 0, "oy": 0, "generated": True},
        {"id": "sprout", "file": "ui/sprout.png", "w": 16, "h": 16, "frames": 1, "anchor": [0, 0], "ox": 0, "oy": 0, "generated": True},
        {"id": "cropYoung", "file": "ui/cropYoung.png", "w": 16, "h": 16, "frames": 1, "anchor": [0, 0], "ox": 0, "oy": 0, "generated": True},
        {"id": "cropReady", "file": "ui/cropReady.png", "w": 16, "h": 16, "frames": 1, "anchor": [0, 0], "ox": 0, "oy": 0, "generated": True},
        {"id": "veggie", "file": "ui/veggie.png", "w": 16, "h": 16, "frames": 1, "anchor": [0, 0], "ox": 0, "oy": 0, "generated": True},
        {"id": "stump", "file": "props/stump.png", "w": 16, "h": 16, "frames": 1, "anchor": [0, 0], "ox": 0, "oy": 0, "generated": True},
        {"id": "wood", "file": "ui/wood.png", "w": 16, "h": 16, "frames": 1, "anchor": [0, 0], "ox": 0, "oy": 0, "generated": True},
        {"id": "stoneItem", "file": "ui/stone.png", "w": 16, "h": 16, "frames": 1, "anchor": [0, 0], "ox": 0, "oy": 0, "generated": True},
        {"id": "path", "file": "tiles/path.png", "w": 16, "h": 16, "frames": 1, "anchor": [0, 0], "ox": 0, "oy": 0, "generated": True},
        {"id": "player-down", "file": "actors/player-down-{n}.png", "w": 16, "h": 32, "frames": 2, "anchor": A, "ox": 0, "oy": 0, "generated": True},
        {"id": "player-up", "file": "actors/player-up-{n}.png", "w": 16, "h": 32, "frames": 2, "anchor": A, "ox": 0, "oy": 0, "generated": True},
        {"id": "player-right", "file": "actors/player-right-{n}.png", "w": 16, "h": 32, "frames": 2, "anchor": A, "ox": 0, "oy": 0, "generated": True},
        {"id": "player-left", "file": "actors/player-left-{n}.png", "w": 16, "h": 32, "frames": 2, "anchor": A, "ox": 0, "oy": 0, "generated": True},
        {"id": "npc-down", "file": "actors/npc-down-{n}.png", "w": 16, "h": 32, "frames": 2, "anchor": A, "ox": 0, "oy": 0, "generated": True},
        {"id": "npc-up", "file": "actors/npc-up-{n}.png", "w": 16, "h": 32, "frames": 2, "anchor": A, "ox": 0, "oy": 0, "generated": True},
        {"id": "npc-right", "file": "actors/npc-right-{n}.png", "w": 16, "h": 32, "frames": 2, "anchor": A, "ox": 0, "oy": 0, "generated": True},
        {"id": "npc-left", "file": "actors/npc-left-{n}.png", "w": 16, "h": 32, "frames": 2, "anchor": A, "ox": 0, "oy": 0, "generated": True},
        {"id": "chicken-right", "file": "actors/chicken-right-{n}.png", "w": 16, "h": 16, "frames": 2, "anchor": Ck, "ox": 0, "oy": 0, "generated": True},
        {"id": "chicken-left", "file": "actors/chicken-left-{n}.png", "w": 16, "h": 16, "frames": 2, "anchor": Ck, "ox": 0, "oy": 0, "generated": True},
        {"id": "stone0", "file": "tiles/stone0.png", "w": 16, "h": 16, "frames": 1, "anchor": [0, 0], "ox": 0, "oy": 0, "generated": True},
        {"id": "stone1", "file": "tiles/stone1.png", "w": 16, "h": 16, "frames": 1, "anchor": [0, 0], "ox": 0, "oy": 0, "generated": True},
        {"id": "hill", "file": "tiles/hill.png", "w": 16, "h": 16, "frames": 1, "anchor": [0, 0], "ox": 0, "oy": 0, "generated": True},
        {"id": "wall", "file": "tiles/wall.png", "w": 16, "h": 16, "frames": 1, "anchor": [0, 0], "ox": 0, "oy": 0, "generated": True},
        {"id": "cave", "file": "props/cave.png", "w": 64, "h": 48, "frames": 1, "anchor": [0, 0], "ox": 0, "oy": -16, "generated": True},
        {"id": "lantern", "file": "props/lantern.png", "w": 16, "h": 24, "frames": 1, "anchor": [0, 0], "ox": 0, "oy": -8, "generated": True},
        {"id": "ladder", "file": "props/ladder.png", "w": 16, "h": 24, "frames": 1, "anchor": [0, 0], "ox": 0, "oy": -8, "generated": True},
        {"id": "copper", "file": "ui/copper.png", "w": 16, "h": 16, "frames": 1, "anchor": [0, 0], "ox": 0, "oy": 0, "generated": True},
        {"id": "mushroom", "file": "ui/mushroom.png", "w": 16, "h": 16, "frames": 1, "anchor": [0, 0], "ox": 0, "oy": 0, "generated": True},
        {"id": "moonshard", "file": "ui/moonshard.png", "w": 16, "h": 16, "frames": 1, "anchor": [0, 0], "ox": 0, "oy": 0, "generated": True},
        {"id": "note", "file": "props/note.png", "w": 16, "h": 16, "frames": 1, "anchor": [0, 0], "ox": 0, "oy": 0, "generated": True},
        {"id": "trophy", "file": "ui/trophy.png", "w": 16, "h": 16, "frames": 1, "anchor": [0, 0], "ox": 0, "oy": 0, "generated": True},
        {"id": "woodfloor", "file": "tiles/woodfloor.png", "w": 16, "h": 16, "frames": 1, "anchor": [0, 0], "ox": 0, "oy": 0, "generated": True},
        {"id": "inwall", "file": "tiles/inwall.png", "w": 16, "h": 16, "frames": 1, "anchor": [0, 0], "ox": 0, "oy": 0, "generated": True},
        {"id": "bed", "file": "props/bed.png", "w": 32, "h": 32, "frames": 1, "anchor": [0, 0], "ox": 0, "oy": 0, "generated": True},
        {"id": "table", "file": "props/table.png", "w": 32, "h": 24, "frames": 1, "anchor": [0, 0], "ox": 0, "oy": -8, "generated": True},
        {"id": "rug", "file": "props/rug.png", "w": 48, "h": 32, "frames": 1, "anchor": [0, 0], "ox": 0, "oy": 0, "generated": True},
        {"id": "window", "file": "props/window.png", "w": 16, "h": 24, "frames": 1, "anchor": [0, 0], "ox": 0, "oy": 0, "generated": True},
        {"id": "doormat", "file": "props/doormat.png", "w": 16, "h": 16, "frames": 1, "anchor": [0, 0], "ox": 0, "oy": 0, "generated": True},
        {"id": "inndoor", "file": "props/inndoor.png", "w": 16, "h": 24, "frames": 1, "anchor": [0, 0], "ox": 0, "oy": -8, "generated": True},
    ]


def frame_path(sprite, n):
    return sprite["file"].replace("{n}", str(n))


def frame_gen_id(sprite, n):
    if sprite["frames"] <= 1 and "{n}" not in sprite["file"]:
        return sprite["id"]
    return "%s-%d" % (sprite["id"], n)


def merge_manifest(builtins):
    extras = []
    if MANIFEST_PATH.exists():
        old = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
        bids = {s["id"] for s in builtins}
        for s in old.get("sprites", []):
            if s.get("id") not in bids:
                extras.append(s)
    return builtins + extras


def ensure_pngs(sprites, regen):
    for spr in sprites:
        for n in range(spr.get("frames", 1)):
            rel = frame_path(spr, n)
            path = ASSETS / rel
            gid = frame_gen_id(spr, n)
            if path.exists() and not (regen and spr.get("generated") and gid in GENERATORS):
                continue
            if gid not in GENERATORS:
                if path.exists():
                    continue
                raise SystemExit("missing PNG %s (id %s) and no generator" % (rel, gid))
            pix = GENERATORS[gid]()
            if pix.w != spr["w"] or pix.h != spr["h"]:
                raise SystemExit("%s size %dx%d != %dx%d" % (gid, pix.w, pix.h, spr["w"], spr["h"]))
            pix.save(path)
            print("  wrote", rel)


def pack_atlas(sprites, pad=1):
    strips = []
    for spr in sprites:
        frames = []
        for n in range(spr.get("frames", 1)):
            frames.append(Pix.load(ASSETS / frame_path(spr, n)))
        fw, fh = spr["w"], spr["h"]
        strip = Pix(fw * len(frames) + pad * (len(frames) - 1) if False else fw * len(frames), fh)
        # pack frames flush (no pad inside strip) so fw math stays simple
        for i, fr in enumerate(frames):
            strip.blit(fr, i * fw, 0)
        strips.append((spr, strip))
    strips.sort(key=lambda t: -t[1].h)
    atlas_w = 256
    x = pad
    y = pad
    row_h = 0
    placed = []
    for spr, strip in strips:
        if x + strip.w + pad > atlas_w:
            x = pad
            y += row_h + pad
            row_h = 0
        placed.append((spr, strip, x, y))
        x += strip.w + pad
        row_h = max(row_h, strip.h)
    atlas_h = y + row_h + pad
    # grow width if a single strip is wider
    max_w = max(s.w for _spr, s in strips)
    if max_w + pad * 2 > atlas_w:
        atlas_w = max_w + pad * 2
        return pack_atlas_wide(sprites, atlas_w, pad)
    atlas = Pix(atlas_w, atlas_h)
    out_sprites = []
    atlas_map = {}
    for spr, strip, px, py in placed:
        atlas.blit(strip, px, py)
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
            "x": px, "y": py, "w": strip.w, "h": strip.h,
            "fw": spr["w"], "frames": spr.get("frames", 1),
            "anchor": spr.get("anchor", [0, 0]),
            "ox": spr.get("ox", 0), "oy": spr.get("oy", 0),
        }
    return atlas, out_sprites, atlas_map


def pack_atlas_wide(sprites, atlas_w, pad):
    # retry with a wider sheet
    x = pad
    y = pad
    row_h = 0
    placed = []
    strips = []
    for spr in sprites:
        frames = [Pix.load(ASSETS / frame_path(spr, n)) for n in range(spr.get("frames", 1))]
        strip = Pix(spr["w"] * len(frames), spr["h"])
        for i, fr in enumerate(frames):
            strip.blit(fr, i * spr["w"], 0)
        strips.append((spr, strip))
    strips.sort(key=lambda t: -t[1].h)
    for spr, strip in strips:
        if x + strip.w + pad > atlas_w:
            x = pad
            y += row_h + pad
            row_h = 0
        placed.append((spr, strip, x, y))
        x += strip.w + pad
        row_h = max(row_h, strip.h)
    atlas = Pix(atlas_w, y + row_h + pad)
    out_sprites = []
    atlas_map = {}
    for spr, strip, px, py in placed:
        atlas.blit(strip, px, py)
        rec = {
            "id": spr["id"], "file": spr["file"], "w": spr["w"], "h": spr["h"],
            "frames": spr.get("frames", 1), "anchor": spr.get("anchor", [0, 0]),
            "ox": spr.get("ox", 0), "oy": spr.get("oy", 0),
            "x": px, "y": py, "fw": spr["w"],
        }
        if spr.get("generated"):
            rec["generated"] = True
        out_sprites.append(rec)
        atlas_map[spr["id"]] = {
            "x": px, "y": py, "w": strip.w, "h": strip.h,
            "fw": spr["w"], "frames": spr.get("frames", 1),
            "anchor": spr.get("anchor", [0, 0]),
            "ox": spr.get("ox", 0), "oy": spr.get("oy", 0),
        }
    return atlas, out_sprites, atlas_map


GROUND = [
    "gggggggggggggggggggg",
    "gggggggggggggggggggg",
    "gggggggggggggggggggg",
    "gggggggggggggggggggg",
    "gggggggggggggggggggg",
    "ggggggggggggddddgggg",
    "gggggppgggggddddgggg",
    "gggggppgggggdddggggg",
    "gggggppggggdddgggggg",
    "ggggggggggdddggggggg",
    "gggggggggdddgggggggg",
    "ggggggggddgggggggggg",
]

PROPS = [
    ("tree", 2, 3),
    ("house", 13, 1),
    ("well", 18, 4),
    ("mailbox", 16, 5),
    ("crate", 12, 4),
    ("pond", 1, 9),
    ("rock0", 8, 3),
    ("rock1", 18, 10),
    ("rock0", 11, 11),
    ("weed0", 4, 4),
    ("weed1", 10, 2),
    ("weed0", 12, 5),
    ("weed1", 19, 7),
    ("weed0", 9, 6),
    ("fenceH", 4, 5),
    ("fenceH", 5, 5),
    ("fenceH", 6, 5),
    ("fenceL", 4, 6),
    ("fenceL", 4, 7),
    ("fenceL", 4, 8),
    ("fenceR", 7, 5),
    ("fenceR", 7, 6),
    ("fenceR", 7, 7),
    ("fenceR", 7, 8),
]


def draw_preview(atlas_map, atlas: Pix, scale=2):
    vw, vh = 320, 192
    world = Pix(vw, vh)
    tiles = {
        "grass0": Pix.load(ASSETS / "tiles/grass0.png"),
        "grass1": Pix.load(ASSETS / "tiles/grass1.png"),
        "grass2": Pix.load(ASSETS / "tiles/grass2.png"),
        "grass3": Pix.load(ASSETS / "tiles/grass3.png"),
        "dirt": Pix.load(ASSETS / "tiles/dirt.png"),
        "till": Pix.load(ASSETS / "tiles/till.png"),
        "sprout": Pix.load(ASSETS / "ui/sprout.png"),
    }

    def grass_index(tx, ty):
        return ((tx * 3 + ty * 7) & 0xFFFFFFFF) % 4

    for ty, row in enumerate(GROUND):
        for tx, ch in enumerate(row):
            if ch == "d":
                world.blit(tiles["dirt"], tx * 16, ty * 16)
            elif ch == "p":
                world.blit(tiles["till"], tx * 16, ty * 16)
                if (tx, ty) in ((5, 6), (6, 7)):
                    world.blit(tiles["sprout"], tx * 16, ty * 16)
            else:
                world.blit(tiles["grass%d" % grass_index(tx, ty)], tx * 16, ty * 16)

    def blit_id(sid, x, y, frame=0):
        rec = atlas_map[sid]
        src = Pix(rec["fw"], rec["h"])
        # copy from atlas
        sx = rec["x"] + frame * rec["fw"]
        sy = rec["y"]
        for yy in range(rec["h"]):
            for xx in range(rec["fw"]):
                o = ((sy + yy) * atlas.w + (sx + xx)) * 4
                src._set(xx, yy, (atlas.data[o], atlas.data[o + 1], atlas.data[o + 2], atlas.data[o + 3]))
        ax, ay = rec["anchor"]
        world.blit(src, int(x + rec["ox"] - ax), int(y + rec["oy"] - ay))

    # z-sort-ish: props then actors
    for kind, tx, ty in PROPS:
        blit_id(kind, tx * 16, ty * 16)
    blit_id("npc-right", 10 * 16 + 8, 5 * 16 + 14, 0)
    blit_id("chicken-right", 8 * 16 + 8, 8 * 16 + 14, 0)
    blit_id("player-down", 14 * 16 + 8, 6 * 16 + 14, 0)

    # 2x nearest
    out = Pix(vw * scale, vh * scale)
    for y in range(vh):
        for x in range(vw):
            o = (y * vw + x) * 4
            col = (world.data[o], world.data[o + 1], world.data[o + 2], world.data[o + 3])
            for dy in range(scale):
                for dx in range(scale):
                    out._set(x * scale + dx, y * scale + dy, col)
    out.save(PREVIEW_PATH)
    print("  wrote assets/preview.png (%dx%d)" % (out.w, out.h))


def main():
    ap = argparse.ArgumentParser(description="Export Moondrop Mountain pixel assets")
    ap.add_argument("--regen", action="store_true", help="rebuild built-in PNGs from this script")
    args = ap.parse_args()
    load_palette()
    builtins = builtin_sprites()
    sprites = merge_manifest(builtins)
    print("generating sprites (--regen=%s)" % args.regen)
    ensure_pngs(sprites, args.regen)
    print("packing atlas")
    atlas, out_sprites, atlas_map = pack_atlas(sprites)
    atlas.save(ATLAS_PNG)
    print("  wrote assets/atlas.png (%dx%d)" % (atlas.w, atlas.h))
    manifest = {
        "atlas": "atlas.png",
        "palette": C,
        "sprites": out_sprites,
    }
    MANIFEST_PATH.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print("  wrote assets/manifest.json")
    ATLAS_JSON.write_text(json.dumps({"image": "atlas.png", "sprites": atlas_map}, indent=2) + "\n", encoding="utf-8")
    print("  wrote assets/atlas.json")
    draw_preview(atlas_map, atlas, 2)
    print("done. %d sprites" % len(out_sprites))


if __name__ == "__main__":
    main()
