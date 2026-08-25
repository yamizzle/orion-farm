# Moondrop Mountain gameplay canon

Rules both harnesses must keep. If a playtest or a “simplify smash” impulse disagrees with this file, **this file wins** until the human says otherwise.

Read this before changing harvest, drops, tools, the hotbar, the shop, or combat equipment.

## Chop and smash

Stand **beside** the tile (do not walk onto a live tree or rock). **One tap = one strike.** HP persists in `harvestNodes` (`state: "hurt"`). Walk away and the chips stay.

| Node | Hands | Right tool |
|---|---|---|
| Farm tree | 5 HP, 1 dmg | Axe: 3 dmg (two hits), extra wood |
| Farm rock | 5 HP, 1 dmg | Pick: 3 dmg (two hits), extra stone |
| Mine rock (floors 1–3) | 4 HP, 1 dmg | Pick: 4 dmg (one hit) |
| Deep mine rock (floor 4+) | 6 HP, 1 dmg | Pick: 3 dmg (two hits) |

Do **not** set rock HP to 1. Do **not** one-shot farm rocks without a pick.

Hurt look: Imagine sprites `treeHurt` / `treeHurt2` and `rock0Hurt` / `rock0Hurt2` (rock1 is the flip). Do not paint scars in code. `nodeHurtStage` 0/1/2 picks the sprite.

Walking **into** a rock bumps; it does not smash. Smash is tap-on-rock or Space while adjacent/facing.

Trees occupy **one tile** for clicks and collision (the trunk). The canopy is draw-only. Do not hit-test the 48×64 sprite box.

## Drops

Harvest yields (wood, stone, iron extras, carrots, flowers, grass loot, monster drops) **pop onto the source tile** and hover. They do **not** auto-bag.

- Walk **onto** the drop tile to pick up (or tap it so Orion walks onto it). Standing beside is not enough.
- Same kind on that tile stacks as one pile with a count.
- Bag full: pile stays, toast `BAG FULL. USE THE CHEST.`
- Persist in the save (`loot`). Do not `flushPickups` ground piles into the bag on save or scene change.
- After pickup, the short fly-to-bag may play.

Use `spawnGroundLoot`. Do **not** `addItem("stone")` (or wood) inside `finishHarvest`.

Unique world finds (copper, mushroom, moon shard on the map) still sit as props until collected.

## Draw order (trees)

Sort actors by foot Y, same as everyone else. **Do not** add a constant to Orion’s foot to force him above every canopy.

- South of the trunk: in front of the tree.
- North of the trunk: behind the canopy. That is 3/4, not a bug.

## Economy (jobs)

Fuel stacks. Tools unlock once. Errands convert. Wonders stay in the world.

- **Iron** pays for the iron sword (4 wood + 3 iron) and shield (4 wood + 2 iron). Pick stays wood+stone so you can mine iron first.
- **Mushrooms** are food (tap to eat) after you have extras. Junie still takes **one** for her job.
- **Copper** drops stop after Pip’s lantern. Slot hides when that job is done.
- **Gem, sapphire, mountain heart** are finds / table trophies, not gold.
- **Gold loop:** grow carrots → Junie pays 10G. Pip **sells** (buns, seeds, flowers, hat, kits). Pip does **not** buy carrots or buns.
- **Hotbar is verbs:** seed, wood, stone, carrot, flower, bun always. Tools/hat only when owned. Copper only during Pip’s job. Shard only until it goes home. Mushroom only while you hold one.

## Storage

Not endless. Pockets are a work outing; the house chest is the warehouse. Ground piles stay on the tile when the bag is full.

| Place | Cap per kind | Role |
|---|---|---|
| Bag (pockets) | 150 | What Orion carries on the farm and in the mine |
| House chest | 500 | Home warehouse. Same UI later for shop crates / mine lockers, each with its own cap |
| Ground loot | until picked | Overflow that did not fit the bag |

Do not auto-move new pickups into the chest. `overflowBagToChest` is only for old saves that already exceeded the bag cap. Future storage is another chest object with a cap, not a bigger bag.

## Do not

- Mix a key graphic promote with a gameplay commit.
- Run `export-assets.py --regen` or `process-generated.py` without `--all`.
- Close a `BACKLOG.md` row without a live playtest on GitHub Pages.
