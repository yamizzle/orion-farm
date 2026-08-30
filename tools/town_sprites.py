"""Original town tiles and sprites for Moondrop Mountain. Imported by export-assets."""
from __future__ import annotations


def install(ns):
    """Register town generators and sprite records onto export-assets namespaces."""
    Pix = ns["Pix"]
    C = ns["C"]
    blob = ns["blob"]
    hash01 = ns["hash01"]
    gen_grass = ns["gen_grass"]
    gen_person = ns["gen_person"]
    _person_colors = ns["_person_colors"]
    GENERATORS = ns["GENERATORS"]

    def gen_cobble():
        g = Pix(16, 16)
        g.fill(0, 0, 16, 16, C["cobbleMid"])
        pavers = [
            (0, 0, 7, 5), (8, 0, 8, 4),
            (0, 6, 5, 5), (6, 5, 10, 6),
            (0, 12, 8, 3), (9, 12, 7, 3),
        ]
        for i, (x, y, w, h) in enumerate(pavers):
            hi = C["cobbleHi"] if i % 2 == 0 else C["cobbleMid"]
            g.fill(x, y, w, h, hi)
            g.fill(x, y + h - 1, w, 1, C["cobbleSh"])
            g.fill(x + w - 1, y, 1, h, C["cobbleSh"])
            if i % 3 == 0:
                g.px(x + 1, y + 1, C["cobbleHi"])
            if i % 4 == 1:
                g.px(x + 2, y + 2, C["cobbleMoss"])
        for x in range(16):
            if x % 5 == 0:
                g.px(x, 0, C["cobbleHi"])
            g.px(x, 14, C["cobbleSh"])
            g.px(x, 15, C["woodOut"] if x % 2 else C["cobbleSh"])
        g.px(3, 8, C["cobbleMoss"])
        g.px(12, 3, C["cobbleMoss"])
        return g

    def gen_meadow():
        g = gen_grass(1)
        blooms = [
            (3, 4, C["blossom"]), (8, 3, C["flower"]), (12, 6, C["meadowBloom"]),
            (5, 9, C["flower"]), (11, 11, C["blossom"]), (2, 12, C["meadowBloom"]),
            (14, 9, C["flower"]), (7, 13, C["blossom"]),
        ]
        for x, y, col in blooms:
            g.px(x, y, col)
            g.px(x, y + 1, C["leaf"])
            g.px(x - 1, y + 1, C["grassSh"])
        g.px(4, 3, C["leaf"])
        g.px(9, 2, C["leaf"])
        return g

    def _cottage(roof, roof_hi, roof_sh, plaster=False, shop=False):
        g = Pix(64, 64)
        g.fill(6, 61, 52, 3, C["shadow"])
        # chimney
        g.fill(10, 4, 8, 2, C["stoneHi"])
        g.fill(11, 2, 6, 3, C["stone"])
        g.fill(11, 6, 6, 14, C["stone"])
        g.fill(11, 6, 1, 14, C["stoneHi"])
        g.fill(15, 6, 2, 14, C["stoneSh"])
        # roof top
        g.fill(22, 6, 20, 2, roof_hi)
        g.fill(26, 5, 12, 2, roof)
        for y in range(8, 30):
            t = (y - 8) / 21.0
            half = 10 + t * 20
            x0 = int(round(32 - half))
            x1 = int(round(32 + half))
            color = roof_sh if y % 5 == 0 else roof
            g.fill(x0, y, x1 - x0, 1, color)
            if (y + 2) % 5 == 0:
                for x in range(x0 + 2, x1 - 1, 4):
                    g.px(x, y, roof_hi)
            g.px(x0, y, C["woodOut"])
            g.px(x1 - 1, y, C["woodOut"])
            if y >= 12:
                g.px(x1, y, roof_sh)
        g.fill(4, 29, 56, 2, C["woodSh"])
        g.fill(4, 29, 56, 1, C["woodHi"])
        wall = C["plaster"] if plaster else C["woodMid"]
        wall_hi = C["plasterHi"] if plaster else C["woodHi"]
        wall_sh = C["plasterSh"] if plaster else C["woodSh"]
        g.fill(8, 31, 48, 28, wall)
        g.fill(8, 31, 48, 1, wall_hi)
        g.fill(8, 31, 1, 28, C["woodOut"])
        g.fill(55, 31, 1, 28, C["woodOut"])
        g.fill(56, 31, 4, 28, wall_sh)
        g.fill(59, 31, 1, 28, C["woodOut"])
        for y in range(36, 56, 6):
            g.fill(8, y, 48, 1, wall_sh)
        g.fill(6, 59, 52, 3, C["stone"])
        g.fill(6, 59, 52, 1, C["stoneHi"])
        # windows
        def win(wx, wy):
            g.fill(wx - 1, wy - 1, 10, 10, C["woodOut"])
            g.fill(wx, wy, 8, 8, C["glass"])
            g.fill(wx, wy, 8, 1, C["woodHi"])
            g.fill(wx + 3, wy, 2, 8, C["woodOut"])
            g.fill(wx, wy + 3, 8, 2, C["woodOut"])
            g.px(wx + 1, wy + 1, C["parch"])
            g.fill(wx - 1, wy + 8, 10, 2, C["woodSh"])
        win(12, 36)
        win(44, 36)
        # door
        g.fill(26, 40, 12, 19, C["woodOut"])
        g.fill(27, 41, 10, 8, C["door"])
        g.fill(27, 50, 10, 8, C["woodMid"])
        g.fill(27, 49, 10, 1, C["woodOut"])
        g.px(32, 44, C["glass"])
        g.px(35, 46, C["woodHi"])
        g.fill(24, 60, 16, 3, C["stone"])
        g.fill(26, 62, 12, 2, C["stoneHi"])
        if shop:
            # awning
            g.fill(20, 31, 24, 4, C["roof"])
            g.fill(20, 31, 24, 1, C["roofHi"])
            g.fill(20, 34, 24, 1, C["roofSh"])
            for x in range(20, 44, 4):
                g.fill(x, 32, 2, 2, C["roofHi"] if (x // 4) % 2 == 0 else C["roofSh"])
            # hanging sign
            g.fill(30, 18, 2, 8, C["woodMid"])
            g.fill(24, 14, 14, 10, C["woodMid"])
            g.fill(24, 14, 14, 1, C["woodHi"])
            g.fill(24, 14, 1, 10, C["woodOut"])
            g.fill(37, 14, 1, 10, C["woodOut"])
            g.fill(26, 16, 10, 6, C["parch"])
            g.px(28, 17, C["leaf"])
            g.px(30, 18, C["flower"])
            g.px(32, 17, C["dirtHi"])
            g.px(31, 19, C["dirtSh"])
        return g

    def gen_shop_house():
        return _cottage(C["roof"], C["roofHi"], C["roofSh"], plaster=False, shop=True)

    def gen_town_house_a():
        return _cottage(C["roofTeal"], C["roofTealHi"], C["roofTealSh"], plaster=True, shop=False)

    def gen_town_house_b():
        return _cottage(C["roofBlue"], C["roofBlueHi"], C["roofBlueSh"], plaster=True, shop=False)

    def gen_fountain(frame):
        g = Pix(32, 32)
        g.fill(6, 29, 20, 3, C["shadow"])
        # basin
        g.fill(4, 20, 24, 9, C["stone"])
        g.fill(4, 20, 2, 9, C["stoneHi"])
        g.fill(26, 20, 2, 9, C["stoneSh"])
        g.fill(4, 28, 24, 1, C["woodOut"])
        # rim
        g.fill(6, 18, 20, 3, C["stoneHi"])
        g.fill(6, 18, 20, 1, C["stone"])
        g.fill(8, 17, 16, 2, C["stoneHi"])
        # water
        g.fill(8, 20, 16, 6, C["water"])
        g.fill(8, 24, 16, 2, C["waterDp"])
        if frame == 0:
            g.fill(14, 8, 4, 10, C["waterFm"])
            g.fill(15, 6, 2, 4, C["water"])
            g.px(13, 12, C["waterFm"])
            g.px(18, 11, C["waterFm"])
            g.px(10, 21, C["waterFm"])
            g.px(21, 22, C["water"])
        else:
            g.fill(15, 7, 2, 11, C["waterFm"])
            g.fill(14, 10, 4, 6, C["water"])
            g.px(12, 14, C["waterFm"])
            g.px(19, 13, C["waterFm"])
            g.px(11, 22, C["water"])
            g.px(20, 21, C["waterFm"])
        # center post
        g.fill(14, 16, 4, 4, C["stone"])
        g.fill(14, 16, 4, 1, C["stoneHi"])
        g.px(15, 17, C["waterFm"])
        return g

    def gen_statue():
        g = Pix(16, 32)
        g.fill(3, 30, 10, 2, C["shadow"])
        # plinth
        g.fill(3, 24, 10, 6, C["stone"])
        g.fill(3, 24, 10, 1, C["stoneHi"])
        g.fill(3, 24, 1, 6, C["stoneHi"])
        g.fill(12, 24, 1, 6, C["stoneSh"])
        g.fill(3, 29, 10, 1, C["woodOut"])
        # figure: kid holding a moon
        g.fill(5, 10, 6, 8, C["stoneHi"])
        g.fill(5, 10, 1, 8, C["stone"])
        g.fill(10, 10, 1, 8, C["stoneSh"])
        # head
        g.fill(5, 4, 6, 6, C["stoneHi"])
        g.fill(6, 3, 4, 2, C["stone"])
        g.fill(5, 8, 6, 1, C["stone"])
        g.px(6, 6, C["stoneSh"])
        g.px(9, 6, C["stoneSh"])
        # arms up holding moon
        g.fill(3, 11, 2, 3, C["stone"])
        g.fill(11, 11, 2, 3, C["stone"])
        # moon
        g.fill(6, 0, 4, 4, C["moonHi"])
        g.fill(5, 1, 6, 3, C["moonMid"])
        g.px(6, 1, C["moonGlow"])
        g.px(9, 2, C["moonSh"])
        # legs
        g.fill(5, 18, 2, 6, C["stone"])
        g.fill(9, 18, 2, 6, C["stoneSh"])
        return g

    def gen_car(face, frame):
        g = Pix(24, 16)
        y = 0 if frame else 1
        g.fill(4, 13 + y, 16, 2, C["shadow"])
        # body
        g.fill(3, 5 + y, 18, 7, C["carRed"])
        g.fill(3, 5 + y, 18, 1, C["carRedHi"])
        g.fill(3, 5 + y, 1, 7, C["carRedHi"])
        g.fill(20, 5 + y, 1, 7, C["carRedSh"])
        g.fill(3, 11 + y, 18, 1, C["carRedSh"])
        # cabin
        g.fill(8, 2 + y, 8, 4, C["carDark"])
        g.fill(9, 3 + y, 6, 3, C["glass"])
        g.fill(9, 3 + y, 6, 1, C["parch"])
        # bumper
        g.fill(2, 10 + y, 2, 2, C["stoneHi"])
        g.fill(20, 10 + y, 2, 2, C["stoneHi"])
        # wheels
        wy = 11 + (0 if frame else 1)
        for wx in (5, 16):
            g.fill(wx, wy, 4, 4, C["carDark"])
            g.fill(wx + 1, wy + 1, 2, 2, C["stone"])
            if frame:
                g.px(wx + 1, wy, C["stoneHi"])
            else:
                g.px(wx + 2, wy + 3, C["stoneHi"])
        # headlights
        if face == "right":
            g.px(21, 8 + y, C["carYellow"])
            g.px(21, 9 + y, C["honeyHi"])
        else:
            g.px(2, 8 + y, C["carYellow"])
            g.px(2, 9 + y, C["honeyHi"])
        # roof stripe
        g.fill(10, 1 + y, 4, 1, C["carRedHi"])
        if face == "left":
            return g.flip_h()
        return g

    def gen_car_vert(face, frame):
        g = Pix(16, 20)
        y = 0 if frame else 1
        g.fill(3, 17 + y, 10, 2, C["shadow"])
        g.fill(3, 6 + y, 10, 10, C["carRed"])
        g.fill(3, 6 + y, 10, 1, C["carRedHi"])
        g.fill(3, 6 + y, 1, 10, C["carRedHi"])
        g.fill(12, 6 + y, 1, 10, C["carRedSh"])
        if face == "up":
            g.fill(4, 3 + y, 8, 4, C["carDark"])
            g.fill(5, 4 + y, 6, 3, C["glass"])
            g.px(5, 3 + y, C["carYellow"])
            g.px(10, 3 + y, C["carYellow"])
        else:
            g.fill(4, 12 + y, 8, 4, C["carDark"])
            g.fill(5, 13 + y, 6, 2, C["glass"])
            g.px(5, 16 + y, C["carYellow"])
            g.px(10, 16 + y, C["honeyHi"])
        for wx in (3, 10):
            g.fill(wx, 14 + y, 3, 3, C["carDark"])
            g.px(wx + 1, 15 + y, C["stone"])
        return g

    def gen_shop_sign():
        g = Pix(16, 16)
        g.fill(7, 0, 2, 4, C["woodMid"])
        g.fill(1, 3, 14, 12, C["woodMid"])
        g.fill(1, 3, 14, 1, C["woodHi"])
        g.fill(1, 3, 1, 12, C["woodOut"])
        g.fill(14, 3, 1, 12, C["woodOut"])
        g.fill(1, 14, 14, 1, C["woodOut"])
        g.fill(3, 5, 10, 8, C["parch"])
        g.px(5, 6, C["leaf"])
        g.px(7, 7, C["flower"])
        g.px(9, 6, C["dirtHi"])
        g.px(8, 8, C["dirtSh"])
        g.px(6, 9, C["leaf"])
        g.px(10, 9, C["blossom"])
        return g

    def gen_straw_hat():
        g = Pix(16, 16)
        g.fill(4, 13, 8, 2, C["shadow"])
        g.fill(5, 3, 6, 4, C["npcHat"])
        g.fill(5, 3, 6, 1, C["npcHatHi"])
        g.fill(5, 6, 6, 1, C["npcHatBand"])
        g.fill(2, 7, 12, 3, C["npcHat"])
        g.fill(1, 8, 14, 2, C["npcHatSh"])
        g.px(6, 4, C["npcHatHi"])
        return g

    def gen_honeybun():
        g = Pix(16, 16)
        g.fill(4, 13, 8, 2, C["shadow"])
        g.fill(4, 6, 8, 6, C["honey"])
        g.fill(5, 5, 6, 2, C["honeyHi"])
        g.fill(4, 6, 2, 6, C["honeyHi"])
        g.fill(10, 6, 2, 6, C["honeySh"])
        g.fill(5, 11, 6, 1, C["honeySh"])
        g.px(7, 7, C["parch"])
        g.px(8, 8, C["flower"])
        g.fill(6, 4, 4, 2, C["honeyHi"])
        return g

    def gen_town_flower():
        g = Pix(16, 16)
        g.fill(7, 10, 2, 5, C["grassSh"])
        g.px(7, 10, C["leaf"])
        g.fill(4, 4, 8, 6, C["blossom"])
        g.fill(5, 3, 6, 2, C["meadowBloom"])
        g.fill(6, 2, 4, 2, C["blossom"])
        g.px(7, 6, C["flower"])
        g.px(8, 6, C["flower"])
        g.px(4, 7, C["leaf"])
        g.px(11, 7, C["leaf"])
        g.px(6, 4, C["parch"])
        return g

    def gen_counter():
        g = Pix(48, 24)
        g.fill(2, 21, 44, 3, C["shadow"])
        g.fill(2, 6, 44, 5, C["woodHi"])
        g.fill(4, 5, 40, 2, C["parch"])
        g.fill(2, 10, 44, 1, C["woodOut"])
        g.fill(2, 11, 40, 8, C["woodMid"])
        g.fill(2, 11, 40, 1, C["woodHi"])
        g.fill(2, 18, 40, 1, C["woodSh"])
        g.fill(42, 6, 4, 13, C["woodSh"])
        g.fill(45, 6, 1, 13, C["woodOut"])
        for x in (4, 40):
            g.fill(x, 19, 3, 3, C["woodMid"])
        g.fill(8, 2, 5, 4, C["copperMid"])
        g.px(9, 1, C["leaf"])
        g.px(11, 1, C["flower"])
        g.fill(20, 3, 8, 3, C["parch"])
        g.fill(20, 3, 8, 1, C["woodHi"])
        g.px(22, 4, C["dirtHi"])
        g.px(25, 5, C["seed"] if False else C["leaf"])
        return g

    # extra person palettes
    orig = _person_colors

    def _town_person_colors(kind):
        if kind == "pip":
            return {
                "hair": C["pipHair"], "hairHi": C["pipHairHi"],
                "skin": C["skin"], "skinSh": C["skinSh"],
                "eye": C["npcEye"], "eyeHi": C["npcEyeHi"], "lip": C["npcLip"],
                "shirt": C["pipShirt"], "shirtHi": C["pipShirtHi"], "shirtSh": C["pipShirtSh"],
                "pants": C["npcPants"], "pantsSh": C["npcPantsSh"], "shoe": C["npcShoe"],
                "out": C["woodOut"],
                "apron": C["parch"],
            }
        if kind == "lila":
            return {
                "hair": C["lilaHair"], "hairHi": C["lilaHairHi"],
                "skin": C["skin"], "skinSh": C["skinSh"],
                "eye": C["npcEye"], "eyeHi": C["npcEyeHi"], "lip": C["npcLip"],
                "shirt": C["lilaShirt"], "shirtHi": C["lilaShirtHi"], "shirtSh": C["lilaShirtSh"],
                "pants": C["lilaShirtSh"], "pantsSh": C["npcPantsSh"], "shoe": C["npcShoe"],
                "out": C["woodOut"],
            }
        if kind == "reed":
            return {
                "hair": C["reedHair"], "hairHi": C["reedHairHi"],
                "skin": C["skin"], "skinSh": C["skinSh"],
                "eye": C["playerEye"], "eyeHi": C["playerEyeHi"], "lip": C["npcLip"],
                "shirt": C["reedShirt"], "shirtHi": C["reedShirtHi"], "shirtSh": C["reedShirtSh"],
                "pants": C["playerPants"], "pantsSh": C["playerPantsSh"], "shoe": C["playerShoe"],
                "out": C["woodOut"],
            }
        return orig(kind)

    ns["_person_colors"] = _town_person_colors

    def _gp(kind, face, frame):
        # temporarily use patched colors via ns
        old = ns.get("_person_colors_orig")
        return gen_person_town(kind, face, frame)

    def gen_person_town(kind, face, frame):
        """Same 16x32 chibi as gen_person, using town palettes."""
        g = Pix(16, 32)
        p = _town_person_colors(kind)
        fr = 1 if frame else 0
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
            if kind == "lila":
                g.px(3, 6, C["blossom"])
                g.px(12, 5, C["flower"])
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
            if kind == "lila":
                g.px(3, 5, C["blossom"])
        return g

    extra_gen = {
        "cobble": gen_cobble,
        "meadow": gen_meadow,
        "shopHouse": gen_shop_house,
        "townHouseA": gen_town_house_a,
        "townHouseB": gen_town_house_b,
        "fountain-0": lambda: gen_fountain(0),
        "fountain-1": lambda: gen_fountain(1),
        "statue": gen_statue,
        "car-right-0": lambda: gen_car("right", 0),
        "car-right-1": lambda: gen_car("right", 1),
        "car-left-0": lambda: gen_car("left", 0),
        "car-left-1": lambda: gen_car("left", 1),
        "car-up-0": lambda: gen_car_vert("up", 0),
        "car-up-1": lambda: gen_car_vert("up", 1),
        "car-down-0": lambda: gen_car_vert("down", 0),
        "car-down-1": lambda: gen_car_vert("down", 1),
        "shopSign": gen_shop_sign,
        "strawHat": gen_straw_hat,
        "honeybun": gen_honeybun,
        "townFlower": gen_town_flower,
        "counter": gen_counter,
        "pip-down-0": lambda: gen_person_town("pip", "down", 0),
        "pip-down-1": lambda: gen_person_town("pip", "down", 1),
        "pip-up-0": lambda: gen_person_town("pip", "up", 0),
        "pip-up-1": lambda: gen_person_town("pip", "up", 1),
        "pip-right-0": lambda: gen_person_town("pip", "right", 0),
        "pip-right-1": lambda: gen_person_town("pip", "right", 1),
        "pip-left-0": lambda: gen_person_town("pip", "right", 0).flip_h(),
        "pip-left-1": lambda: gen_person_town("pip", "right", 1).flip_h(),
        "lila-down-0": lambda: gen_person_town("lila", "down", 0),
        "lila-down-1": lambda: gen_person_town("lila", "down", 1),
        "lila-up-0": lambda: gen_person_town("lila", "up", 0),
        "lila-up-1": lambda: gen_person_town("lila", "up", 1),
        "lila-right-0": lambda: gen_person_town("lila", "right", 0),
        "lila-right-1": lambda: gen_person_town("lila", "right", 1),
        "lila-left-0": lambda: gen_person_town("lila", "right", 0).flip_h(),
        "lila-left-1": lambda: gen_person_town("lila", "right", 1).flip_h(),
        "reed-down-0": lambda: gen_person_town("reed", "down", 0),
        "reed-down-1": lambda: gen_person_town("reed", "down", 1),
        "reed-up-0": lambda: gen_person_town("reed", "up", 0),
        "reed-up-1": lambda: gen_person_town("reed", "up", 1),
        "reed-right-0": lambda: gen_person_town("reed", "right", 0),
        "reed-right-1": lambda: gen_person_town("reed", "right", 1),
        "reed-left-0": lambda: gen_person_town("reed", "right", 0).flip_h(),
        "reed-left-1": lambda: gen_person_town("reed", "right", 1).flip_h(),
    }
    GENERATORS.update(extra_gen)

    A = [8, 28]
    CarA = [12, 14]
    extra_sprites = [
        {"id": "cobble", "file": "tiles/cobble.png", "w": 16, "h": 16, "frames": 1, "anchor": [0, 0], "ox": 0, "oy": 0, "generated": True},
        {"id": "meadow", "file": "tiles/meadow.png", "w": 16, "h": 16, "frames": 1, "anchor": [0, 0], "ox": 0, "oy": 0, "generated": True},
        {"id": "shopHouse", "file": "props/shopHouse.png", "w": 96, "h": 80, "frames": 1, "anchor": [0, 0], "ox": 0, "oy": -16, "generated": True},
        {"id": "townHouseA", "file": "props/townHouseA.png", "w": 64, "h": 96, "frames": 1, "anchor": [0, 0], "ox": 0, "oy": -16, "generated": True},
        {"id": "townHouseB", "file": "props/townHouseB.png", "w": 96, "h": 80, "frames": 1, "anchor": [0, 0], "ox": 0, "oy": -16, "generated": True},
        {"id": "fountain", "file": "props/fountain-{n}.png", "w": 32, "h": 32, "frames": 2, "anchor": [0, 0], "ox": 0, "oy": 0, "generated": True},
        {"id": "statue", "file": "props/statue.png", "w": 16, "h": 32, "frames": 1, "anchor": [0, 0], "ox": 0, "oy": -16, "generated": True},
        {"id": "car-right", "file": "actors/car-right-{n}.png", "w": 24, "h": 16, "frames": 2, "anchor": CarA, "ox": 0, "oy": 0, "generated": True},
        {"id": "car-left", "file": "actors/car-left-{n}.png", "w": 24, "h": 16, "frames": 2, "anchor": CarA, "ox": 0, "oy": 0, "generated": True},
        {"id": "car-up", "file": "actors/car-up-{n}.png", "w": 16, "h": 20, "frames": 2, "anchor": [8, 18], "ox": 0, "oy": 0, "generated": True},
        {"id": "car-down", "file": "actors/car-down-{n}.png", "w": 16, "h": 20, "frames": 2, "anchor": [8, 18], "ox": 0, "oy": 0, "generated": True},
        {"id": "shopSign", "file": "props/shopSign.png", "w": 16, "h": 16, "frames": 1, "anchor": [0, 0], "ox": 0, "oy": 0, "generated": True},
        {"id": "strawHat", "file": "ui/strawHat.png", "w": 16, "h": 16, "frames": 1, "anchor": [0, 0], "ox": 0, "oy": 0, "generated": True},
        {"id": "honeybun", "file": "ui/honeybun.png", "w": 16, "h": 16, "frames": 1, "anchor": [0, 0], "ox": 0, "oy": 0, "generated": True},
        {"id": "townFlower", "file": "ui/townFlower.png", "w": 16, "h": 16, "frames": 1, "anchor": [0, 0], "ox": 0, "oy": 0, "generated": True},
        {"id": "counter", "file": "props/counter.png", "w": 48, "h": 24, "frames": 1, "anchor": [0, 0], "ox": 0, "oy": -8, "generated": True},
        {"id": "pip-down", "file": "actors/pip-down-{n}.png", "w": 16, "h": 32, "frames": 2, "anchor": A, "ox": 0, "oy": 0, "generated": True},
        {"id": "pip-up", "file": "actors/pip-up-{n}.png", "w": 16, "h": 32, "frames": 2, "anchor": A, "ox": 0, "oy": 0, "generated": True},
        {"id": "pip-right", "file": "actors/pip-right-{n}.png", "w": 16, "h": 32, "frames": 2, "anchor": A, "ox": 0, "oy": 0, "generated": True},
        {"id": "pip-left", "file": "actors/pip-left-{n}.png", "w": 16, "h": 32, "frames": 2, "anchor": A, "ox": 0, "oy": 0, "generated": True},
        {"id": "lila-down", "file": "actors/lila-down-{n}.png", "w": 16, "h": 32, "frames": 2, "anchor": A, "ox": 0, "oy": 0, "generated": True},
        {"id": "lila-up", "file": "actors/lila-up-{n}.png", "w": 16, "h": 32, "frames": 2, "anchor": A, "ox": 0, "oy": 0, "generated": True},
        {"id": "lila-right", "file": "actors/lila-right-{n}.png", "w": 16, "h": 32, "frames": 2, "anchor": A, "ox": 0, "oy": 0, "generated": True},
        {"id": "lila-left", "file": "actors/lila-left-{n}.png", "w": 16, "h": 32, "frames": 2, "anchor": A, "ox": 0, "oy": 0, "generated": True},
        {"id": "reed-down", "file": "actors/reed-down-{n}.png", "w": 16, "h": 32, "frames": 2, "anchor": A, "ox": 0, "oy": 0, "generated": True},
        {"id": "reed-up", "file": "actors/reed-up-{n}.png", "w": 16, "h": 32, "frames": 2, "anchor": A, "ox": 0, "oy": 0, "generated": True},
        {"id": "reed-right", "file": "actors/reed-right-{n}.png", "w": 16, "h": 32, "frames": 2, "anchor": A, "ox": 0, "oy": 0, "generated": True},
        {"id": "reed-left", "file": "actors/reed-left-{n}.png", "w": 16, "h": 32, "frames": 2, "anchor": A, "ox": 0, "oy": 0, "generated": True},
    ]
    ns["TOWN_SPRITES"] = extra_sprites
    return extra_sprites
