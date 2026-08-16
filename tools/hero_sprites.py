"""Imaginative 16-bit hero and key-prop sprites for Moondrop Mountain.

Orion, Junie (neighbor), Nim (asset only), moon-kid statue, moon shard,
and the mountain heart. Imported by export-assets. Does not place Nim.
"""
from __future__ import annotations


def install(ns):
    Pix = ns["Pix"]
    C = ns["C"]
    GENERATORS = ns["GENERATORS"]

    def G(name, fallback):
        return C.get(name, fallback)

    # --- shared kid-safe palette -----------------------------------------
    SKIN = G("skin", "#F0C090")
    SKIN_SH = G("skinSh", "#D4A06A")
    OUT = G("woodOut", "#3D1A0C")
    SHADOW = G("shadow", "rgba(30,90,18,0.40)")
    CHEEK = G("blossom", "#E8A0A8")
    LIP = G("playerLip", "#C47A38")
    PARCH = G("parch", "#F3D2A3")
    GOLD = G("flower", "#E8C84A")
    GOLD_HI = G("parch", "#F3D2A3")
    GOLD_SH = G("honeySh", "#A86C14")
    MOON_HI = G("moonHi", "#F8F0C8")
    MOON_MID = G("moonMid", "#C8D8F0")
    MOON_SH = G("moonSh", "#6A88C0")
    MOON_GLOW = G("moonGlow", "#E8F0FF")
    LEAF = G("leaf", "#4A9A28")
    HAT = G("npcHat", "#E8C84A")
    HAT_HI = G("npcHatHi", "#F0D878")
    HAT_SH = G("npcHatSh", "#A86C14")
    HAT_BAND = G("npcHatBand", "#C45A38")

    # Orion — farm kid with a moon pin and a tiny starry scarf
    ORION = {
        "hair": G("playerHair", "#6B3A22"),
        "hairHi": G("playerHairHi", "#8B5A38"),
        "eye": G("playerEye", "#2A4A38"),
        "eyeHi": G("playerEyeHi", "#5CBC88"),
        "shirt": G("playerShirt", "#3D8C9C"),
        "shirtHi": G("playerShirtHi", "#6CB8C4"),
        "shirtSh": G("playerShirtSh", "#246070"),
        "pants": G("playerPants", "#4A5A28"),
        "pantsSh": G("playerPantsSh", "#2E3A18"),
        "shoe": G("playerShoe", "#5A2E18"),
        "scarf": "#2A2458",
        "scarfHi": "#5A4A98",
        "scarfSh": "#181430",
        "moon": MOON_HI,
    }

    # Junie — kind gardener, straw hat, someone a kid would trust
    JUNIE = {
        "hair": "#C48A48",
        "hairHi": "#E0B060",
        "eye": "#3A4A62",
        "eyeHi": "#8AB0C8",
        "shirt": "#3A8A58",
        "shirtHi": "#5CBC78",
        "shirtSh": "#246438",
        "pants": "#5A4A30",
        "pantsSh": "#3A2E20",
        "shoe": "#4A2814",
        "apron": PARCH,
        "apronSh": "#D4B078",
    }

    # Nim — shy moon-kid, starry cloak, small lantern
    NIM = {
        "hair": "#D8D0E8",
        "hairHi": "#F4EEF8",
        "eye": "#3A2A58",
        "eyeHi": "#A8C0F0",
        "shirt": "#6A7AB0",
        "shirtHi": "#8A9AD0",
        "shirtSh": "#3A4A78",
        "pants": "#3A3A58",
        "pantsSh": "#242438",
        "shoe": "#2A2238",
        "cloak": "#2A2A58",
        "cloakHi": "#4A4A88",
        "cloakSh": "#181838",
        "star": GOLD,
    }

    def _legs(g, p, face, fr):
        if face in ("down", "up"):
            g.fill(4, 23 + fr, 3, 5, p["pants"])
            g.fill(4, 28 + fr, 3, 2, p["shoe"])
            g.fill(9, 23 - fr, 3, 5, p["pantsSh"] if face == "up" else p["pants"])
            g.fill(9, 28 - fr, 3, 2, p["shoe"])
            g.px(4, 23 + fr, p["pantsSh"])
            g.px(11, 23 - fr, p["pantsSh"])
        else:
            g.fill(6, 23 + fr, 3, 5, p["pantsSh"])
            g.fill(6, 28 + fr, 3, 2, p["shoe"])
            g.fill(8, 23 - fr, 3, 5, p["pants"])
            g.fill(8, 28 - fr, 3, 2, p["shoe"])

    def _torso_box(g, p, face, fr, extra=None):
        extra = extra or {}
        if face == "down":
            g.fill(4, 13, 8, 10, p["shirt"])
            g.fill(4, 13, 8, 1, p["shirtHi"])
            g.fill(4, 13, 1, 10, p["shirtHi"])
            g.fill(11, 13, 1, 10, p["shirtSh"])
            g.fill(2, 14, 2, 6, p["shirt"])
            g.fill(12, 14, 2, 6, p["shirt"])
            g.fill(2, 19, 2, 2, SKIN)
            g.fill(12, 19, 2, 2, SKIN)
            if extra.get("apron"):
                g.fill(5, 16, 6, 6, extra["apron"])
                g.fill(5, 16, 6, 1, PARCH)
                g.fill(5, 21, 6, 1, extra.get("apronSh", extra["apron"]))
        elif face == "up":
            g.fill(4, 13, 8, 10, p["shirtSh"])
            g.fill(4, 13, 8, 1, p["shirt"])
            g.fill(2, 14, 2, 6, p["shirtSh"])
            g.fill(12, 14, 2, 6, p["shirtSh"])
            g.fill(2, 19, 2, 2, SKIN)
            g.fill(12, 19, 2, 2, SKIN)
        else:
            g.fill(5, 13, 6, 10, p["shirt"])
            g.fill(5, 13, 6, 1, p["shirtHi"])
            g.fill(10, 13, 1, 10, p["shirtSh"])
            g.fill(10, 14 + fr, 2, 6, p["shirt"])
            g.fill(10, 20 + fr, 2, 2, SKIN)
            if extra.get("apron"):
                g.fill(6, 16, 4, 6, extra["apron"])

    def _head_down(g, p, bangs=True):
        g.fill(3, 3, 10, 8, p["hair"])
        g.fill(4, 2, 8, 2, p["hair"])
        g.fill(4, 5, 8, 6, SKIN)
        g.fill(5, 4, 6, 1, SKIN)
        g.fill(4, 10, 8, 1, SKIN_SH)
        if bangs:
            g.fill(4, 3, 8, 2, p["hair"])
            g.fill(4, 3, 2, 3, p["hair"])
            g.fill(10, 3, 2, 3, p["hair"])
        g.fill(5, 2, 6, 1, p["hairHi"])
        g.px(5, 7, p["eye"])
        g.px(6, 7, p["eyeHi"])
        g.px(9, 7, p["eye"])
        g.px(10, 7, p["eyeHi"])
        g.px(4, 8, CHEEK)
        g.px(11, 8, CHEEK)
        g.px(7, 9, SKIN_SH)
        g.px(8, 10, LIP)
        g.px(3, 7, SKIN)
        g.px(12, 7, SKIN)
        g.fill(6, 11, 4, 2, SKIN)
        g.px(3, 2, OUT)
        g.px(12, 2, OUT)

    def _head_up(g, p):
        g.fill(3, 3, 10, 8, p["hair"])
        g.fill(4, 2, 8, 2, p["hairHi"])
        g.fill(3, 4, 10, 7, p["hair"])
        g.fill(6, 11, 4, 2, p["hair"])
        g.px(3, 7, SKIN)
        g.px(12, 7, SKIN)

    def _head_side(g, p):
        g.fill(3, 3, 9, 8, p["hair"])
        g.fill(4, 2, 7, 2, p["hair"])
        g.fill(5, 5, 6, 6, SKIN)
        g.fill(5, 4, 5, 1, SKIN)
        g.fill(3, 3, 3, 8, p["hair"])
        g.fill(4, 2, 2, 2, p["hairHi"])
        g.px(8, 7, p["eye"])
        g.px(9, 7, p["eyeHi"])
        g.px(10, 8, SKIN_SH)
        g.px(10, 9, CHEEK)
        g.px(9, 10, LIP)
        g.fill(7, 11, 3, 2, SKIN)

    def _hat(g, face, flower=True):
        if face == "up":
            g.fill(5, 0, 6, 4, HAT)
            g.fill(5, 0, 6, 1, HAT_HI)
            g.fill(2, 3, 12, 2, HAT)
            g.fill(1, 4, 14, 1, HAT_SH)
        elif face == "down":
            g.fill(5, 0, 6, 3, HAT)
            g.fill(5, 0, 6, 1, HAT_HI)
            g.fill(5, 2, 6, 1, HAT_BAND)
            g.fill(2, 3, 12, 2, HAT)
            g.fill(1, 4, 14, 1, HAT_SH)
            if flower:
                g.px(12, 2, CHEEK)
                g.px(13, 2, GOLD)
                g.px(12, 1, LEAF)
        else:
            g.fill(4, 0, 7, 3, HAT)
            g.fill(4, 0, 7, 1, HAT_HI)
            g.fill(4, 2, 7, 1, HAT_BAND)
            g.fill(2, 3, 11, 2, HAT)
            g.fill(1, 4, 13, 1, HAT_SH)
            if flower:
                g.px(11, 1, CHEEK)
                g.px(12, 1, GOLD)
                g.px(11, 0, LEAF)

    def gen_orion(face, frame):
        """7-year-old farm kid: brown cowlick, teal shirt, moon pin, starry scarf."""
        g = Pix(16, 32)
        p = ORION
        fr = 1 if frame else 0
        g.fill(3, 30, 10, 2, SHADOW)
        _legs(g, p, face, fr)
        _torso_box(g, p, face, fr)
        if face == "down":
            # starry scarf / tiny capelet, darker than the teal shirt
            g.fill(3, 13, 10, 3, p["scarf"])
            g.fill(3, 13, 10, 1, p["scarfHi"])
            g.px(2, 14, p["scarf"])
            g.px(13, 14, p["scarfSh"] if "scarfSh" in p else p["scarf"])
            g.px(5, 14, GOLD)
            g.px(10, 14, MOON_GLOW)
            g.px(8, 15, GOLD_HI)
            # cream moon pin
            g.px(7, 18, p["moon"])
            g.px(8, 18, MOON_MID)
            g.px(7, 19, MOON_MID)
            g.px(8, 19, p["shirtHi"])
            _head_down(g, p)
            # cowlick
            g.px(5, 1, p["hair"])
            g.px(4, 0, p["hairHi"])
            g.px(6, 1, p["hairHi"])
        elif face == "up":
            g.fill(2, 13, 12, 4, p["scarf"])
            g.fill(2, 13, 12, 1, p["scarfHi"])
            g.px(4, 15, GOLD)
            g.px(9, 16, MOON_GLOW)
            g.px(7, 14, GOLD_HI)
            g.px(11, 15, p["star"] if "star" in p else GOLD)
            _head_up(g, p)
            g.px(5, 1, p["hairHi"])
            g.px(4, 0, p["hair"])
        else:
            g.fill(5, 13, 6, 3, p["scarf"])
            g.fill(3, 14, 3, 4, p["scarf"])
            g.px(4, 15, GOLD)
            g.px(6, 13, MOON_GLOW)
            g.px(8, 18, p["moon"])
            _head_side(g, p)
            g.px(4, 1, p["hairHi"])
            g.px(3, 0, p["hair"])
        return g

    def gen_junie(face, frame):
        """Kind gardener neighbor: straw hat with a daisy, apron, warm smile."""
        g = Pix(16, 32)
        p = JUNIE
        fr = 1 if frame else 0
        g.fill(3, 30, 10, 2, SHADOW)
        _legs(g, p, face, fr)
        extra = {"apron": p["apron"], "apronSh": p["apronSh"]}
        _torso_box(g, p, face, fr, extra)
        if face == "down":
            _head_down(g, p)
            # freckles + kinder smile
            g.px(5, 9, SKIN_SH)
            g.px(10, 9, SKIN_SH)
            g.px(7, 10, LIP)
            g.px(8, 10, LIP)
            # seed pouch on apron
            g.fill(6, 18, 4, 3, p["apronSh"])
            g.px(7, 19, LEAF)
            g.px(8, 19, GOLD)
            _hat(g, "down", flower=True)
            # honey hair peeking
            g.px(3, 5, p["hair"])
            g.px(12, 5, p["hairHi"])
        elif face == "up":
            _head_up(g, p)
            _hat(g, "up", flower=False)
            g.px(3, 6, p["hair"])
            g.px(12, 6, p["hair"])
        else:
            _head_side(g, p)
            _hat(g, "right", flower=True)
            g.px(3, 6, p["hairHi"])
        return g

    def _lantern(g, x, y, frame):
        glow = GOLD if frame else GOLD_HI
        g.px(x, y, OUT)
        g.px(x + 1, y, OUT)
        g.fill(x - 1, y + 1, 4, 4, OUT)
        g.fill(x, y + 2, 2, 2, glow)
        g.px(x, y + 2, PARCH)
        g.px(x + 1, y + 3, GOLD_SH)
        g.px(x, y + 5, OUT)
        if frame:
            g.px(x - 1, y + 1, GOLD_HI)
            g.px(x + 2, y + 1, GOLD)

    def gen_nim(face, frame):
        """Shy moon-kid: silver hair, starry cloak, small lantern. Asset only."""
        g = Pix(16, 32)
        p = NIM
        fr = 1 if frame else 0
        g.fill(3, 30, 10, 2, G("shadow", "rgba(20,16,40,0.45)"))
        _legs(g, p, face, fr)
        _torso_box(g, p, face, fr)
        if face == "down":
            # cloak over shoulders
            g.fill(2, 13, 12, 8, p["cloak"])
            g.fill(2, 13, 12, 1, p["cloakHi"])
            g.fill(2, 13, 1, 8, p["cloakHi"])
            g.fill(13, 13, 1, 8, p["cloakSh"])
            g.px(4, 15, p["star"])
            g.px(11, 16, MOON_GLOW)
            g.px(7, 18, p["star"])
            # shy face, smaller eyes
            g.fill(3, 3, 10, 8, p["hair"])
            g.fill(4, 2, 8, 2, p["hairHi"])
            g.fill(4, 5, 8, 6, SKIN)
            g.fill(5, 4, 6, 1, SKIN)
            g.fill(4, 3, 8, 2, p["hair"])
            g.fill(4, 10, 8, 1, SKIN_SH)
            g.px(5, 7, p["eye"])
            g.px(6, 7, p["eyeHi"])
            g.px(9, 7, p["eye"])
            g.px(10, 7, p["eyeHi"])
            g.px(4, 8, CHEEK)
            g.px(11, 8, CHEEK)
            g.px(8, 10, LIP)
            g.fill(6, 11, 4, 2, SKIN)
            # hood
            g.fill(3, 1, 10, 3, p["cloak"])
            g.fill(4, 0, 8, 2, p["cloakHi"])
            g.px(5, 1, p["star"])
            g.px(10, 2, MOON_GLOW)
            _lantern(g, 1, 18 + fr, frame)
        elif face == "up":
            g.fill(2, 12, 12, 10, p["cloak"])
            g.fill(2, 12, 12, 1, p["cloakHi"])
            g.px(4, 14, p["star"])
            g.px(8, 16, MOON_GLOW)
            g.px(11, 15, p["star"])
            g.px(6, 19, GOLD)
            _head_up(g, p)
            g.fill(3, 1, 10, 4, p["cloak"])
            g.fill(4, 0, 8, 2, p["cloakHi"])
            g.px(7, 2, p["star"])
            _lantern(g, 13, 18 + fr, frame)
        else:
            g.fill(3, 13, 8, 9, p["cloak"])
            g.fill(3, 13, 8, 1, p["cloakHi"])
            g.px(5, 16, p["star"])
            g.px(8, 18, MOON_GLOW)
            _head_side(g, p)
            g.fill(3, 1, 9, 4, p["cloak"])
            g.fill(4, 0, 7, 2, p["cloakHi"])
            g.px(6, 1, p["star"])
            _lantern(g, 12, 17 + fr, frame)
        return g

    def gen_orion_faint():
        """Same kid napping on his side — teal shirt, starry scarf, sleepy stars."""
        g = Pix(24, 16)
        p = ORION
        g.fill(3, 13, 18, 2, SHADOW)
        g.fill(18, 9, 4, 3, p["shoe"])
        g.fill(18, 8, 4, 1, p["pantsSh"])
        g.fill(14, 8, 5, 4, p["pants"])
        g.fill(14, 8, 5, 1, p["pantsSh"])
        g.fill(7, 7, 8, 5, p["shirt"])
        g.fill(7, 7, 8, 1, p["shirtHi"])
        g.fill(14, 8, 1, 4, p["shirtSh"])
        g.fill(6, 8, 1, 3, p["shirtHi"])
        # scarf
        g.fill(6, 7, 3, 3, p["scarf"])
        g.px(7, 8, GOLD)
        # moon pin
        g.px(10, 9, p["moon"])
        # head
        g.fill(1, 5, 7, 6, p["hair"])
        g.fill(2, 4, 5, 2, p["hair"])
        g.fill(2, 6, 5, 4, SKIN)
        g.fill(2, 9, 5, 1, SKIN_SH)
        g.fill(2, 5, 5, 2, p["hair"])
        g.fill(3, 4, 3, 1, p["hairHi"])
        g.px(3, 8, OUT)
        g.px(4, 8, OUT)
        g.px(6, 8, OUT)
        g.px(7, 8, OUT)
        g.px(5, 10, LIP)
        g.px(1, 7, SKIN)
        g.px(2, 7, CHEEK)
        # cowlick
        g.px(3, 3, p["hairHi"])
        # sleepy stars
        g.px(4, 1, GOLD)
        g.px(3, 2, GOLD)
        g.px(5, 2, GOLD)
        g.px(4, 3, GOLD)
        g.px(4, 2, GOLD_HI)
        g.px(8, 0, GOLD_HI)
        g.px(7, 1, GOLD)
        g.px(9, 1, GOLD)
        return g

    def gen_statue():
        """Moon-kid holding up the night — stone figure, glowing crescent."""
        g = Pix(16, 32)
        stone, hi, sh = C["stone"], C["stoneHi"], C["stoneSh"]
        g.fill(3, 30, 10, 2, SHADOW)
        # plinth with a star
        g.fill(3, 24, 10, 6, stone)
        g.fill(3, 24, 10, 1, hi)
        g.fill(3, 24, 1, 6, hi)
        g.fill(12, 24, 1, 6, sh)
        g.fill(3, 29, 10, 1, OUT)
        g.px(7, 26, GOLD)
        g.px(8, 26, GOLD_HI)
        g.px(7, 27, GOLD_SH)
        g.px(8, 27, GOLD)
        # legs
        g.fill(5, 19, 2, 5, stone)
        g.fill(9, 19, 2, 5, sh)
        g.fill(5, 19, 2, 1, hi)
        # body
        g.fill(5, 12, 6, 7, hi)
        g.fill(5, 12, 1, 7, stone)
        g.fill(10, 12, 1, 7, sh)
        # raised arms holding the moon
        g.fill(2, 9, 3, 3, stone)
        g.fill(11, 9, 3, 3, sh)
        g.px(2, 8, hi)
        g.px(13, 8, stone)
        g.fill(3, 11, 2, 3, stone)
        g.fill(11, 11, 2, 3, sh)
        # head
        g.fill(5, 6, 6, 6, hi)
        g.fill(6, 5, 4, 2, stone)
        g.fill(5, 10, 6, 1, stone)
        g.px(6, 8, sh)
        g.px(9, 8, sh)
        g.px(7, 10, stone)
        # glowing crescent held above — C opening right, readable at 16px
        cres = [
            (7, 0, MOON_GLOW), (8, 0, MOON_HI),
            (6, 1, MOON_HI), (7, 1, MOON_GLOW), (9, 1, MOON_MID),
            (5, 2, MOON_MID), (6, 2, MOON_HI), (7, 2, MOON_GLOW),
            (5, 3, MOON_MID), (6, 3, MOON_HI),
            (6, 4, MOON_MID), (7, 4, MOON_SH), (8, 4, MOON_SH),
            (7, 5, MOON_SH), (8, 5, MOON_SH), (9, 3, MOON_SH),
        ]
        for x, y, col in cres:
            g.px(x, y, col)
        g.px(11, 1, GOLD_HI)
        g.px(4, 2, GOLD)
        g.px(10, 0, MOON_GLOW)
        return g

    def gen_moonshard():
        """Crescent moon flake — not a generic diamond crystal."""
        g = Pix(16, 16)
        g.fill(4, 13, 8, 2, SHADOW)
        # thick C-crescent, opening right
        for x, y, col in [
            (7, 2, MOON_HI), (8, 2, MOON_GLOW), (9, 2, MOON_MID),
            (6, 3, MOON_HI), (7, 3, MOON_GLOW), (8, 3, MOON_HI), (9, 3, MOON_SH),
            (5, 4, MOON_MID), (6, 4, MOON_HI), (7, 4, MOON_GLOW), (8, 4, MOON_MID),
            (4, 5, MOON_MID), (5, 5, MOON_HI), (6, 5, MOON_GLOW), (7, 5, MOON_MID),
            (4, 6, MOON_MID), (5, 6, MOON_HI), (6, 6, MOON_MID),
            (4, 7, MOON_MID), (5, 7, MOON_MID), (6, 7, MOON_SH),
            (5, 8, MOON_MID), (6, 8, MOON_SH), (7, 8, MOON_SH),
            (6, 9, MOON_SH), (7, 9, MOON_MID), (8, 9, MOON_SH), (9, 9, MOON_SH),
            (7, 10, MOON_SH), (8, 10, MOON_MID), (9, 10, OUT),
            (8, 11, OUT),
        ]:
            g.px(x, y, col)
        g.px(10, 3, GOLD_HI)
        g.px(3, 6, GOLD)
        g.px(11, 8, GOLD)
        g.px(8, 1, MOON_GLOW)
        return g

    def gen_mountain_heart():
        """Mountain heart: a moonlight heart with a crescent nestled inside."""
        g = Pix(16, 16)
        g.fill(4, 14, 8, 2, SHADOW)
        # two bumps + point, moon-colored (not a bowl)
        g.fill(3, 3, 4, 4, MOON_MID)
        g.fill(9, 3, 4, 4, MOON_MID)
        g.fill(3, 6, 10, 4, MOON_MID)
        g.fill(4, 10, 8, 2, MOON_MID)
        g.fill(5, 12, 6, 1, MOON_SH)
        g.fill(6, 13, 4, 1, OUT)
        g.px(7, 13, MOON_SH)
        # left bump highlight, right bump shade
        g.fill(4, 3, 2, 2, MOON_HI)
        g.px(5, 2, MOON_GLOW)
        g.px(10, 2, MOON_HI)
        g.fill(11, 4, 2, 3, MOON_SH)
        g.fill(10, 10, 2, 2, MOON_SH)
        # inner gold crescent
        g.px(7, 6, MOON_GLOW)
        g.px(6, 7, MOON_HI)
        g.px(7, 7, GOLD_HI)
        g.px(8, 7, GOLD)
        g.px(6, 8, MOON_HI)
        g.px(7, 8, GOLD)
        g.px(8, 8, MOON_SH)
        g.px(7, 9, MOON_SH)
        # sparkles
        g.px(2, 4, GOLD_HI)
        g.px(13, 3, GOLD)
        g.px(8, 1, MOON_GLOW)
        return g

    extra_gen = {
        "player-down-0": lambda: gen_orion("down", 0),
        "player-down-1": lambda: gen_orion("down", 1),
        "player-up-0": lambda: gen_orion("up", 0),
        "player-up-1": lambda: gen_orion("up", 1),
        "player-right-0": lambda: gen_orion("right", 0),
        "player-right-1": lambda: gen_orion("right", 1),
        "player-left-0": lambda: gen_orion("right", 0).flip_h(),
        "player-left-1": lambda: gen_orion("right", 1).flip_h(),
        "npc-down-0": lambda: gen_junie("down", 0),
        "npc-down-1": lambda: gen_junie("down", 1),
        "npc-up-0": lambda: gen_junie("up", 0),
        "npc-up-1": lambda: gen_junie("up", 1),
        "npc-right-0": lambda: gen_junie("right", 0),
        "npc-right-1": lambda: gen_junie("right", 1),
        "npc-left-0": lambda: gen_junie("right", 0).flip_h(),
        "npc-left-1": lambda: gen_junie("right", 1).flip_h(),
        "nim-down-0": lambda: gen_nim("down", 0),
        "nim-down-1": lambda: gen_nim("down", 1),
        "nim-up-0": lambda: gen_nim("up", 0),
        "nim-up-1": lambda: gen_nim("up", 1),
        "nim-right-0": lambda: gen_nim("right", 0),
        "nim-right-1": lambda: gen_nim("right", 1),
        "nim-left-0": lambda: gen_nim("right", 0).flip_h(),
        "nim-left-1": lambda: gen_nim("right", 1).flip_h(),
        "player-faint": gen_orion_faint,
        "statue": gen_statue,
        "moonshard": gen_moonshard,
        "mooncrystal": gen_mountain_heart,
    }
    GENERATORS.update(extra_gen)

    A = [8, 28]
    extra_sprites = [
        {"id": "nim-down", "file": "actors/nim-down-{n}.png", "w": 16, "h": 32, "frames": 2, "anchor": A, "ox": 0, "oy": 0, "generated": True},
        {"id": "nim-up", "file": "actors/nim-up-{n}.png", "w": 16, "h": 32, "frames": 2, "anchor": A, "ox": 0, "oy": 0, "generated": True},
        {"id": "nim-right", "file": "actors/nim-right-{n}.png", "w": 16, "h": 32, "frames": 2, "anchor": A, "ox": 0, "oy": 0, "generated": True},
        {"id": "nim-left", "file": "actors/nim-left-{n}.png", "w": 16, "h": 32, "frames": 2, "anchor": A, "ox": 0, "oy": 0, "generated": True},
    ]
    ns["HERO_SPRITES"] = extra_sprites
    return extra_sprites
