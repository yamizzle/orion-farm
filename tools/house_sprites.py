"""Lived-in house tiles and furniture for Moondrop Mountain.

Cream plaster + wood wainscot, night windows, flower boxes, fireplace,
writing desk, chair, and one corner plant. Imported by export-assets.
"""
from __future__ import annotations


def install(ns):
    Pix = ns["Pix"]
    C = ns["C"]
    GENERATORS = ns["GENERATORS"]

    NIGHT = "#1B2A4A"
    NIGHT_HI = "#2A3E68"
    NIGHT_DP = "#121A30"
    STAR = "#F8F0C8"
    MTN = "#2C3A4E"
    MTN_HI = "#3A4C64"
    FIRE_HI = "#F8E878"
    FIRE_MID = "#F0A040"
    FIRE_LO = "#C45A38"
    FIRE_EM = "#8B2E1C"
    PINK = C["blossom"]
    PINK_HI = "#F0C0C8"
    PURP = C["npcShirtHi"]
    PURP_DP = C["npcShirt"]

    def gen_inwall():
        """Cream/tan plaster with a low wood wainscot. Not the honey floor."""
        g = Pix(16, 16)
        g.fill(0, 0, 16, 10, C["plaster"])
        g.fill(0, 0, 16, 1, C["plasterHi"])
        g.fill(0, 1, 16, 1, C["plasterHi"])
        g.px(3, 3, C["plasterHi"])
        g.px(9, 2, C["plasterHi"])
        g.px(6, 5, C["plasterSh"])
        g.px(12, 4, C["plasterSh"])
        g.px(4, 7, C["plasterHi"])
        g.px(14, 6, C["plasterSh"])
        # timber posts at tile seams
        g.fill(0, 0, 1, 10, C["woodOut"])
        g.fill(1, 0, 1, 10, C["woodSh"])
        g.fill(15, 0, 1, 10, C["woodOut"])
        g.px(1, 1, C["woodHi"])
        # chair rail
        g.fill(0, 9, 16, 1, C["woodHi"])
        g.fill(0, 10, 16, 1, C["woodOut"])
        # wainscot panels
        g.fill(0, 11, 16, 4, C["woodMid"])
        g.fill(0, 11, 16, 1, C["woodSh"])
        g.fill(2, 12, 5, 2, C["woodSh"])
        g.fill(9, 12, 5, 2, C["woodSh"])
        g.px(3, 12, C["woodHi"])
        g.px(10, 12, C["woodHi"])
        g.fill(0, 11, 1, 4, C["woodOut"])
        g.fill(15, 11, 1, 4, C["woodOut"])
        g.fill(0, 15, 16, 1, C["woodOut"])
        return g

    def gen_window_night():
        """16x24 casement: night-blue mountain, stars. Shop keeps the day window."""
        g = Pix(16, 24)
        g.fill(1, 2, 14, 16, C["woodOut"])
        g.fill(2, 3, 12, 2, C["woodHi"])
        g.fill(2, 5, 12, 12, C["woodMid"])
        # night glass
        g.fill(3, 5, 10, 11, NIGHT)
        g.fill(3, 5, 10, 4, NIGHT_HI)
        # mountain peak (reads through both lower panes)
        g.fill(3, 12, 10, 4, MTN)
        g.px(4, 13, MTN_HI)
        g.px(5, 11, MTN)
        g.px(6, 10, MTN_HI)
        g.px(6, 11, MTN)
        g.px(10, 11, MTN)
        g.px(11, 10, MTN_HI)
        g.px(11, 11, MTN)
        g.px(12, 12, MTN)
        g.px(5, 14, NIGHT_DP)
        g.px(12, 14, NIGHT_DP)
        # stars
        g.px(4, 6, STAR)
        g.px(12, 6, STAR)
        g.px(5, 8, C["moonMid"])
        g.px(10, 7, STAR)
        # muntins
        g.fill(7, 5, 2, 11, C["woodOut"])
        g.fill(3, 9, 10, 2, C["woodOut"])
        g.px(4, 6, C["parch"])
        g.px(11, 6, C["parch"])
        # sill
        g.fill(0, 17, 16, 3, C["woodMid"])
        g.fill(0, 17, 16, 1, C["woodHi"])
        g.fill(0, 19, 16, 1, C["woodOut"])
        return g

    def gen_flowerbox():
        """16x16 wall-mounted box of purple/pink blooms. Sits under a window."""
        g = Pix(16, 16)
        # blooms rise into the top half so they tuck under the sill
        for x, y, col in (
            (3, 4, PINK), (4, 3, PINK_HI), (5, 4, PURP),
            (6, 2, PINK), (7, 3, PURP), (8, 2, PINK_HI),
            (9, 3, PINK), (10, 2, PURP), (11, 4, PINK_HI),
            (12, 3, PURP), (4, 5, PURP_DP), (8, 4, PURP_DP),
            (11, 5, PINK),
        ):
            g.px(x, y, col)
        for x, y in ((3, 6), (5, 5), (7, 5), (9, 5), (11, 6), (6, 4), (10, 4)):
            g.px(x, y, C["leaf"])
        g.px(4, 6, C["grassSh"])
        g.px(8, 6, C["grassSh"])
        g.px(12, 6, C["grassMid"])
        # box
        g.fill(1, 7, 14, 6, C["woodMid"])
        g.fill(1, 7, 14, 1, C["woodHi"])
        g.fill(1, 12, 14, 1, C["woodOut"])
        g.fill(1, 7, 1, 6, C["woodHi"])
        g.fill(14, 7, 1, 6, C["woodOut"])
        g.fill(3, 9, 4, 2, C["woodSh"])
        g.fill(9, 9, 4, 2, C["woodSh"])
        g.fill(2, 13, 12, 1, C["woodOut"])
        return g

    def _paint_fireplace(frame):
        """32x48 stone chimney + hearth. frame 0/1 swaps the fire."""
        g = Pix(32, 48)
        # chimney shaft
        g.fill(9, 0, 14, 18, C["stone"])
        g.fill(9, 0, 14, 1, C["stoneHi"])
        g.fill(9, 0, 1, 18, C["stoneHi"])
        g.fill(22, 0, 1, 18, C["stoneSh"])
        g.fill(9, 17, 14, 1, C["stoneSh"])
        # stone blocks on shaft
        for y in (2, 6, 10, 14):
            g.fill(10, y, 5, 1, C["stoneSh"])
            g.fill(16, y + 1, 5, 1, C["stoneSh"])
            g.px(11, y - 1, C["stoneHi"])
            g.px(18, y, C["stoneHi"])
        # mantel
        g.fill(3, 18, 26, 4, C["stone"])
        g.fill(3, 18, 26, 1, C["stoneHi"])
        g.fill(3, 21, 26, 1, C["woodOut"])
        g.fill(3, 18, 1, 4, C["stoneHi"])
        g.fill(28, 18, 1, 4, C["stoneSh"])
        # mantel bits: frame, plant, candle
        g.fill(6, 15, 3, 3, C["parch"])
        g.fill(6, 15, 3, 1, C["woodHi"])
        g.px(7, 16, C["leaf"])
        g.fill(15, 16, 2, 2, C["copperMid"])
        g.px(15, 15, C["leaf"])
        g.px(16, 14, C["grassHi"])
        g.fill(23, 16, 2, 2, C["parch"])
        g.px(23, 15, FIRE_MID)
        g.px(24, 14, FIRE_HI)
        # body
        g.fill(4, 22, 24, 20, C["stone"])
        g.fill(4, 22, 1, 20, C["stoneHi"])
        g.fill(27, 22, 1, 20, C["stoneSh"])
        g.fill(5, 24, 6, 1, C["stoneSh"])
        g.fill(18, 28, 7, 1, C["stoneSh"])
        g.fill(8, 34, 5, 1, C["stoneSh"])
        g.px(6, 26, C["stoneHi"])
        g.px(24, 32, C["stoneHi"])
        g.px(20, 36, C["stoneHi"])
        # hearth opening
        g.fill(8, 24, 16, 14, C["woodOut"])
        g.fill(9, 25, 14, 12, NIGHT_DP)
        g.fill(9, 34, 14, 3, "#2A1A10")
        # logs
        g.fill(10, 33, 12, 2, C["woodSh"])
        g.fill(11, 32, 10, 1, C["woodMid"])
        g.px(12, 32, C["woodHi"])
        g.fill(13, 34, 8, 1, C["woodOut"])
        # fire
        if frame == 0:
            g.fill(13, 28, 6, 5, FIRE_LO)
            g.fill(14, 27, 4, 5, FIRE_MID)
            g.fill(15, 26, 2, 4, FIRE_HI)
            g.px(16, 25, FIRE_HI)
            g.px(12, 30, FIRE_MID)
            g.px(19, 29, FIRE_LO)
        else:
            g.fill(12, 29, 8, 4, FIRE_LO)
            g.fill(13, 28, 6, 4, FIRE_MID)
            g.fill(14, 27, 3, 3, FIRE_HI)
            g.px(15, 26, FIRE_HI)
            g.px(18, 27, FIRE_MID)
            g.px(11, 31, FIRE_EM)
        g.px(14, 31, FIRE_EM)
        g.px(17, 32, FIRE_LO)
        # inner stone lip
        g.fill(8, 24, 16, 1, C["stoneSh"])
        g.fill(8, 24, 1, 14, C["stoneSh"])
        g.fill(23, 24, 1, 14, C["woodOut"])
        # base / hearth slab
        g.fill(3, 41, 26, 4, C["stone"])
        g.fill(3, 41, 26, 1, C["stoneHi"])
        g.fill(3, 44, 26, 1, C["woodOut"])
        g.fill(5, 45, 22, 2, C["shadow"])
        return g

    def gen_desk():
        """32x32 writing desk: drawer, open journal, quill, ink."""
        g = Pix(32, 32)
        g.fill(4, 29, 24, 3, C["shadow"])
        # top plane
        g.fill(3, 10, 26, 5, C["woodHi"])
        g.fill(4, 9, 24, 2, C["woodHi"])
        g.fill(6, 8, 20, 2, C["parch"])
        g.fill(3, 14, 26, 1, C["woodOut"])
        g.px(8, 11, C["woodMid"])
        g.px(20, 12, C["woodMid"])
        # right sliver
        g.fill(27, 10, 3, 5, C["woodSh"])
        g.fill(29, 10, 1, 5, C["woodOut"])
        # apron + drawer
        g.fill(3, 15, 24, 6, C["woodMid"])
        g.fill(3, 15, 24, 1, C["woodHi"])
        g.fill(3, 20, 24, 1, C["woodSh"])
        g.fill(3, 15, 1, 6, C["woodHi"])
        g.fill(26, 15, 1, 6, C["woodOut"])
        g.fill(27, 15, 3, 6, C["woodSh"])
        g.fill(8, 16, 16, 4, C["woodSh"])
        g.fill(8, 16, 16, 1, C["woodOut"])
        g.fill(15, 17, 2, 2, C["woodHi"])
        g.px(16, 18, C["flower"])
        # legs
        for x in (4, 23):
            g.fill(x, 21, 3, 8, C["woodMid"])
            g.fill(x, 21, 1, 8, C["woodHi"])
            g.fill(x + 2, 21, 1, 8, C["woodSh"])
            g.fill(x, 28, 3, 1, C["woodOut"])
        # open journal on the desktop
        g.fill(7, 7, 8, 5, C["parch"])
        g.fill(16, 7, 7, 5, C["parch"])
        g.fill(7, 7, 16, 1, C["woodHi"])
        g.fill(14, 7, 3, 5, C["woodMid"])
        g.fill(15, 8, 1, 3, C["woodOut"])
        g.px(9, 9, C["woodOut"])
        g.px(10, 9, C["woodSh"])
        g.px(9, 10, C["woodOut"])
        g.px(11, 10, C["woodSh"])
        g.px(18, 9, C["woodOut"])
        g.px(19, 9, C["woodSh"])
        g.px(18, 10, C["woodOut"])
        # quill + ink
        g.fill(24, 8, 2, 3, C["woodOut"])
        g.px(24, 7, C["parch"])
        g.px(25, 6, C["moonMid"])
        g.fill(26, 10, 2, 2, C["goldCoinSh"])
        g.px(26, 10, C["goldCoin"])
        return g

    def gen_chair():
        """16x24 pine chair, 3/4, facing the desk (north)."""
        g = Pix(16, 24)
        g.fill(3, 22, 10, 2, C["shadow"])
        # backrest (far)
        g.fill(3, 2, 10, 10, C["woodMid"])
        g.fill(3, 2, 10, 1, C["woodHi"])
        g.fill(3, 2, 1, 10, C["woodHi"])
        g.fill(12, 2, 1, 10, C["woodOut"])
        g.fill(5, 4, 2, 6, C["woodSh"])
        g.fill(9, 4, 2, 6, C["woodSh"])
        g.fill(3, 11, 10, 1, C["woodOut"])
        # seat
        g.fill(2, 12, 12, 4, C["woodHi"])
        g.fill(3, 11, 10, 2, C["parch"])
        g.fill(2, 15, 12, 1, C["woodOut"])
        g.fill(12, 12, 2, 4, C["woodSh"])
        # legs
        for x in (3, 11):
            g.fill(x, 16, 2, 6, C["woodMid"])
            g.fill(x, 16, 1, 6, C["woodHi"])
            g.fill(x, 21, 2, 1, C["woodOut"])
        return g

    def gen_house_plant():
        """16x24 terracotta pot with a leafy houseplant."""
        g = Pix(16, 24)
        g.fill(4, 22, 8, 2, C["shadow"])
        # leaves
        g.px(7, 2, C["grassHi"])
        g.px(8, 1, C["leaf"])
        g.fill(5, 4, 6, 6, C["leaf"])
        g.fill(4, 6, 3, 5, C["grassMid"])
        g.fill(9, 5, 4, 6, C["grassMid"])
        g.px(6, 3, C["grassHi"])
        g.px(10, 3, C["grassHi"])
        g.px(3, 8, C["leaf"])
        g.px(12, 7, C["grassHi"])
        g.px(8, 4, C["grassHi"])
        g.px(5, 9, C["grassSh"])
        g.px(11, 10, C["grassSh"])
        # pot
        g.fill(5, 13, 6, 8, C["copperMid"])
        g.fill(4, 13, 8, 2, C["copperHi"])
        g.fill(5, 19, 6, 1, C["copperSh"])
        g.fill(6, 20, 4, 1, C["copperSh"])
        g.fill(4, 13, 1, 7, C["copperHi"])
        g.fill(11, 13, 1, 7, C["copperSh"])
        g.fill(5, 21, 6, 1, C["woodOut"])
        return g

    def gen_workbench():
        """32x32 3/4 crafting table: thick pine top, pegs, tools on the slab."""
        g = Pix(32, 32)
        steel = C.get("steel", "#C8D0D8")
        steel_hi = C.get("steelHi", "#E8F0F4")
        steel_sh = C.get("steelSh", "#6A7888")
        g.fill(3, 29, 26, 3, C["shadow"])
        # top plane
        g.fill(2, 8, 26, 6, C["woodHi"])
        g.fill(3, 7, 24, 2, C["parch"])
        g.fill(5, 6, 20, 2, C["woodHi"])
        g.fill(2, 13, 26, 1, C["woodOut"])
        g.px(7, 9, C["woodMid"])
        g.px(16, 10, C["woodMid"])
        g.px(22, 8, C["woodMid"])
        # right sliver
        g.fill(26, 8, 4, 6, C["woodSh"])
        g.fill(29, 8, 1, 6, C["woodOut"])
        # apron + peg rack
        g.fill(2, 14, 24, 7, C["woodMid"])
        g.fill(2, 14, 24, 1, C["woodHi"])
        g.fill(2, 20, 24, 1, C["woodSh"])
        g.fill(2, 14, 1, 7, C["woodHi"])
        g.fill(25, 14, 1, 7, C["woodOut"])
        g.fill(26, 14, 4, 7, C["woodSh"])
        g.fill(29, 14, 1, 7, C["woodOut"])
        g.fill(5, 16, 18, 3, C["woodSh"])
        g.fill(5, 16, 18, 1, C["woodOut"])
        for x in (7, 12, 17, 21):
            g.px(x, 17, C["woodHi"])
            g.px(x, 18, C["woodOut"])
        # legs
        for x in (3, 22):
            g.fill(x, 21, 4, 8, C["woodMid"])
            g.fill(x, 21, 1, 8, C["woodHi"])
            g.fill(x + 3, 21, 1, 8, C["woodSh"])
            g.fill(x, 28, 4, 1, C["woodOut"])
        # stone slab inset
        g.fill(6, 9, 8, 3, C["stone"])
        g.fill(6, 9, 8, 1, C["stoneHi"])
        g.fill(6, 11, 8, 1, C["stoneSh"])
        g.px(5, 9, C["woodOut"])
        g.px(14, 9, C["woodOut"])
        # tiny mallet on the right
        g.fill(20, 5, 2, 4, C["woodMid"])
        g.px(20, 5, C["woodHi"])
        g.fill(18, 4, 6, 2, C["stone"])
        g.fill(18, 4, 6, 1, C["stoneHi"])
        g.px(17, 4, C["woodOut"])
        g.px(24, 4, C["woodOut"])
        # saw / plank
        g.fill(16, 10, 8, 1, steel)
        g.px(16, 10, steel_hi)
        g.px(23, 10, steel_sh)
        g.px(24, 10, C["woodOut"])
        return g

    def gen_axe():
        """16x16 stone axe, 3/4, dark-brown outline."""
        g = Pix(16, 16)
        out = C["woodOut"]
        g.fill(3, 14, 9, 2, C["shadow"])
        # handle
        g.fill(6, 5, 2, 9, C["woodMid"])
        g.fill(6, 5, 1, 9, C["woodHi"])
        g.fill(7, 8, 1, 4, C["woodSh"])
        g.fill(6, 13, 2, 1, out)
        # stone head
        g.fill(3, 2, 8, 4, C["stone"])
        g.fill(3, 2, 8, 1, C["stoneHi"])
        g.fill(3, 5, 8, 1, C["stoneSh"])
        g.fill(2, 3, 2, 2, C["stoneHi"])
        g.fill(10, 3, 2, 2, C["stoneSh"])
        g.px(2, 2, out)
        g.px(11, 2, out)
        g.px(1, 3, out)
        g.px(12, 4, out)
        g.px(4, 1, out)
        g.px(8, 1, out)
        g.px(5, 6, out)
        g.px(8, 6, out)
        return g

    def gen_pickaxe():
        """16x16 stone pickaxe, pointed head."""
        g = Pix(16, 16)
        out = C["woodOut"]
        g.fill(4, 14, 8, 2, C["shadow"])
        g.fill(7, 5, 2, 9, C["woodMid"])
        g.fill(7, 5, 1, 9, C["woodHi"])
        g.fill(8, 9, 1, 3, C["woodSh"])
        g.fill(7, 13, 2, 1, out)
        # pointed head
        g.fill(4, 3, 8, 3, C["stone"])
        g.fill(4, 3, 8, 1, C["stoneHi"])
        g.fill(2, 4, 3, 2, C["stoneHi"])
        g.fill(11, 4, 3, 2, C["stoneSh"])
        g.px(1, 5, C["stoneHi"])
        g.px(14, 5, C["stoneSh"])
        g.px(3, 2, out)
        g.px(12, 2, out)
        g.px(0, 5, out)
        g.px(15, 5, out)
        g.px(6, 6, out)
        g.px(9, 6, out)
        return g

    def gen_shield():
        """16x16 round wood shield with a steel boss."""
        g = Pix(16, 16)
        steel = C.get("steel", "#C8D0D8")
        steel_hi = C.get("steelHi", "#E8F0F4")
        steel_sh = C.get("steelSh", "#6A7888")
        out = C["woodOut"]
        g.fill(3, 14, 10, 2, C["shadow"])
        for y in range(1, 15):
            for x in range(1, 15):
                dx = x - 7.5
                dy = y - 7.5
                d = dx * dx + dy * dy
                if d <= 42:
                    if d > 34:
                        g.px(x, y, out)
                    elif y < 6:
                        g.px(x, y, C["woodHi"])
                    elif y > 10:
                        g.px(x, y, C["woodSh"])
                    else:
                        g.px(x, y, C["woodMid"])
        g.fill(6, 6, 4, 4, steel)
        g.fill(6, 6, 4, 1, steel_hi)
        g.fill(6, 9, 4, 1, steel_sh)
        g.px(6, 6, steel_hi)
        g.px(9, 9, steel_sh)
        g.px(7, 7, C["parch"])
        return g

    def gen_iron_sword():
        """16x16 iron sword: cooler steel blade, darker grip."""
        g = Pix(16, 16)
        steel = C.get("steel", "#C8D0D8")
        steel_hi = C.get("steelHi", "#E8F0F4")
        steel_sh = C.get("steelSh", "#6A7888")
        gold = C.get("lanternGlow", "#F0C060")
        gold_sh = C.get("honeySh", "#A86C14")
        out = C["woodOut"]
        g.fill(4, 13, 8, 2, C["shadow"])
        g.fill(8, 0, 2, 9, steel)
        g.px(8, 0, steel_hi)
        g.px(9, 0, steel)
        g.fill(7, 1, 1, 8, steel_hi)
        g.fill(10, 1, 1, 8, steel_sh)
        g.px(9, 0, steel_hi)
        g.px(7, 0, out)
        g.px(10, 0, out)
        g.px(11, 2, out)
        g.fill(4, 8, 8, 2, steel)
        g.fill(4, 8, 8, 1, steel_hi)
        g.fill(4, 9, 8, 1, steel_sh)
        g.px(3, 8, out)
        g.px(12, 8, out)
        g.fill(7, 10, 2, 4, C["woodSh"])
        g.px(7, 10, C["woodMid"])
        g.px(8, 12, out)
        g.fill(6, 14, 4, 1, gold)
        g.px(6, 14, gold_sh)
        g.px(9, 14, out)
        return g

    def gen_bow():
        """16x16 wooden bow, 3/4, string taut."""
        g = Pix(16, 16)
        out = C["woodOut"]
        string = C.get("parch", "#F3D2A3")
        g.fill(4, 14, 8, 2, C["shadow"])
        # limb
        g.px(10, 1, C["woodHi"])
        g.px(11, 2, C["woodHi"])
        g.fill(11, 3, 2, 3, C["woodMid"])
        g.fill(10, 6, 2, 4, C["woodMid"])
        g.fill(11, 10, 2, 3, C["woodMid"])
        g.px(11, 13, C["woodSh"])
        g.px(10, 14, C["woodSh"])
        g.px(12, 3, C["woodSh"])
        g.px(12, 12, C["woodSh"])
        g.px(9, 1, out)
        g.px(12, 2, out)
        g.px(13, 4, out)
        g.px(13, 11, out)
        g.px(12, 13, out)
        g.px(9, 14, out)
        # grip
        g.fill(9, 7, 2, 3, C["woodSh"])
        g.px(9, 8, C["woodHi"])
        # string
        g.px(5, 2, string)
        g.px(4, 4, string)
        g.px(4, 6, string)
        g.px(4, 8, string)
        g.px(4, 10, string)
        g.px(4, 12, string)
        g.px(5, 13, string)
        return g

    def gen_arrow():
        """16x16 short arrow, shaft pointing right."""
        g = Pix(16, 16)
        steel = C.get("steel", "#C8D0D8")
        steel_hi = C.get("steelHi", "#E8F0F4")
        out = C["woodOut"]
        # shaft
        g.fill(2, 7, 10, 2, C["woodMid"])
        g.fill(2, 7, 10, 1, C["woodHi"])
        g.fill(2, 8, 10, 1, C["woodSh"])
        # tip
        g.fill(11, 6, 3, 4, C["stone"])
        g.fill(11, 6, 3, 1, C["stoneHi"])
        g.px(14, 7, C["stoneHi"])
        g.px(14, 8, C["stone"])
        g.px(15, 7, out)
        g.px(13, 5, out)
        g.px(13, 10, out)
        # fletching
        g.px(1, 6, C["blossom"])
        g.px(2, 6, C["blossom"])
        g.px(1, 9, C["npcShirt"])
        g.px(2, 9, C["npcShirt"])
        g.px(0, 7, C["parch"])
        g.px(0, 8, C["parch"])
        return g

    GENERATORS["inwall"] = gen_inwall
    GENERATORS.update({
        "windowNight": gen_window_night,
        "flowerbox": gen_flowerbox,
        "fireplace-0": lambda: _paint_fireplace(0),
        "fireplace-1": lambda: _paint_fireplace(1),
        "desk": gen_desk,
        "chair": gen_chair,
        "housePlant": gen_house_plant,
        "workbench": gen_workbench,
        "axe": gen_axe,
        "pickaxe": gen_pickaxe,
        "shield": gen_shield,
        "ironSword": gen_iron_sword,
        "bow": gen_bow,
        "arrow": gen_arrow,
    })

    extra_sprites = [
        {"id": "windowNight", "file": "props/windowNight.png", "w": 32, "h": 40, "frames": 1, "anchor": [0, 0], "ox": -8, "oy": 0, "generated": True},
        {"id": "flowerbox", "file": "props/flowerbox.png", "w": 32, "h": 16, "frames": 1, "anchor": [0, 0], "ox": -8, "oy": 0, "generated": True},
        {"id": "fireplace", "file": "props/fireplace-{n}.png", "w": 48, "h": 64, "frames": 2, "anchor": [0, 0], "ox": 0, "oy": -16, "generated": True},
        {"id": "desk", "file": "props/desk.png", "w": 64, "h": 48, "frames": 1, "anchor": [0, 0], "ox": 0, "oy": 0, "generated": True},
        {"id": "houseLamp", "file": "props/houseLamp.png", "w": 16, "h": 32, "frames": 1, "anchor": [0, 0], "ox": 0, "oy": -16},
        {"id": "chair", "file": "props/chair.png", "w": 16, "h": 24, "frames": 1, "anchor": [0, 0], "ox": 0, "oy": -8, "generated": True},
        {"id": "housePlant", "file": "props/housePlant.png", "w": 16, "h": 24, "frames": 1, "anchor": [0, 0], "ox": 0, "oy": -8, "generated": True},
        {"id": "workbench", "file": "props/workbench.png", "w": 32, "h": 32, "frames": 1, "anchor": [0, 0], "ox": 0, "oy": -8, "generated": True},
        {"id": "axe", "file": "ui/axe.png", "w": 16, "h": 16, "frames": 1, "anchor": [0, 0], "ox": 0, "oy": 0, "generated": True},
        {"id": "pickaxe", "file": "ui/pickaxe.png", "w": 16, "h": 16, "frames": 1, "anchor": [0, 0], "ox": 0, "oy": 0, "generated": True},
        {"id": "shield", "file": "ui/shield.png", "w": 16, "h": 16, "frames": 1, "anchor": [0, 0], "ox": 0, "oy": 0, "generated": True},
        {"id": "ironSword", "file": "ui/ironSword.png", "w": 16, "h": 16, "frames": 1, "anchor": [0, 0], "ox": 0, "oy": 0, "generated": True},
        {"id": "bow", "file": "ui/bow.png", "w": 16, "h": 16, "frames": 1, "anchor": [0, 0], "ox": 0, "oy": 0, "generated": True},
        {"id": "arrow", "file": "ui/arrow.png", "w": 16, "h": 16, "frames": 1, "anchor": [0, 0], "ox": 0, "oy": 0, "generated": True},
    ]
    ns["HOUSE_SPRITES"] = extra_sprites
    return extra_sprites
