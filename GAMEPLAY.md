# Moondrop Mountain gameplay canon

Rules both harnesses must keep. If a playtest or a “simplify smash” impulse disagrees with this file, **this file wins** until the human says otherwise.

Read this before changing harvest, drops, tools, the hotbar, the shop, or combat equipment.

## Chop and smash

Stand **beside** the tile (do not walk onto a live tree or rock). **One tap = one strike.** HP persists in `harvestNodes` (`state: "hurt"`). Walk away and the chips stay.

| Node | Hands | Right tool |
|---|---|---|
| Farm tree | 5 HP, 1 dmg | Axe: 3 dmg (two hits), extra wood |
| Fallen log (woods) | 2 HP, 1 dmg | Axe: 2 dmg (one hit), wood on the tile |
| Farm rock | 5 HP, 1 dmg | Pick: 3 dmg (two hits), extra stone |
| Mine rock (floors 1–3) | 4 HP, 1 dmg | Pick: 4 dmg (one hit) |
| Deep mine rock (floor 4+) | 6 HP, 1 dmg | Pick: 3 dmg (two hits) |

Do **not** set rock HP to 1. Do **not** one-shot farm rocks without a pick.

Hurt look: Imagine sprites `treeHurt` / `treeHurt2` and `rock0Hurt` / `rock0Hurt2` (rock1 is the flip). Do not paint scars in code. `nodeHurtStage` 0/1/2 picks the sprite.

Walking **into** a rock bumps; it does not smash. Smash is tap-on-rock or Space while adjacent/facing.

Fences are **pick-up builds**, not multi-hit chops. With **BUILD off**, tap a fence (or Space while adjacent/facing) while holding the **axe**, **shovel**, or an **empty hand** to remove it in one action: **1 wood** goes straight into the bag/tray and toast `FENCE PICKED UP`. Bag full keeps the fence and toasts `BAG FULL. USE THE CHEST.` Walking into a fence still bumps. Wood + **BUILD on** place flow is unchanged (still spends `FENCE_COST` wood). Loop: pick up → select wood → tap BUILD → place again.

Player **dirt paths** are pick-up builds too (same axe / shovel / empty hand gate). Tap a path you placed (or Space while standing on / next to it) to lift it: **1 stone** returns to the bag/tray, toast `PATH PICKED UP`, and the grass/dirt under it comes back. Holding **stone** (path place mode) skips pick-up so you can keep paving. World town cobble is not player path and stays. Pickaxe smash still does not mine paths (05bj).

Player-planted **town flowers** (from the FLOWER item / Pip buy) are pick-up placeables too: tap or Space-pick returns the flower straight to the bag/tray (`FLOWER PICKED UP`) so you can replant. World plaza flowers and wildflowers still pop ground loot to walk onto (harvest rule).


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

Tree chop **acorns** / **pinecones** are tray food too (tap the selected stack to nibble hearts + energy). They are not plantable seeds.

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
- **Gold loop:** grow carrots → Junie pays 10G. Pip **sells** (buns, seeds, flowers, hat, kits, fishing pole). Pip does **not** buy carrots or buns.
- **Tray + bag:** 10 extra tray slots (always on screen) plus a 15x6 bag of 90 storage cells (100 total). Use/eat/plant/tools from the selected tray slot only. Move stacks between tray and bag in the BAG panel. Pickup fills a tray stack with room, then a bag stack with room, then an empty tray slot, then an empty bag slot.

## Fishing

Farm ponds only (props at (3,33) and (24,13)). Not the town fountain.

- Buy **FISHING POLE** from Pip (30G, one-time). Hotbar slot like shovel. Selecting it does not eat or place.
- Stand orthogonally next to a pond tile with the pole selected, then tap the water or Space/E facing it.
- No pole: `YOU NEED A FISHING POLE.` Pole out but not next to water: tap walks, no auto-cast.
- Cast → wait ~1.5–4s (bobber) → reel. Miss ~28% before the rarity roll. No timing bar. Tap elsewhere cancels (no fish). Cannot walk/swing mid-cast.
- Catch goes to a named bag stack (150 cap). HUD shows the fish name. Do not grant fish on load.

## Storage

Not endless. Pockets are a work outing; the house chest is the warehouse. Ground piles stay on the tile when the bag is full.

| Place | Cap per kind | Role |
|---|---|---|
| Tray (10 extra slots) | 150 / stack | Always-on hotbar. What you use. |
| Bag (15x6 = 90 cells) | 150 / stack | Storage. Open BAG to move in/out of the tray |
| House chest | 500 | Home warehouse. Same UI later for shop crates / mine lockers, each with its own cap |
| Crop stacks (carrot, potato, berry) | 1000 | Bag and chest. Darren 8/29: hold up to 1000 carrots. Wood/ore stay 150/500 |
| Ground loot | until picked | Overflow that did not fit the bag |

Do not auto-move new pickups into the chest. `overflowBagToChest` is only for old saves that already exceeded the bag cap. Future storage is another chest object with a cap, not a bigger bag.

## Do not

- Mix a key graphic promote with a gameplay commit.
- Run `export-assets.py --regen` or `process-generated.py` without `--all`.
- Close a `BACKLOG.md` row without a live playtest on GitHub Pages.
