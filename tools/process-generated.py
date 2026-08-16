#!/usr/bin/env python3
"""Process IMAGE-GENERATOR PNGs into game-sized sprites.

Reads assets/generated-src/, chroma-keys magenta or grey/white checkerboard,
crops to the opaque bbox (+1px pad), nearest-neighbor scales to the sizes in
assets/manifest.json, and writes tiles/props/actors/ui.

Does not call the pixel painter and does not invoke export-assets.py --regen.
After this script, pack with:  python3 tools/export-assets.py
"""
from __future__ import annotations

import json
import struct
import sys
import zlib
from collections import deque
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
SRC = ASSETS / "generated-src"
MANIFEST_PATH = ASSETS / "manifest.json"

try:
    from PIL import Image as PILImage
except ImportError:
    PILImage = None


# ---------------------------------------------------------------------------
# Tiny PNG I/O (used when Pillow is missing)
# ---------------------------------------------------------------------------

def _crc32(data: bytes) -> int:
    return zlib.crc32(data) & 0xFFFFFFFF


def _paeth(a, b, c):
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
            w, h, bit_depth, color_type, _comp, _filt, inter = struct.unpack(">IIBBBBB", chunk)
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
                row[x] = (row[x] + _paeth(left, up, ul)) & 255
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
    return w, h, out


def write_png(path: Path, w: int, h: int, rgba) -> None:
    def chunk(tag: bytes, data: bytes) -> bytes:
        return struct.pack(">I", len(data)) + tag + data + struct.pack(">I", _crc32(tag + data))

    raw = b"".join(b"\x00" + bytes(rgba[y * w * 4 : (y + 1) * w * 4]) for y in range(h))
    ihdr = struct.pack(">IIBBBBB", w, h, 8, 6, 0, 0, 0)
    png = b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", ihdr) + chunk(b"IDAT", zlib.compress(raw, 9)) + chunk(b"IEND", b"")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(png)


