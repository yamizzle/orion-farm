"""Original deeper-mine props for Moondrop Mountain. Imported by export-assets."""
from __future__ import annotations


def install(ns):
    """Register hole, gem, chest, and moon-crystal generators."""
    Pix = ns["Pix"]
    C = ns["C"]
    GENERATORS = ns["GENERATORS"]

    def gen_hole():
        """Floor shaft down: darker pit, wood rim, down chevron. Not the up-ladder."""
        g = Pix(16, 24)
        dark = C.get("caveDark", "#14110E")
        mid = C.get("caveFloor", "#4A4840")
        hi = C["stoneHi"]
        sh = C["stoneSh"]
        wood = C["woodMid"]
        wood_hi = C["woodHi"]
        wood_sh = C["woodSh"]
        out = C["woodOut"]
        glow = C.get("lanternGlow", "#F0C060")
        # stone rim
        for y in range(4, 15):
            for x in range(1, 15):
                dx = (x - 8) / 6.2
                dy = (y - 9) / 4.4
                d = dx * dx + dy * dy
                if d < 1.18:
                    if d > 0.78:
                        g.px(x, y, hi if y < 9 else sh)
                    elif d > 0.42:
                        g.px(x, y, mid)
                    else:
                        g.px(x, y, dark)
        # deeper south lip
        for x in range(3, 13):
            g.px(x, 13, sh)
            g.px(x, 14, out)
        # wood frame posts
        g.fill(2, 5, 2, 10, wood)
        g.fill(2, 5, 1, 10, wood_hi)
        g.fill(3, 5, 1, 10, wood_sh)
        g.fill(12, 5, 2, 10, wood)
        g.fill(12, 5, 1, 10, wood_hi)
        g.fill(13, 5, 1, 10, wood_sh)
        g.fill(2, 5, 12, 2, wood)
        g.fill(2, 5, 12, 1, wood_hi)
        g.fill(2, 14, 12, 2, wood)
        g.fill(2, 15, 12, 1, wood_sh)
        # down chevron on a little plank
        g.fill(5, 16, 6, 6, wood)
        g.fill(5, 16, 6, 1, wood_hi)
        g.fill(5, 21, 6, 1, out)
        g.px(7, 17, glow)
        g.px(8, 17, glow)
        g.px(6, 18, glow)
        g.px(9, 18, glow)
        g.px(7, 19, glow)
        g.px(8, 19, glow)
        g.px(7, 20, glow)
        return g

    def gen_gem():
        """3/4 teal gem sitting on the cave floor."""
        g = Pix(16, 16)
        hi = C.get("roofTealHi", "#5CBC9A")
        mid = C.get("roofTeal", "#3A8A7A")
        sh = C.get("roofTealSh", "#1E5A4A")
        glow = C.get("moonGlow", "#E8F0FF")
        out = C["woodOut"]
        g.fill(4, 13, 8, 2, C.get("shadow", "rgba(20,16,12,0.40)"))
        # top facet
        g.px(7, 3, hi)
        g.px(8, 3, hi)
        g.fill(6, 4, 4, 1, hi)
        g.fill(5, 5, 6, 1, mid)
        g.px(6, 5, glow)
        g.px(8, 5, hi)
        # front
        g.fill(4, 6, 8, 5, mid)
        g.fill(4, 6, 2, 5, hi)
        g.fill(10, 6, 2, 5, sh)
        g.fill(5, 11, 6, 1, sh)
        g.px(3, 6, out)
        g.px(12, 6, out)
        g.px(4, 11, out)
        g.px(11, 11, out)
        g.px(7, 8, glow)
        g.px(8, 7, hi)
        return g

    def gen_chest():
        """Small 3/4 wood chest with a gold latch, lid slightly open."""
        g = Pix(16, 16)
        wood = C["woodMid"]
        wood_hi = C["woodHi"]
        wood_sh = C["woodSh"]
        out = C["woodOut"]
        gold = C.get("goldCoin", "#F0C040")
        gold_hi = C.get("goldCoinHi", "#F8E878")
        gold_sh = C.get("goldCoinSh", "#C47A18")
        glow = C.get("moonGlow", "#E8F0FF")
        g.fill(3, 14, 10, 2, C.get("shadow", "rgba(20,16,12,0.40)"))
        # body
        g.fill(3, 8, 10, 6, wood)
        g.fill(3, 8, 10, 1, wood_hi)
        g.fill(3, 13, 10, 1, wood_sh)
        g.fill(3, 8, 1, 6, wood_hi)
        g.fill(12, 8, 1, 6, wood_sh)
        g.px(2, 8, out)
        g.px(13, 8, out)
        g.fill(2, 14, 12, 1, out)
        # bands
        g.fill(3, 10, 10, 1, gold_sh)
        g.fill(7, 8, 2, 6, gold)
        g.px(7, 8, gold_hi)
        # lid, cracked open
        g.fill(3, 4, 10, 4, wood)
        g.fill(3, 4, 10, 1, wood_hi)
        g.fill(3, 7, 10, 1, gold)
        g.px(2, 4, out)
        g.px(13, 4, out)
        g.px(3, 3, wood_hi)
        g.px(12, 3, wood_sh)
        # glow in the gap
        g.px(7, 7, glow)
        g.px(8, 7, gold_hi)
        g.px(6, 7, glow)
        return g

    def gen_mooncrystal():
        """Cluster of moon crystals, bigger than the floor-1 shard."""
        g = Pix(16, 16)
        hi, mid, sh, glow = C["moonHi"], C["moonMid"], C["moonSh"], C["moonGlow"]
        out = C["woodOut"]
        g.fill(4, 14, 8, 2, C.get("shadow", "rgba(20,16,12,0.40)"))
        # left spike
        pts = [
            (5, 6, mid), (4, 7, mid), (5, 7, hi), (6, 7, mid),
            (4, 8, mid), (5, 8, hi), (6, 8, sh),
            (5, 9, sh), (6, 9, out),
        ]
        # tall center
        pts += [
            (8, 1, hi), (7, 2, hi), (8, 2, glow), (9, 2, mid),
            (7, 3, hi), (8, 3, glow), (9, 3, mid),
            (6, 4, mid), (7, 4, hi), (8, 4, glow), (9, 4, mid), (10, 4, sh),
            (6, 5, mid), (7, 5, hi), (8, 5, mid), (9, 5, sh), (10, 5, sh),
            (6, 6, mid), (7, 6, mid), (8, 6, sh), (9, 6, sh),
            (7, 7, mid), (8, 7, sh), (9, 7, out),
            (7, 8, sh), (8, 8, sh), (9, 8, out),
            (7, 9, sh), (8, 9, out),
            (8, 10, out),
        ]
        # right stub
        pts += [
            (11, 6, mid), (12, 6, sh),
            (11, 7, mid), (12, 7, sh), (13, 7, out),
            (11, 8, sh), (12, 8, out),
        ]
        for x, y, col in pts:
            g.px(x, y, col)
        # base
        g.fill(5, 11, 6, 2, mid)
        g.fill(5, 12, 6, 1, sh)
        g.px(5, 13, out)
        g.px(10, 13, out)
        g.px(8, 3, glow)
        return g

    extra_gen = {
        "hole": gen_hole,
        "gem": gen_gem,
        "chest": gen_chest,
        "mooncrystal": gen_mooncrystal,
    }
    GENERATORS.update(extra_gen)

    extra_sprites = [
        {"id": "hole", "file": "props/hole.png", "w": 16, "h": 24, "frames": 1, "anchor": [0, 0], "ox": 0, "oy": -8, "generated": True},
        {"id": "gem", "file": "ui/gem.png", "w": 16, "h": 16, "frames": 1, "anchor": [0, 0], "ox": 0, "oy": 0, "generated": True},
        {"id": "chest", "file": "props/chest.png", "w": 16, "h": 16, "frames": 1, "anchor": [0, 0], "ox": 0, "oy": 0, "generated": True},
        {"id": "mooncrystal", "file": "ui/mooncrystal.png", "w": 16, "h": 16, "frames": 1, "anchor": [0, 0], "ox": 0, "oy": 0, "generated": True},
    ]
    ns["MINE_SPRITES"] = extra_sprites
    return extra_sprites
