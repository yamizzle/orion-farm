# Moondrop Mountain backlog

Playtest issues from the live game ([yamizzle.github.io/orion-farm](https://yamizzle.github.io/orion-farm/)). Both Grok Build and Grok Bot should pick from the top. Do not close an item without a playtest on the live URL.

Last live pass: **2026-08-20 1:43pm PT** (also 8/20 2am, 8/19 2am, 8/18 2am, 8/17 evening). Treat the table as *what a player felt*.

Highest-leverage theme: make tap-to-move, chop/smash, and the sword *feel* like they work.

| Pri | Status | Issue | Where | Notes |
| --- | --- | --- | --- | --- |
| Critical | Open | Tap-to-move often no-ops | Overworld woods | 8/20 pm new. Highlight appears, Orion stays put. Only WASD unsticks him. |
| Critical | Open | Tree tiles hide Orion and freeze WASD | Farm / woods | 8/20 pm: tap walks him onto the tree; he vanishes; WASD only turns until you tap elsewhere. |
| Critical | Verify | Sword never lands; swing button is silent | Mine / HUD | Not reached 8/20 pm (never found the cave). Fix claimed on `main`: mine swing + slime reach hit. Needs a live mine playtest. |
| Critical | Done 8/19 | Farmhouse door / bed | House | Still good 8/20 pm. Sleep Day 2→3 correct. |
| Critical | Worse | Day clock races | Everywhere | 8/20 pm: Day 1→2 in ~90s with no sleep; Day 6 in ~10 min. Indoors still frozen. |
| High | Open | Rocks vanish with no stone | Farm / woods | 8/20 pm: pick tap removes the rock, count stays 0, no shake/sound. Rocks also blink when you step on them. |
| High | Open | World toasts are illegible | Overworld | 8/20 pm new. Washed-out transparent text over grass. |
| High | Open | “Say hi to Junie” stays after she already talked | Town | 8/20 pm: greeting fired, job still SAY HI TO JUNIE through Day 6. Reopened. |
| High | Open | Shop / town buildings not enterable; 0G | Town | 8/20 pm: every building is “KNOCK KNOCK… SOMEONE IS HOME.” Reed’s car/cart drifts; hard to say hi. |
| High | Open | Orion vanishes under tree canopies | Farm / forest | Still, and now also steals input (see Critical). |
| High | Open | Enemies draw on top of the hearts HUD | Mine / HUD | Not reached 8/20 pm. |
| High | Open | Night can flip to full daylight while the clock says NIGHT | Overworld | Still 8/20 pm. Hard rectangular seam. |
| High | Partial | Chop and smash have no juice | Farm | 8/20 pm: one tap, gone, no stone. |
| High | Open | START OVER sits in the Jobs book | Jobs | Still the biggest button. Esc does not close; no X. |
| High | Partial | Moon shard / hotbar counts | Mine / hotbar | 8/20 pm: all counts 0 (did not reach mine). |
| High | Open | Mine “ore” walks around like a creature | Mine | Not reached 8/20 pm. |
| High | Open | Star popup covers an open dialog | Mine / house | Not reproduced 8/20 pm. |
| High | Open | Stone / seed selection steals taps | Farm | Still. |
| Medium | Open | Farm↔town grass seams | Overworld | 8/20 pm new. Straight-edged blocks where fields meet town. |
| Medium | Open | Sword button is a permanent overlay | HUD | Still. |
| Medium | Partial | Night wash too blue; people stay daylit | Farm / town | Still. Header NIGHT over a fully daylit world. |
| Medium | Open | Mine looks like a flat tan room | Mine | Not reached 8/20 pm. |
| Medium | Open | Stars list clips, names only | Stars | Still. |
| Medium | Open | Header swaps season for place | Interiors | Still (“EVENING · HOME”). |
| Low | Open | HUD overlap; FX / MU / FS labels | HUD | Still. |
| Low | Open | Player hides behind the hotbar | Camera | Still. |
| Low | Open | Taps in the top HUD band are swallowed | HUD | Still. |
| Low | Open | Taps hit the facing tile, not the thing you tapped | Town | Still. |

## Strengths to keep

Warm wooden HUD, lamp pools at night, tap + WASD, house interior and bed, Junie talk, fullscreen.

## How to use this

1. Take the top open Critical or High.
2. One playable change.
3. Hard-refresh the live URL and play it.
4. Mark the row `Done` (and the date) only after that playtest.