class Pix:
    def __init__(self, w, h, data=None):
        self.w = w
        self.h = h
        if data is None:
            self.data = bytearray(w * h * 4)
        else:
            self.data = bytearray(data)

    @classmethod
    def load(cls, path: Path) -> "Pix":
        if PILImage is not None:
            im = PILImage.open(path).convert("RGBA")
            return cls(im.size[0], im.size[1], im.tobytes())
        w, h, rgba = read_png(path)
        return cls(w, h, rgba)

    def save(self, path: Path) -> None:
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        if PILImage is not None:
            im = PILImage.frombytes("RGBA", (self.w, self.h), bytes(self.data))
            im.save(path, "PNG")
            return
        write_png(path, self.w, self.h, self.data)

    def copy(self) -> "Pix":
        return Pix(self.w, self.h, self.data)

    def get(self, x, y):
        o = (y * self.w + x) * 4
        d = self.data
        return d[o], d[o + 1], d[o + 2], d[o + 3]

    def seta(self, x, y, a):
        self.data[(y * self.w + x) * 4 + 3] = a

    def flip_h(self) -> "Pix":
        out = Pix(self.w, self.h)
        for y in range(self.h):
            for x in range(self.w):
                src = (y * self.w + x) * 4
                dst = (y * self.w + (self.w - 1 - x)) * 4
                out.data[dst : dst + 4] = self.data[src : src + 4]
        return out

    def shift(self, dx, dy) -> "Pix":
        out = Pix(self.w, self.h)
        for y in range(self.h):
            sy = y - dy
            if sy < 0 or sy >= self.h:
                continue
            for x in range(self.w):
                sx = x - dx
                if sx < 0 or sx >= self.w:
                    continue
                so = (sy * self.w + sx) * 4
                do = (y * self.w + x) * 4
                out.data[do : do + 4] = self.data[so : so + 4]
        return out

    def wrap(self, dx, dy) -> "Pix":
        out = Pix(self.w, self.h)
        for y in range(self.h):
            sy = (y - dy) % self.h
            for x in range(self.w):
                sx = (x - dx) % self.w
                so = (sy * self.w + sx) * 4
                do = (y * self.w + x) * 4
                out.data[do : do + 4] = self.data[so : so + 4]
        return out

    def crop(self, x0, y0, x1, y1) -> "Pix":
        w = x1 - x0
        h = y1 - y0
        out = Pix(w, h)
        for y in range(h):
            sy = y0 + y
            if sy < 0 or sy >= self.h:
                continue
            for x in range(w):
                sx = x0 + x
                if sx < 0 or sx >= self.w:
                    continue
                so = (sy * self.w + sx) * 4
                do = (y * w + x) * 4
                out.data[do : do + 4] = self.data[so : so + 4]
        return out

    def opaque_bbox(self, pad=1):
        minx, miny = self.w, self.h
        maxx, maxy = -1, -1
        for y in range(self.h):
            row = y * self.w
            for x in range(self.w):
                if self.data[(row + x) * 4 + 3] > 8:
                    if x < minx:
                        minx = x
                    if y < miny:
                        miny = y
                    if x > maxx:
                        maxx = x
                    if y > maxy:
                        maxy = y
        if maxx < 0:
            return None
        x0 = max(0, minx - pad)
        y0 = max(0, miny - pad)
        x1 = min(self.w, maxx + 1 + pad)
        y1 = min(self.h, maxy + 1 + pad)
        return x0, y0, x1, y1

    def opaque_count(self):
        n = 0
        d = self.data
        for i in range(3, len(d), 4):
            if d[i] > 8:
                n += 1
        return n

    def nn_scale(self, tw, th) -> "Pix":
        """Stretch nearest-neighbor to exact tw x th."""
        out = Pix(tw, th)
        if self.w <= 0 or self.h <= 0:
            return out
        for y in range(th):
            sy = min(self.h - 1, (y * self.h) // th)
            for x in range(tw):
                sx = min(self.w - 1, (x * self.w) // tw)
                so = (sy * self.w + sx) * 4
                do = (y * tw + x) * 4
                out.data[do : do + 4] = self.data[so : so + 4]
        return out

    def fit_grounded(self, tw, th) -> "Pix":
        """Uniform NN scale to fit inside tw x th, pasted bottom-center."""
        if self.w <= 0 or self.h <= 0:
            return Pix(tw, th)
        # integer scale that fits
        # use max scale that keeps both axes inside
        # (src * s) / something; compute dest size
        scale_w = tw / self.w
        scale_h = th / self.h
        scale = min(scale_w, scale_h)
        nw = max(1, int(round(self.w * scale)))
        nh = max(1, int(round(self.h * scale)))
        nw = min(nw, tw)
        nh = min(nh, th)
        scaled = self.nn_scale(nw, nh)
        out = Pix(tw, th)
        ox = (tw - nw) // 2
        oy = th - nh  # ground to bottom
        for y in range(nh):
            for x in range(nw):
                so = (y * nw + x) * 4
                do = ((y + oy) * tw + (x + ox)) * 4
                out.data[do : do + 4] = scaled.data[so : so + 4]
        return out


# ---------------------------------------------------------------------------
# Chroma
# ---------------------------------------------------------------------------

def is_magenta(r, g, b, loose=False):
    """#FF00FF-ish, plus nearby pinks from the generator."""
    if loose:
        if g >= 130 or r < 140 or b < 130:
            return False
        return (r + b) / 2 - g >= 50
    if g >= 90 or r < 170 or b < 155:
        return False
    return (r + b) / 2 - g >= 85


def is_grey_white(r, g, b, loose=False):
    mx, mn = max(r, g, b), min(r, g, b)
    if loose:
        return mx >= 195 and (mx - mn) <= 32
    return mx >= 215 and (mx - mn) <= 22


def sample_border(pix, step=16):
    pts = []
    w, h = pix.w, pix.h
    for x in range(0, w, step):
        pts.append(pix.get(x, 0)[:3])
        pts.append(pix.get(x, h - 1)[:3])
    for y in range(0, h, step):
        pts.append(pix.get(0, y)[:3])
        pts.append(pix.get(w - 1, y)[:3])
    return pts


def detect_bg(pix):
    pts = sample_border(pix)
    mag = sum(1 for r, g, b in pts if is_magenta(r, g, b))
    gw = sum(1 for r, g, b in pts if is_grey_white(r, g, b))
    n = max(1, len(pts))
    if mag / n >= 0.45:
        return "magenta"
    if gw / n >= 0.45:
        return "checker"
    # weaker majority
    if mag > gw and mag / n >= 0.2:
        return "magenta"
    if gw > mag and gw / n >= 0.2:
        return "checker"
    return "unknown"


def key_match(kind, r, g, b, loose=False):
    if kind == "magenta":
        return is_magenta(r, g, b, loose=loose)
    if kind == "checker":
        return is_grey_white(r, g, b, loose=loose)
    return is_magenta(r, g, b, loose=loose) or is_grey_white(r, g, b, loose=loose)


def chroma_key(pix, kind):
    """Flood-fill from the border, then sweep leftover matching pixels."""
    w, h = pix.w, pix.h
    marked = bytearray(w * h)
    q = deque()

    def consider(x, y, loose):
        i = y * w + x
        if marked[i]:
            return
        r, g, b, a = pix.get(x, y)
        if a <= 8 or key_match(kind, r, g, b, loose=loose):
            marked[i] = 1
            q.append((x, y))

    for x in range(w):
        consider(x, 0, False)
        consider(x, h - 1, False)
    for y in range(h):
        consider(0, y, False)
        consider(w - 1, y, False)

    while q:
        x, y = q.popleft()
        for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
            if 0 <= nx < w and 0 <= ny < h:
                consider(nx, ny, False)

    # leftover islands that are clearly the same key color
    for y in range(h):
        for x in range(w):
            i = y * w + x
            if marked[i]:
                continue
            r, g, b, a = pix.get(x, y)
            if a > 8 and key_match(kind, r, g, b, loose=False):
                marked[i] = 1

    # fringe: opaque pixels next to keyed ones that are loosely bg
    extra = []
    for y in range(h):
        for x in range(w):
            i = y * w + x
            if marked[i]:
                continue
            r, g, b, a = pix.get(x, y)
            if a <= 8 or not key_match(kind, r, g, b, loose=True):
                continue
            for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                if 0 <= nx < w and 0 <= ny < h and marked[ny * w + nx]:
                    extra.append(i)
                    break
    for i in extra:
        marked[i] = 1

    keyed = 0
    for i, flag in enumerate(marked):
        if flag:
            pix.data[i * 4 + 3] = 0
            keyed += 1
    return keyed


# ---------------------------------------------------------------------------
# Pipeline
# ---------------------------------------------------------------------------

REPORT = []


def process_sprite(src_name, chroma=True, stretch=False):
    path = SRC / src_name
    if not path.exists():
        REPORT.append((src_name, "MISSING source", None, 0, 0))
        print("  FAIL missing", src_name)
        return None, "missing"
    pix = Pix.load(path)
    kind = "none"
    keyed = 0
    if chroma:
        kind = detect_bg(pix)
        keyed = chroma_key(pix, kind)
        frac = keyed / max(1, pix.w * pix.h)
        if kind == "unknown":
            REPORT.append((src_name, "chroma unknown (best-effort)", kind, keyed, frac))
        elif frac < 0.15:
            REPORT.append((src_name, "low chroma fraction %.2f" % frac, kind, keyed, frac))
        else:
            REPORT.append((src_name, "ok", kind, keyed, frac))
    else:
        REPORT.append((src_name, "no-chroma (full-bleed tile)", "none", 0, 0))

    if chroma:
        box = pix.opaque_bbox(pad=1)
        if box is None:
            REPORT.append((src_name, "FAIL empty after chroma", kind, keyed, 0))
            print("  FAIL empty after chroma", src_name)
            return None, "empty"
        pix = pix.crop(*box)
    return pix, kind


def emit(pix, rel, tw, th, stretch=False):
    if pix is None:
        return False
    out = pix.nn_scale(tw, th) if stretch else pix.fit_grounded(tw, th)
    dest = ASSETS / rel
    out.save(dest)
    print("  wrote %s (%dx%d) from %dx%d" % (rel, tw, th, pix.w, pix.h))
    return True


def tile_square(pix):
    """Center-crop full-bleed source to square, no chroma."""
    side = min(pix.w, pix.h)
    x0 = (pix.w - side) // 2
    y0 = (pix.h - side) // 2
    return pix.crop(x0, y0, x0 + side, y0 + side)


def main():
    print("process-generated: src=%s pillow=%s" % (SRC, PILImage is not None))
    if not SRC.exists():
        raise SystemExit("missing %s" % SRC)

    # --- tiles: full-bleed, no chroma ------------------------------------
    grass_src, _ = process_sprite("grass.png", chroma=False)
    dirt_src, _ = process_sprite("dirt.png", chroma=False)
    till_src, _ = process_sprite("till.png", chroma=False)
    water_src, _ = process_sprite("water.png", chroma=False)

    grass0 = tile_square(grass_src).nn_scale(16, 16) if grass_src else None
    if grass0:
        grass0.save(ASSETS / "tiles/grass0.png")
        grass0.wrap(8, 0).save(ASSETS / "tiles/grass1.png")
        grass0.wrap(0, 8).save(ASSETS / "tiles/grass2.png")
        grass0.wrap(8, 8).save(ASSETS / "tiles/grass3.png")
        print("  wrote tiles/grass0-3.png (16x16, wrap offsets)")
    if dirt_src:
        tile_square(dirt_src).nn_scale(16, 16).save(ASSETS / "tiles/dirt.png")
        print("  wrote tiles/dirt.png")
    if till_src:
        tile_square(till_src).nn_scale(16, 16).save(ASSETS / "tiles/till.png")
        print("  wrote tiles/till.png")
    if water_src:
        tile_square(water_src).nn_scale(16, 16).save(ASSETS / "tiles/water.png")
        print("  wrote tiles/water.png")

    # --- hero / props ----------------------------------------------------
    house, _ = process_sprite("house.png")
    emit(house, "props/house.png", 80, 80)

    tree, _ = process_sprite("tree.png")
    emit(tree, "props/tree.png", 48, 64)

    well, _ = process_sprite("well.png")
    emit(well, "props/well.png", 16, 32)

    pond, _ = process_sprite("pond.png")
    emit(pond, "props/pond.png", 36, 32)

    mailbox, _ = process_sprite("mailbox.png")
    emit(mailbox, "props/mailbox.png", 16, 24)

    crate, _ = process_sprite("crate.png")
    emit(crate, "props/crate.png", 16, 16)

    rock, _ = process_sprite("rock.png")
    if rock:
        emit(rock, "props/rock0.png", 16, 16)
        emit(rock.flip_h(), "props/rock1.png", 16, 16)

    weed, _ = process_sprite("weed.png")
    if weed:
        emit(weed, "props/weed0.png", 16, 16)
        emit(weed.flip_h(), "props/weed1.png", 16, 16)

    fence, _ = process_sprite("fence.png")
    if fence:
        emit(fence, "props/fenceH.png", 16, 16)
        mid = max(1, fence.w // 2)
        # left post + a bit of rail; right post + a bit of rail
        left = fence.crop(0, 0, mid + max(1, fence.w // 8), fence.h)
        right = fence.crop(mid - max(1, fence.w // 8), 0, fence.w, fence.h)
        emit(left, "props/fenceL.png", 16, 16)
        emit(right, "props/fenceR.png", 16, 16)

    seed, _ = process_sprite("seed.png")
    emit(seed, "ui/seed.png", 16, 16)

    sprout, _ = process_sprite("sprout.png")
    emit(sprout, "ui/sprout.png", 16, 16)

    # --- actors ----------------------------------------------------------
    def actor_pair(src_name, dest_stub, tw, th):
        pix, _ = process_sprite(src_name)
        if pix is None:
            return None
        f0 = pix.fit_grounded(tw, th)
        f1 = pix.shift(0, -max(1, pix.h // 80)).fit_grounded(tw, th)
        # if shift was tiny on source, also nudge the scaled frame 1px
        if f0.opaque_count() and f1.opaque_count() == f0.opaque_count():
            f1 = f0.shift(0, 1)
        f0.save(ASSETS / ("%s-0.png" % dest_stub))
        f1.save(ASSETS / ("%s-1.png" % dest_stub))
        print("  wrote %s-0/1.png (%dx%d)" % (dest_stub, tw, th))
        return f0, f1

    def flip_pair(frames, dest_stub):
        if not frames:
            return
        f0, f1 = frames
        f0.flip_h().save(ASSETS / ("%s-0.png" % dest_stub))
        f1.flip_h().save(ASSETS / ("%s-1.png" % dest_stub))
        print("  wrote %s-0/1.png (flip)" % dest_stub)

    pd = actor_pair("player-down.png", "actors/player-down", 16, 32)
    pu = actor_pair("player-up.png", "actors/player-up", 16, 32)
    pr = actor_pair("player-right.png", "actors/player-right", 16, 32)
    flip_pair(pr, "actors/player-left")

    nd = actor_pair("npc-down.png", "actors/npc-down", 16, 32)
    actor_pair("npc-right.png", "actors/npc-right", 16, 32)
    # npc-left from right
    nr0 = ASSETS / "actors/npc-right-0.png"
    if nr0.exists():
        r0 = Pix.load(nr0)
        r1 = Pix.load(ASSETS / "actors/npc-right-1.png")
        flip_pair((r0, r1), "actors/npc-left")
    # npc-up: reuse npc-down (no up source)
    if nd:
        nd[0].save(ASSETS / "actors/npc-up-0.png")
        nd[1].save(ASSETS / "actors/npc-up-1.png")
        print("  wrote actors/npc-up-0/1.png (from npc-down)")

    cr = actor_pair("chicken-right.png", "actors/chicken-right", 16, 16)
    flip_pair(cr, "actors/chicken-left")

    print("\n--- chroma/crop report ---")
    failed = []
    for name, status, kind, keyed, frac in REPORT:
        extra = ""
        if kind and kind != "none":
            extra = " key=%s keyed=%d (%.0f%%)" % (kind, keyed, (frac or 0) * 100)
        print("  %-18s %s%s" % (name, status, extra))
        if status.startswith("FAIL") or status.startswith("MISSING") or status.startswith("chroma unknown"):
            failed.append(name)
    if failed:
        print("issues:", ", ".join(failed))
    else:
        print("no chroma/crop failures")
    print("done")


if __name__ == "__main__":
    main()
