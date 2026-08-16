# Moondrop Mountain

A tiny farm game for Orion. You look down at a spring farm: walk around, plant a seed, talk to a neighbor, and watch a chicken wander.

Art is **original 16-bit 3/4** (2.5D): you see the top of the ground and the front of walls, roofs, crates, and people. It is meant to feel like the same *family* as Stardew Valley. It does **not** copy or trace Stardew sprites, the farmhouse, UI, or characters.

## Open it

Public URL (GitHub Pages):

https://yamizzle.github.io/orion-farm/

On a Chromebook, iPad, or iPhone: open that link in the browser (Safari or Chrome). Landscape on iPad is the intended view.

On iPhone, tap the wood **FULL** plaque (top-right) so the farm fills the Safari page. Tap **EXIT**, or swipe down from the top, to go back. Add to Home Screen for a chrome-free farm.

- Tap the grass or path to walk there (the little person will go around the house, water, trees, and fence).
- The first hotbar slot is a seed packet. Tap an empty brown plot inside the fence to plant a sprout.
- Tap the neighbor in the straw hat. They say hello, then tap again to close the box.
- A chicken wanders on the grass. Tap it and it hops.

## Where the art lives

```
assets/
  generated-src/    IMAGE-GENERATOR originals (full-size, before chroma/crop)
  palette.json      named hex colors (grassMid, woodMid, …)
  manifest.json     every sprite: id, file, size, frames, anchor, atlas rect
  atlas.png         packed sheet the game loads
  atlas.json        same frame rects (handy for tools)
  tiles/            16×16 ground (grass, dirt, till, water)
  props/            house, tree, well, mailbox, crate, pond, rocks, weeds, fences
  actors/           player, neighbor, chicken (one PNG per facing/frame)
  ui/               seed packet, sprout
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
