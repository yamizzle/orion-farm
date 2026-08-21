# Moondrop Mountain backlog

Playtest issues from the live game ([yamizzle.github.io/orion-farm](https://yamizzle.github.io/orion-farm/)). Both Grok Build and Grok Bot should pick from the top. Do not close an item without a playtest on the live URL.

Last live pass: **2026-08-21 5:02am PT** (also 8/20 5pm, 8/20 1:43pm, 8/20 2am). Treat the table as *what a player felt*.

Highest-leverage theme: make tap-to-move, chop/smash, and the sword *feel* like they work.

| Pri | Status | Issue | Where | Notes |
| --- | --- | --- | --- | --- |
| Critical | Done 8/21 | Tap-to-move often no-ops | Overworld | 8/21 am: walks to reachable tiles. Residual: long tap to a blocked tile silently does nothing. |
| Critical | Partial | Tree tiles hide Orion and freeze WASD | Farm / woods | 8/21 am: WASD no longer freezes. Still fully hidden under the canopy. |
| Critical | Open | Sword never lands; no swing or hitbox | Mine / HUD | 8/21 am: button and Space, no arc/damage. Slug shares the player tile, no contact hit. |
| Critical | Verify | Farmhouse door / bed | House | 8/21 am: did not enter a bed; town houses knock-only. Shop *is* enterable. Recheck the farmhouse door. |
| Critical | Worse | Day clock races | Everywhere | 8/21 am: Day 366→369 in ~13 min; ~3–4 min/day; rolls with no sleep. |
| Critical | Verify | Camera loses Orion south of the hotbar | Farm | 8/21 pm: camera keeps a 36px pad above the hotbar and can pan a little past the south edge. Needs a live walk-south playtest. |
| High | Open | Rocks vanish with no stone | Farm / mine | Still. Repeat taps, count stays 0; one rock vanished silently. |
| High | Open | Two Pips at once | Shop + town | 8/21 am new. Counter Pip and plaza Pip, same honey-bun line. |
| High | Open | Shop has no buy/sell UI | Shop | 8/21 am: enterable, Pip talks, still 0G, no prices. |
| High | Open | Enemies draw on top of the hearts HUD | Mine / HUD | Not re-shot 8/21. Collision itself is gone (see sword). |
| High | Open | Star + Nim note stack; note has no OK | Mine | 8/21: note still dismiss-only by tapping the world. |
| High | Open | In-mine ladder exits; no Mine 2 | Mine | Still. |
| High | Open | “Say hi to Junie” stays after greetings | Town | 8/21: still SAY HI TO JUNIE after Lila/Pip. Junie not found. |
| High | Partial | Shop / town buildings | Town | Shop enterable. Other houses still knock-only. Still 0G. |
| High | Done 8/21 | Mine regenerates on every re-entry | Mine | 8/21: same rocks/sign/ladder on re-enter. Enemies still wander, not chase. |
| High | Open | START OVER sits in the Jobs book | Jobs | Still the primary button. No Esc/X. |
| High | Open | Stars list clips; no close | Stars | 8/21: MOONDROP NIGHT cut off. First tap on the star button no-op’d. |
| Medium | Partial | Night wash | Overworld | 8/21: Orion night-tinted; lamps cast warm pools on farm and town. Mine still fully lit. |
| Medium | Open | Sword button stays after the mine | HUD | Still; floats outside the play area in interiors. |
| Medium | Partial | Mine look | Mine | Still uniformly lit, no torch falloff. |
| Medium | Open | Header swaps season for place | Interiors | Still (“EVENING · MINE 1”, “EVENING · SHOP”). |
| Low | Open | HUD overlap; FX / MU / FS labels | HUD | Still. |
| Low | Verify | Player hides behind the hotbar | Camera | Same camera pad as the Critical row. |
| Low | Open | Closing a panel by tapping the world also walks | HUD | 8/21 new. Swallow the closing tap. |

## Strengths to keep

Tap-to-move is back, night lamps tint Orion, shop interior exists, mine layout stays put, warm wooden HUD, fullscreen.

## How to use this

1. Take the top open Critical or High.
2. One playable change.
3. Hard-refresh the live URL and play it.
4. Mark the row `Done` (and the date) only after that playtest.
