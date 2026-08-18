# Moondrop Mountain backlog

Playtest issues from the live game ([yamizzle.github.io/orion-farm](https://yamizzle.github.io/orion-farm/)). Both Grok Build and Grok Bot should pick from the top. Do not close an item without a playtest on the live URL.

Captured **2026-08-17 evening** and **2026-08-18 2am PT**. Latest `main` may already have started some of these (trees are supposed to take three hits, Start over asks to confirm, the shop still has Buy/Sell in code). Treat the table as *what a player felt*, then verify.

Highest-leverage theme: make chop, smash, and the sword *feel* like they hit, then make sure Orion can get to his bed.

| Pri | Status | Issue | Where | Notes |
| --- | --- | --- | --- | --- |
| Critical | Open | Sword never lands; no swing, hit flash, or death | Mine | 2am: enemies now chase and chew hearts with no flash or sound. Combat is one-sided. |
| Critical | Open | No heal path; farmhouse door opened the shop | House / shop | Soft-lock at 1 heart. Bed was unreachable in both playtests. |
| Critical | Open | Day clock races (morning to night in seconds) | Everywhere | README says ~2.5 min/day. Playtests felt much faster. |
| High | Open | Chop and smash have no juice; one tap and the thing vanishes | Farm | README says three hits. Playtests felt like one tap, no shake or chips. |
| High | Open | START OVER sits in the Jobs book | Jobs | Easy for Orion to tap. Confirm dialog exists; still too close to the job list. |
| High | Open | “Say hi to Junie” never completes | Town | Walk-through, no talk. Later pass: tap-talk works on others; Junie job still failed. |
| High | Verify | Shop Buy/Sell broken or missing | Shop | Evening: silent no-op at 0G. 2am: buttons gone. Code on `main` still draws BUY / SELL. |
| High | Open | Stone selected steals taps / can dump a rock on the wrong tile | Farm roads | Not reproduced on the 2am pass. |
| Medium | Partial | Night wash too blue; some people stay daylit | Farm / town | 2am: lamps and most NPC tint better; one villager still daylit; mountain night is a different teal. |
| Medium | Open | Mine looks like a flat tan room | Mine | Still bright and even at night. |
| Medium | Open | Stars list clips, names only | Stars | No kid-language hint, no paging. |
| Medium | Open | Header swaps season for place (“NIGHT · SHOP”) | Interiors | Lose the when/where anchor. |
| Low | Open | HUD overlap; FX / MU / FS labels | HUD | Cryptic for a 7-year-old. |
| Low | Open | Player hides behind the hotbar at the bottom of the map | Camera | New on the 2am pass. |
| Low | Open | Taps hit the facing tile, not the thing you tapped | Town | Fountain opened instead of the girl. |

## Strengths to keep

Warm wooden HUD, lamp pools at night, tap + WASD, walk-behind trees, fullscreen.

## How to use this

1. Take the top open Critical or High.
2. One playable change.
3. Hard-refresh the live URL and play it.
4. Mark the row `Done` (and the date) only after that playtest.
