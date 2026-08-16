"""Original combat sprites for Moondrop Mountain. Imported by export-assets."""
from __future__ import annotations


def install(ns):
    """Register combat generators and sprite records onto export-assets namespaces."""
    Pix = ns["Pix"]
    C = ns["C"]
    blob = ns["blob"]
    GENERATORS = ns["GENERATORS"]

    def gen_heart(filled=True):
        g = Pix(10, 9)
        body = C.get("heart", "#E04848")
        hi = C.get("heartHi", "#F87878")
        sh = C.get("heartSh", "#8A2028")
        out = C.get("heartOut", "#4A1014")
        empty = C.get("heartEmpty", "#5A3038")
        empty_hi = C.get("heartEmptyHi", "#7A4850")
        if not filled:
            body, hi, sh = empty, empty_hi, out
        # two bumps + point, 3/4 chubby heart
        g.fill(1, 1, 3, 3, body)
        g.fill(5, 1, 3, 3, body)
        g.fill(1, 3, 7, 3, body)
        g.fill(2, 6, 5, 1, body)
        g.fill(3, 7, 3, 1, body)
        g.px(4, 8, body)
        g.px(1, 1, hi)
        g.px(2, 1, hi)
        g.px(5, 1, hi)
        g.px(2, 2, hi)
        g.px(7, 3, sh)
        g.px(6, 6, sh)
        g.px(5, 7, sh)
        g.px(0, 2, out)
        g.px(3, 0, out)
        g.px(4, 1, out)
        g.px(6, 0, out)
        g.px(8, 2, out)
        g.px(8, 4, out)
        g.px(1, 5, out)
        g.px(7, 5, out)
        g.px(2, 7, out)
        g.px(6, 7, out)
        g.px(3, 8, out)
        g.px(5, 8, out)
        return g

    def gen_sword():
        g = Pix(16, 16)
        steel = C.get("steel", "#C8D0D8")
        steel_hi = C.get("steelHi", "#E8F0F4")
        steel_sh = C.get("steelSh", "#6A7888")
        gold = C.get("lanternGlow", "#F0C060")
        gold_sh = C.get("honeySh", "#A86C14")
        grip = C["woodMid"]
        out = C["woodOut"]
        g.fill(4, 13, 8, 2, C.get("shadow", "rgba(30,90,18,0.40)"))
        # blade, diagonal-ish 3/4
        g.fill(9, 1, 2, 8, steel)
        g.px(9, 1, steel_hi)
        g.px(10, 1, steel)
        g.px(8, 2, steel_hi)
        g.fill(8, 2, 1, 7, steel_hi)
        g.fill(11, 2, 1, 7, steel_sh)
        g.px(10, 0, steel_hi)
        g.px(9, 0, out)
        g.px(11, 1, out)
        # guard
        g.fill(5, 8, 7, 2, gold)
        g.fill(5, 8, 7, 1, C.get("npcHatHi", "#F0D878"))
        g.fill(5, 9, 7, 1, gold_sh)
        g.px(4, 8, out)
        g.px(12, 8, out)
        # grip
        g.fill(8, 10, 2, 4, grip)
        g.px(8, 10, C["woodHi"])
        g.px(9, 12, C["woodSh"])
        g.fill(7, 14, 4, 1, gold)
        g.px(8, 14, C.get("npcHatHi", "#F0D878"))
        return g

    def gen_gold_coin():
        g = Pix(16, 16)
        mid = C.get("goldCoin", "#F0C040")
        hi = C.get("goldCoinHi", "#F8E878")
        sh = C.get("goldCoinSh", "#C47A18")
        out = C["woodOut"]
        g.fill(4, 13, 8, 2, C.get("shadow", "rgba(30,90,18,0.40)"))
        blob(g, 7, 7, 5, 5, mid, sh, hi, out)
        g.fill(6, 5, 3, 5, sh)
        g.px(7, 4, hi)
        g.px(5, 6, hi)
        g.px(7, 7, hi)
        return g

    def gen_pedestal():
        g = Pix(16, 24)
        stone = C["stone"]
        hi = C["stoneHi"]
        sh = C["stoneSh"]
        out = C["woodOut"]
        steel = C.get("steel", "#C8D0D8")
        steel_hi = C.get("steelHi", "#E8F0F4")
        steel_sh = C.get("steelSh", "#6A7888")
        gold = C.get("lanternGlow", "#F0C060")
        g.fill(2, 22, 12, 2, C.get("shadow", "rgba(20,16,12,0.45)"))
        # plinth
        g.fill(3, 16, 10, 6, stone)
        g.fill(3, 16, 10, 1, hi)
        g.fill(3, 16, 1, 6, hi)
        g.fill(12, 16, 1, 6, sh)
        g.fill(3, 21, 10, 1, out)
        g.px(5, 18, hi)
        g.px(9, 19, sh)
        # sword standing in the stone
        g.fill(7, 2, 2, 14, steel)
        g.fill(7, 2, 1, 14, steel_hi)
        g.fill(9, 3, 1, 12, steel_sh)
        g.px(7, 1, steel_hi)
        g.px(8, 1, steel)
        g.px(7, 0, out)
        g.fill(4, 13, 8, 2, gold)
        g.fill(4, 13, 8, 1, C.get("npcHatHi", "#F0D878"))
        g.px(3, 13, out)
        g.px(12, 13, out)
        g.fill(7, 15, 2, 2, C["woodMid"])
        return g

    def gen_slime(frame):
        g = Pix(16, 16)
        mid = C.get("slime", "#6BCB3C")
        hi = C.get("slimeHi", "#A8E86A")
        sh = C.get("slimeSh", "#2F7A14")
        out = C.get("slimeOut", "#1E5A12")
        y = 0 if frame else 1
        g.fill(3, 13, 10, 2, C.get("shadow", "rgba(20,16,12,0.40)"))
        blob(g, 7, 8 + y, 6, 5, mid, sh, hi, out)
        # cheeks
        g.px(3, 9 + y, C.get("blossom", "#E8A0A8"))
        g.px(12, 9 + y, C.get("blossom", "#E8A0A8"))
        # shine
        g.px(5, 5 + y, hi)
        g.px(6, 4 + y, C["parch"])
        # eyes
        g.px(5, 8 + y, C["woodOut"])
        g.px(6, 8 + y, C.get("playerEyeHi", "#5CBC88"))
        g.px(9, 8 + y, C["woodOut"])
        g.px(10, 8 + y, C.get("playerEyeHi", "#5CBC88"))
        # smile
        g.px(7, 10 + y, C.get("playerLip", "#C47A38"))
        g.px(8, 10 + y, C.get("playerLip", "#C47A38"))
        if frame:
            g.px(4, 3, hi)
            g.px(11, 3, hi)
        return g

    def gen_bat(frame):
        g = Pix(16, 16)
        fur = C.get("bat", "#6A5A88")
        hi = C.get("batHi", "#8A7AA8")
        sh = C.get("batSh", "#3A2A58")
        wing = C.get("batWing", "#4A3A70")
        out = C["woodOut"]
        y = 0 if frame else 1
        g.fill(4, 13, 8, 2, C.get("shadow", "rgba(20,16,12,0.40)"))
        # body
        blob(g, 7, 8 + y, 3, 3, fur, sh, hi, out)
        # ears
        g.px(5, 4 + y, fur)
        g.px(6, 3 + y, hi)
        g.px(9, 4 + y, fur)
        g.px(10, 3 + y, hi)
        g.px(5, 3 + y, out)
        g.px(10, 3 + y, out)
        # face
        g.px(6, 8 + y, C["woodOut"])
        g.px(9, 8 + y, C["woodOut"])
        g.px(7, 9 + y, C.get("blossom", "#E8A0A8"))
        g.px(8, 9 + y, C.get("blossom", "#E8A0A8"))
        # wings
        if frame:
            g.fill(1, 6 + y, 3, 2, wing)
            g.fill(12, 6 + y, 3, 2, wing)
            g.px(1, 5 + y, hi)
            g.px(14, 5 + y, hi)
            g.px(0, 7 + y, out)
            g.px(15, 7 + y, out)
        else:
            g.fill(1, 8 + y, 3, 2, wing)
            g.fill(12, 8 + y, 3, 2, wing)
            g.px(1, 10 + y, sh)
            g.px(14, 10 + y, sh)
            g.px(0, 9 + y, out)
            g.px(15, 9 + y, out)
        # feet
        g.px(6, 12 + y, C.get("batSh", "#3A2A58"))
        g.px(9, 12 + y, C.get("batSh", "#3A2A58"))
        return g

    def gen_grub(frame):
        g = Pix(16, 16)
        mid = C.get("grub", "#C4A878")
        hi = C.get("grubHi", "#E0C898")
        sh = C.get("grubSh", "#8A6A40")
        rock = C["stone"]
        out = C["woodOut"]
        x = 0 if frame else 1
        g.fill(3, 13, 10, 2, C.get("shadow", "rgba(20,16,12,0.40)"))
        # segmented pebble body
        blob(g, 5 + x, 9, 3, 3, mid, sh, hi, out)
        blob(g, 8 + x, 9, 3, 3, rock, C["stoneSh"], C["stoneHi"], out)
        blob(g, 11 + x, 9, 3, 3, mid, sh, hi, out)
        # head
        blob(g, 3 + x, 8, 3, 3, hi, sh, C["parch"], out)
        g.px(2 + x, 7, C["woodOut"])
        g.px(3 + x, 7, C.get("playerEyeHi", "#5CBC88"))
        g.px(4 + x, 8, C.get("playerLip", "#C47A38"))
        # tiny antenna
        g.px(2 + x, 4, sh)
        g.px(4 + x, 4, sh)
        g.px(1 + x, 3, C.get("flower", "#E8C84A"))
        g.px(5 + x, 3, C.get("flower", "#E8C84A"))
        # feet
        if frame:
            g.px(5, 13, sh)
            g.px(8, 13, sh)
            g.px(11, 13, sh)
        else:
            g.px(6, 13, sh)
            g.px(9, 13, sh)
            g.px(12, 13, sh)
        return g

    def gen_player_faint():
        """Kid-safe 3/4 faint: Orion napping on his side, closed eyes, tiny stars."""
        g = Pix(24, 16)
        hair = C.get("playerHair", "#3A5A28")
        hair_hi = C.get("playerHairHi", "#5A8A40")
        skin = C.get("skin", "#F0C090")
        skin_sh = C.get("skinSh", "#C49060")
        shirt = C.get("playerShirt", "#3A8A48")
        shirt_hi = C.get("playerShirtHi", "#5CBC68")
        shirt_sh = C.get("playerShirtSh", "#246434")
        pants = C.get("playerPants", "#3A4A6A")
        pants_sh = C.get("playerPantsSh", "#24344A")
        shoe = C.get("playerShoe", "#3A2210")
        out = C.get("woodOut", "#3D1A0C")
        gold = C.get("flower", "#E8C84A")
        gold_hi = C.get("parch", "#F3D2A3")
        g.fill(3, 13, 18, 2, C.get("shadow", "rgba(30,90,18,0.40)"))
        # shoes + legs
        g.fill(18, 9, 4, 3, shoe)
        g.fill(18, 8, 4, 1, pants_sh)
        g.fill(14, 8, 5, 4, pants)
        g.fill(14, 8, 5, 1, pants_sh)
        # torso
        g.fill(7, 7, 8, 5, shirt)
        g.fill(7, 7, 8, 1, shirt_hi)
        g.fill(14, 8, 1, 4, shirt_sh)
        g.fill(6, 8, 1, 3, shirt_hi)
        # head (left), eyes closed
        g.fill(1, 5, 7, 6, hair)
        g.fill(2, 4, 5, 2, hair)
        g.fill(2, 6, 5, 4, skin)
        g.fill(2, 9, 5, 1, skin_sh)
        g.fill(2, 5, 5, 2, hair)
        g.fill(3, 4, 3, 1, hair_hi)
        g.px(3, 8, out)
        g.px(4, 8, out)
        g.px(6, 8, out)
        g.px(7, 8, out)
        g.px(5, 10, C.get("playerLip", "#C47A38"))
        g.px(1, 7, skin)
        # sleepy stars
        g.px(4, 1, gold)
        g.px(3, 2, gold)
        g.px(5, 2, gold)
        g.px(4, 3, gold)
        g.px(4, 2, gold_hi)
        g.px(8, 0, gold_hi)
        g.px(7, 1, gold)
        g.px(9, 1, gold)
        return g

    def gen_faint_star(frame):
        """Chubby 16-bit sparkle star for the faint burst."""
        g = Pix(16, 16)
        gold = C.get("flower", "#E8C84A")
        hi = C.get("parch", "#F3D2A3")
        sh = C.get("honeySh", "#A86C14")
        out = C.get("woodOut", "#3D1A0C")
        cx, cy = 8, 8
        if frame == 0:
            arms = ((0, -3), (0, 3), (-3, 0), (3, 0), (-2, -2), (2, -2), (-2, 2), (2, 2))
            g.px(cx, cy, hi)
            g.px(cx, cy - 1, gold)
            g.px(cx, cy + 1, sh)
        elif frame == 1:
            arms = ((0, -5), (0, 5), (-5, 0), (5, 0), (-3, -3), (3, -3), (-3, 3), (3, 3))
            g.fill(cx - 1, cy - 1, 3, 3, gold)
            g.px(cx, cy, hi)
            g.px(cx, cy - 1, hi)
            g.px(cx + 1, cy, sh)
        else:
            arms = ((0, -6), (0, 6), (-6, 0), (6, 0), (-4, -4), (4, -4), (-4, 4), (4, 4))
            g.fill(cx - 1, cy - 1, 3, 3, gold)
            g.px(cx, cy, hi)
            g.px(cx - 1, cy - 1, hi)
            g.px(cx + 1, cy + 1, sh)
            g.px(cx, cy - 2, gold)
            g.px(cx, cy + 2, sh)
        for dx, dy in arms:
            g.px(cx + dx, cy + dy, gold if abs(dx) + abs(dy) < 7 else hi)
            if frame:
                g.px(cx + dx // 2, cy + dy // 2, gold)
        g.px(cx, cy - 1, hi)
        if frame == 2:
            g.px(1, 2, hi)
            g.px(14, 3, gold)
            g.px(2, 13, gold)
            g.px(13, 12, hi)
        return g

    def gen_slash(frame):
        """Faint 16-bit crescent spark for the sword arc (2 frames)."""
        g = Pix(24, 16)
        hi = C.get("steelHi", "#E8F0F4")
        mid = C.get("steel", "#C8D0D8")
        gold = C.get("lanternGlow", "#F0C060")
        parch = C.get("parch", "#F3D2A3")
        sh = C.get("steelSh", "#6A7888")
        # C-shaped crescent opening right, readable when rotated with the blade
        arc = [
            (11, 1), (12, 1), (13, 2), (14, 2),
            (9, 2), (10, 2), (8, 3), (7, 4),
            (6, 5), (5, 6), (5, 7), (5, 8),
            (6, 9), (7, 10), (8, 11), (9, 12),
            (10, 13), (11, 14), (12, 14), (13, 13), (14, 13),
        ]
        inner = [
            (11, 2), (12, 2), (10, 3), (9, 3),
            (8, 4), (7, 5), (6, 6), (6, 7), (6, 8),
            (7, 9), (8, 10), (9, 11), (10, 12), (11, 13), (12, 13),
        ]
        for x, y in arc:
            g.px(x, y, hi if y < 5 else (mid if y < 11 else sh))
        for x, y in inner:
            g.px(x, y, gold if frame else mid)
        if frame:
            g.px(15, 2, parch)
            g.px(16, 3, gold)
            g.px(4, 7, parch)
            g.px(15, 13, parch)
            g.px(16, 12, gold)
            g.px(12, 3, parch)
            g.px(7, 7, parch)
        return g

    extra_gen = {
        "heart": lambda: gen_heart(True),
        "heartEmpty": lambda: gen_heart(False),
        "sword": gen_sword,
        "goldCoin": gen_gold_coin,
        "swordPedestal": gen_pedestal,
        "slime-0": lambda: gen_slime(0),
        "slime-1": lambda: gen_slime(1),
        "bat-0": lambda: gen_bat(0),
        "bat-1": lambda: gen_bat(1),
        "rockgrub-0": lambda: gen_grub(0),
        "rockgrub-1": lambda: gen_grub(1),
        "player-faint": gen_player_faint,
        "faintStar-0": lambda: gen_faint_star(0),
        "faintStar-1": lambda: gen_faint_star(1),
        "faintStar-2": lambda: gen_faint_star(2),
        "slash-0": lambda: gen_slash(0),
        "slash-1": lambda: gen_slash(1),
    }
    GENERATORS.update(extra_gen)

    MonA = [8, 14]
    extra_sprites = [
        {"id": "heart", "file": "ui/heart.png", "w": 10, "h": 9, "frames": 1, "anchor": [0, 0], "ox": 0, "oy": 0, "generated": True},
        {"id": "heartEmpty", "file": "ui/heartEmpty.png", "w": 10, "h": 9, "frames": 1, "anchor": [0, 0], "ox": 0, "oy": 0, "generated": True},
        {"id": "sword", "file": "ui/sword.png", "w": 16, "h": 16, "frames": 1, "anchor": [0, 0], "ox": 0, "oy": 0, "generated": True},
        {"id": "goldCoin", "file": "ui/goldCoin.png", "w": 16, "h": 16, "frames": 1, "anchor": [0, 0], "ox": 0, "oy": 0, "generated": True},
        {"id": "swordPedestal", "file": "props/swordPedestal.png", "w": 16, "h": 24, "frames": 1, "anchor": [0, 0], "ox": 0, "oy": -8, "generated": True},
        {"id": "slime", "file": "actors/slime-{n}.png", "w": 16, "h": 16, "frames": 2, "anchor": MonA, "ox": 0, "oy": 0, "generated": True},
        {"id": "bat", "file": "actors/bat-{n}.png", "w": 16, "h": 16, "frames": 2, "anchor": MonA, "ox": 0, "oy": 0, "generated": True},
        {"id": "rockgrub", "file": "actors/rockgrub-{n}.png", "w": 16, "h": 16, "frames": 2, "anchor": MonA, "ox": 0, "oy": 0, "generated": True},
        {"id": "player-faint", "file": "actors/player-faint.png", "w": 24, "h": 16, "frames": 1, "anchor": [12, 14], "ox": 0, "oy": 0, "generated": True},
        {"id": "faintStar", "file": "ui/faintStar-{n}.png", "w": 16, "h": 16, "frames": 3, "anchor": [8, 8], "ox": 0, "oy": 0, "generated": True},
        {"id": "slash", "file": "ui/slash-{n}.png", "w": 24, "h": 16, "frames": 2, "anchor": [12, 8], "ox": 0, "oy": 0, "generated": True},
    ]
    ns["COMBAT_SPRITES"] = extra_sprites
    return extra_sprites
