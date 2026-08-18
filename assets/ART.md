# Moondrop Mountain art

How both Grok Build and Grok Bot change graphics. The game reads **shipped** PNGs only (`tiles/`, `props/`, `actors/`, `ui/` packed into `atlas.png`). Player save is browser `localStorage` — swapping pixels does not break a farm.

## Contract

```
Imagine (edit-chained from refs)
        ↓
  assets/inbox/<id>.png     ← proposed, not live
        ↓
  python3 tools/art.py preview <id>
        ↓
  you say “promote <id>”
        ↓
  python3 tools/art.py promote <id>
        ↓
  art-only git commit
        ↓
  if it looks wrong: python3 tools/art.py restore <id>
```

Do not promote unless the human said promote. Do not pack the atlas on a preview.

```
python3 tools/art.py status
python3 tools/art.py preview <id>
python3 tools/art.py promote <id>
python3 tools/art.py restore <id>
```

`preview` writes `assets/preview/compare-<id>.png` (left = shipped, right = inbox) and does not touch the atlas.

## Folders

| Path | Role |
|---|---|
| `assets/refs/` | Frozen canon (style sheet, Orion turnaround). Never overwrite from a generation pass. |
| `assets/inbox/` | Today’s Imagine drop. Named `inbox/<manifest-id>.png`. Not loaded by the game. |
| `assets/tiles/`, `props/`, `actors/`, `ui/` | Shipped game-size PNGs. Written only by `promote` / `restore`. |
| `assets/atlas.png` | Build product. Packed after promote/restore. |
| `assets/preview/` | Local compare strips. Gitignored. |
| `assets/generated-src/` | Historical dump. Do not add new work here. |
| `assets/palette.json` | Named colors. Promote snaps isolated sprites to this. |
| `assets/art.json` | Specials only (families, flips, chroma). Defaults come from `manifest.json`. |

Inbox is one slot per id — last writer wins. Extra local tries may use a suffix (`grass0-b.png`); only the exact id name promotes. Inbox may be committed so the other harness can pick it up.

Refs:

- World / props: `assets/refs/style-sheet.png`
- Orion: `assets/refs/orion-sheet.png`
- Anyone else: the **current shipped PNG** as the edit-chain source. Do not invent a new Orion from text.

## Look

- Original **16-bit 3/4** (2.5D): top of the ground, front of walls, roofs, crates, and people.
- Same *family* as Stardew Valley. **Do not copy or trace** Stardew sprites, the farmhouse, UI, or characters.
- Chunky, readable pixels. Three or four value steps per material (hi / mid / shadow / outline). Soft **1-pixel** dark outline.
- Warm spring farm. Use `palette.json`, not a new pastel set each time.
- Isolated sprites on flat **magenta `#FF00FF`** (or already transparent). No baked ground, no cast shadow (the game draws shadows), no scenery behind the subject.
- **Tiles** are the exception: full-bleed, seamless, no chroma. Highest-risk Imagine category. Prefer native 16×16 or exactly 2× then nearest-neighbor. Always check a 2×2 tile.

## Sizes

Read `w` / `h` from `assets/manifest.json`. Do not invent a new size without adding the sprite first.

- Ground tiles: 16×16
- People: 16×32, two walk frames (a 1px bob is fine)
- Chicken: 16×16 × 2
- Props: 16×16 up to house 80×80

Draw at **native game size**, or exactly **2×** (then nearest-neighbor down). Do not generate a large painting and shrink it — that is how Orion went muddy.

## Imagine

1. Recurring subject → `image_edit` from the matching ref (or the shipped PNG). Never a fresh text-only `image_gen` of Orion, Junie, Nim, or a tile already in the game.
2. Keep the style sentence in every edit prompt so the look does not drift photoreal.
3. Drop the PNG in `inbox/<id>.png`, run `preview`, **stop**.

Shared prompt (copy, then name the one subject):

> 16-bit SNES-era farm RPG sprite, three-quarter view, chunky pixels, limited warm palette, one-pixel dark outline, isolated on flat magenta #FF00FF, no drop shadow, no background scenery, crisp native pixels.

## Do not

- Run `python3 tools/process-generated.py` with no flags (rewrites the world). It now requires `--all`.
- Run `python3 tools/export-assets.py --regen` (overwrites shipped Imagine art with the Python painters).
- Mix art and gameplay in one commit.
- Promote a whole set “while we are here.”
- Overwrite `assets/refs/` unless the human said this is the new canon.
