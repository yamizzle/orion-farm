# Orion's Game — blank spring farm

This is a **tech-test shell**, not the full farm game yet. No bunny, no growing crops, no NPCs, no inventory items. It exists so Darren can confirm a public link opens full-screen on Chromebook, iPad, and iPhone — and so Orion (7) can see that this is the *kind* of game he means (looking down at a tiled farm, not a cartoon postcard).

Later updates should replace files in this same project / same published URL. Do not start a second game site unless you mean to.

## Open it

Public URL (GitHub Pages):

https://yamizzle.github.io/orion-farm/

On a Chromebook, iPad, or iPhone: open that link in the browser (Safari or Chrome). It should fill the screen with a pixel farm — grass, a dirt path, a wooden house, a fenced plot, a tree. Tap or click a tile: it highlights and a soft ripple fades. Tap a hotbar slot to select it.

Landscape on iPad is the intended view. If the page looks like a GitHub file list instead of a farm, wait a minute and refresh; Pages sometimes needs a short first deploy.

## What is in here

- `index.html` — the whole game (vanilla HTML/CSS/JS, one canvas, no build step, no Phaser, no accounts, no ads, no trackers)
- `.nojekyll` — tells GitHub Pages to serve the files as-is

Art is original 16×16 pixel tiles drawn in code. It is meant to feel like the same *family* as Stardew Valley (3/4 top-down, spring greens, mustard path, wood HUD). It does not copy Stardew sprites, the farmhouse, UI chrome, or fonts.

## How to update later

Edit `index.html` in this repo and push to `main`. The same Pages URL will show the new version after deploy (usually under a minute).
