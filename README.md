# Moondrop Mountain

A tiny farm game for Orion. You look down at a spring farm on Moondrop Mountain: walk the fields, plant a seed, talk to a neighbor, watch a chicken wander, step inside the farmhouse, and follow the dirt path north to a mine in the rocky hill.

Art is **original 16-bit 3/4** (2.5D): you see the top of the ground and the front of walls, roofs, crates, and people. It is meant to feel like the same *family* as Stardew Valley. It does **not** copy or trace Stardew sprites, the farmhouse, UI, or characters.

## Open it

Public URL (GitHub Pages):

https://yamizzle.github.io/orion-farm/

On a Chromebook, iPad, or iPhone: open that link in the browser (Safari or Chrome). Landscape on iPad is the intended view.

On iPhone, tap the wood **FULL** plaque (top-right) so the farm fills the Safari page. Tap **EXIT**, or swipe down from the top, to go back. Add to Home Screen for a chrome-free farm.

- Tap the grass or path to walk there. The camera follows so you stay in the middle until you reach the edge of the mountain.
- Tap the farmhouse door or the stoop in front of it to go inside. Walk onto the doormat (or tap the inside door) to come back out, just south of the house.
- The mailbox by the house raises a teal flag and a letter when mail is waiting. Tap it (walk up if you need to) to read a wood-and-parchment letter. After you read it the flag goes down; tap again to re-read. A second letter arrives after the first mine visit.
- The first hotbar slot is a seed packet. Tap an empty brown plot inside the fence to plant a sprout.
- Tap a tree or a rock (outside or in the mine). Walk up, face it, and hit it three times. Trees leave a stump and give **wood**; rocks give **stone**.
- Wood is the second hotbar slot (2 wood = one fence). Stone is the third (1 stone = one path). Tap the slot, then tap empty grass or dirt to build. Fences block walking; paths do not.
- Tap the neighbor in the straw hat. They say hello, then tap again to close the box.
- A chicken wanders the farm grass. Tap it and it hops.
- Follow the dirt path north to the timbered cave in the rocky hill. Walk onto the mouth to go inside; tap the ladder to come back out.
- Inside, Nim left a wall note and three treasures in different rooms: a copper nugget, a cave mushroom, and a moon shard. Walk onto them to pick them up.
- A wood star on the HUD opens your stars. New ones pop up on a little plaque.

## Where the art lives

```
assets/
  generated-src/    IMAGE-GENERATOR originals (full-size, before chroma/crop)
  palette.json      named hex colors (grassMid, woodMid, …)
  manifest.json     every sprite: id, file, size, frames, anchor, atlas rect
  atlas.png         packed sheet the game loads
  atlas.json        same frame rects (handy for tools)
  tiles/            16×16 ground (grass, dirt, till, water, hill, stone, wall, wood floor, interior wall)
  props/            house, tree, stump, well, mailbox, mailbox-up, crate, pond, rocks, weeds, fences, cave, lantern, ladder, note, bed, table, rug, window, doormat, door
  actors/           player, neighbor, chicken (one PNG per facing/frame)
  ui/               seed packet, sprout, wood, stone, copper, mushroom, moon shard, star, letter
tools/
  process-generated.py  chroma-key, crop, and scale generated-src into game sizes
  export-assets.py      pack those PNGs into atlas.png (do not use --regen)
```

The game loads `assets/manifest.json` + `assets/atlas.png`, then draws with `Assets.draw(ctx, id, x, y, frame)`. It does not paint world pixels in the game loop.

## How to add a new graphic

1. Drop a PNG in the matching folder (example: `assets/ui/tomato.png`, 16×16).
2. Add one object to the `sprites` list in `assets/manifest.json`:

```json
{ "id": "tomato", "file": "ui/tomato.png", "w": 16, "h": 16, "frames": 1, "anchor": [0, 0] }
```

3. Rebuild the atlas (keeps your PNG; only fills in missing built-ins):

```bash
python3 tools/export-assets.py
```

Use `--regen` only if you want the script to overwrite the built-in PNGs from its pixel painter.

Then draw it in the game with `Assets.draw(ctx, "tomato", x, y)`.

To replace one existing sprite (a different tree, for example): overwrite that PNG and rerun the export. No hand-packing.

## How to update later

Edit files in this repo and push to `main`. The same Pages URL will show the new version after deploy (usually under a minute).
