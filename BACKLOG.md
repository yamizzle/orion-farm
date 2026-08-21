# Moondrop Mountain backlog

Playtest issues from the live game ([yamizzle.github.io/orion-farm](https://yamizzle.github.io/orion-farm/)). Both Grok Build and Grok Bot should pick from the top. Do not close an item without a playtest on the live URL.

Last live pass: **2026-08-20 5:03pm PT** (also 8/20 1:43pm, 8/20 2am, 8/19 2am). Treat the table as *what a player felt*.

Highest-leverage theme: make tap-to-move, chop/smash, and the sword *feel* like they work.

| Pri | Status | Issue | Where | Notes |
| --- | --- | --- | --- | --- |
| Critical | Open | Tap-to-move often no-ops | Overworld | 8/20 5pm: mine path, tap highlights, Orion stays put; S walks. Repro 3×. |
| Critical | Open | Tree tiles hide Orion and freeze WASD | Farm / woods | Still. Fully invisible under canopy; S blocked. |
| Critical | Open | Sword never lands; no swing or hitbox | Mine / HUD | 8/20 5pm: cave found (west edge, north). Adjacent snail/slime, 3 button taps, no arc/flash/HP. Claimed `main` fix not felt live. |
| Critical | Done 8/19 | Farmhouse door / bed | House | Not rechecked 5pm. |
| Critical | Worse | Day clock races | Everywhere | 8/20 5pm: Day 80→81 with no sleep; a full day in ~2–3 min of walking. |
| High | Open | Rocks vanish with no stone | Farm / mine | Still, including mine boulders. Count stays 0. |
| High | Open | Enemies draw on top of the hearts HUD | Mine / HUD | 8/20 5pm confirmed. Slime over notebook/hearts; contact 4→3.5, no flash. |
| High | Open | Star + Nim note stack on mine entry | Mine | 8/20 5pm: “A STAR! / CAVE DOOR” covers NIM'S NOTE. Note has no OK button. |
| High | Open | In-mine ladder exits; no Mine 2 | Mine | 8/20 5pm new. Looks like a down-ladder, dumps you outside. |
| High | Open | World toasts are illegible | Overworld | Not rechecked 5pm. |
| High | Open | “Say hi to Junie” stays after she talked | Town | Not rechecked 5pm. |
| High | Open | Shop / town buildings not enterable; 0G | Town | Not rechecked 5pm. |
| High | Open | Mine regenerates on every re-entry | Mine | 8/20 5pm new. Enemies/ore/walls shuffle; shard moves. Enemies wander, never chase. |
| High | Partial | Moon shard / hotbar | Mine | 8/20 5pm: shard collected, star awarded. |
| High | Open | Stone / seed selection steals taps | Farm | Not rechecked 5pm. |
| High | Open | START OVER sits in the Jobs book | Jobs | Not rechecked 5pm. |
| Medium | Partial | Night wash | Overworld | 8/20 5pm: night is actually dark (no seam). Flat saturated blue; player stays daylit. |
| Medium | Open | Sword button stays on the farm after the mine | HUD | 8/20 5pm. Big disc swallows taps. |
| Medium | Partial | Mine look | Mine | Brown rock + ore glints now; still uniformly lit, no torch falloff. |
| Medium | Open | Farm↔town grass seams | Overworld | Not rechecked 5pm. |
| Medium | Open | Stars list clips, names only | Stars | Not rechecked 5pm. |
| Medium | Open | Header swaps season for place | Interiors | Still (“MORNING · MINE 1”). |
| Low | Open | HUD overlap; FX / MU / FS labels | HUD | Still. |
| Low | Open | Player hides behind the hotbar | Camera | Still. |
| Low | Open | Taps in the top HUD band are swallowed | HUD | Still (tap at y≈150 did nothing). |
| Low | Open | Taps hit the facing tile, not the thing you tapped | Town | Still. |

## Strengths to keep

Warm wooden HUD, tap + WASD, house interior and bed, Junie talk, fullscreen, night is dark again.

## How to use this

1. Take the top open Critical or High.
2. One playable change.
3. Hard-refresh the live URL and play it.
4. Mark the row `Done` (and the date) only after that playtest.
