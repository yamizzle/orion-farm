# Moondrop Mountain backlog

Playtest issues from the live game ([yamizzle.github.io/orion-farm](https://yamizzle.github.io/orion-farm/)). Both Grok Build and Grok Bot should pick from the top. Do not close an item without a playtest on the live URL.

Last live pass: **2026-08-22 ~3:10–3:22pm PT** (also 8/22 midnight, 8/21 5:02am, 8/20 5pm, 8/20 1:43pm, 8/20 2am). Treat the table as *what a player felt*. Saved intact (never START OVER); DAY 1 SPRING MORNING 0G → DAY 5 SPRING MORNING after ~15 min (one bed sleep). No BUILD stamp visible.

Highest-leverage theme: the mine is unreachable (blocks sword, shards, slugs, Mine 2). Then canopy hide, rocks that ignore smash input, and the racing day clock. North/south camera pads still hold (Orion stays on-screen) but the camera now overscrolls into void bands.

| Pri | Status | Issue | Where | Notes |
| --- | --- | --- | --- | --- |
| Critical | Done 8/21 | Tap-to-move often no-ops | Overworld | 8/21 am: walks to reachable tiles. Residual: long tap to a blocked tile silently does nothing. Far-target no-ops are a new Low row. |
| Critical | Open | Tree canopy hides Orion completely | Forest N/W + town | Local 8/22 4:10pm: draw-order only — player+shadow sort 64px later so Orion stays above canopy (no sprite edits). Needs live refresh under N/W forest trees to close. Was: 8/22 3pm fully hidden. |
| Critical | Open | Sword never lands; no swing or hitbox | Mine / HUD | 8/22 midnight: mine Space/button always plays a visible arc; hitbox covers current, adjacent, and walk-destination tiles. Button stays mine-only. 8/22 3pm playtest: mine entrance not found, untested. |
| Critical | Done 8/22 | Farmhouse door / bed | House | 8/22 3pm: door and bed both work. Bed now dims the screen with a "YOU SLEEP..." banner, then Day+1 morning. Town houses knock-only. Shop is enterable. |
| Critical | Worse | Day clock races | Everywhere | Still. 8/22 3pm: ~30–60 s per phase; DAY 1→5 in ~15 min with one bed use. Rolls with no sleep. |
| Critical | Done 8/21 | Camera loses Orion south of the hotbar | Farm | 8/22 3pm reconfirm: walking south keeps Orion ~80px above the hotbar. Void-band overscroll below the map edge is a new Medium row. |
| Critical | Done 8/22 | Camera loses Orion under the DAY/season header | Forest N | 8/22 3pm reconfirm: Orion stays fully visible below the DAY/season panel. Camera overscrolls past the world edge into a flat green/blue void band — new Medium row. |
| Critical | Open | Mine entrance not discoverable | Farm W / Forest | Local 8/22 4:10pm: one-tile walk-in hole + MINE sign on the farm west dirt path (13,24), north of the house. Walking in loads MINE 1. Needs live refresh to close. Was: 8/22 3pm 15-min sweep found no cave. |
| High | Open | Rocks don't react; no stone | Farm / mine | Local 8/22 4:10pm: adjacent Space/walk-into/tap one-shots a rock, smash SFX, stone hotbar +1 immediately. Paving dirt with stone still in. Needs live refresh to close. Was: 8/22 3pm ignore input, stone 0. |
| High | Done 8/22 | Two Pips at once | Shop + town | 8/22 3pm reconfirm: only shop Pip. Town square has Lila (fountain) and Reed. Pip appears solely behind the shop counter. |
| High | Open | Shop has no buy/sell UI | Shop | Still. 8/22 3pm: enterable, Pip talks ("bring me one copper for a shop lantern"), no buy/sell, 0G. |
| High | Open | Enemies draw on top of the hearts HUD | Mine / HUD | 8/22 3pm playtest: mine entrance not found, untested. Collision itself is gone (see sword). |
| High | Open | Star + Nim note stack; popups inconsistent | Mine | Still stack on entry. 8/22 midnight: cave-door “A STAR!” now has an OK button. “MOON PIECE / FOUND A SHARD” has none (dismiss only by clicking anywhere). Nim’s Note still has no OK and ignores Esc. 8/22 3pm playtest: mine entrance not found, untested. Esc still closes nothing (Stars/Jobs/dialogue). Dialogue is click-to-dismiss; panels only via toolbar button. One dialog component with a mandatory OK/X and Esc binding. |
| High | Open | In-mine ladder exits; no Mine 2 | Mine | Still. 8/22 3pm playtest: mine entrance not found, untested. |
| High | Partial | “Say hi to Junie” stays after greetings | Farm | 8/22 3pm: Junie found on the farm near the house ("I'm Junie, can you find a cave mushroom for my garden?"). Plaza is Lila/Reed. Jobs text may still be stale after greeting — job-clear unverified. |
| High | Partial | Shop / town buildings | Town | Shop enterable. Other houses still knock-only. Still 0G. |
| High | Done 8/21 | Mine regenerates on every re-entry | Mine | 8/21: same rocks/sign/ladder on re-enter. Enemies still wander, not chase. 8/22 3pm playtest: mine entrance not found, untested. |
| High | Open | START OVER sits in the Jobs book | Jobs | Still the largest central button. No Esc/X. |
| High | Open | Stars list clips; no close | Stars | Still. MOONDROP NIGHT cut off, no scroll. Esc closes nothing. |
| High | Open | Toolbar buttons eat tap-to-move | HUD | 8/22 3pm new. Tapping the upper-left play area opens Stars instead of walking. Inset the HUD or ignore taps that begin on HUD chrome. |
| Medium | Worse | Night wash / tint inconsistent | Overworld | 8/22 3pm: north forest tints blue then flips to daylight-green while the header still says NIGHT; plaza stays blue; east houses render daylight at NIGHT. Drive tint from one global time value applied per-scene, not per-region. Mine untested this pass. |
| Medium | Done 8/22 | Sword button stays after the mine | HUD | 8/22 3pm reconfirm: absent on farm, forest, town, house, shop. Mine-only still holds; swing itself not re-verified (mine not found). |
| Medium | Partial | Mine look | Mine | Still uniformly lit, no torch falloff. Lamps glow. 8/22 3pm playtest: mine entrance not found, untested. |
| Medium | Open | Header swaps season for place | Interiors | Still (“AFTERNOON · HOME”, “MORNING · SHOP”). |
| Medium | Open | Slug contact drains hearts; no i-frames / heal | Mine | 8/22 midnight: contact 5→3 hearts, no i-frames feedback, no way to heal or fight back (sword does nothing). Mine is a pure health sink. 8/22 3pm playtest: mine entrance not found, untested. |
| Medium | Open | Camera overscrolls past world bounds | Farm / Forest N/S | 8/22 3pm new. N forest and S farm pads keep Orion on-screen, but the camera scrolls past the tile edge into a flat green/blue void band. Clamp camera to the world rect; keep the HUD-safe player insets. |
| Low | Open | HUD overlap; hotbar covers lower play field | HUD | Still. 8/22 3pm: hotbar overlaps the lower play field and NPCs in the bottom rows. FX / MU / FS labels still sit on the playfield. Inset the playable rect or raise the camera pad further. |
| Low | Done 8/21 | Player hides behind the hotbar | Camera | Same as the south camera pad fix. 8/22 3pm reconfirm (Orion ~80px above hotbar). |
| Low | Open | Closing a panel by tapping the world also walks | HUD | 8/21 new. Swallow the closing tap. 8/22 3pm: Esc still closes nothing; dialogue is click-to-dismiss, panels only via toolbar button. |
| Low | Open | Moon shard hotbar count stays 0 | Mine | 8/22 midnight: pickup credits the bag immediately so the hotbar badge reads 1 (was 0 until the fly-in finished, and the MOON PIECE toast paused that). 8/22 3pm playtest: mine entrance not found, untested. |
| Low | Done 8/22 | Bed advances the day with no prompt | House | 8/22 3pm: screen dim + "YOU SLEEP..." banner, then Day+1 morning. |
| Low | Open | Tap-to-move silently fails for far targets | Overworld | 8/22 3pm new. Far-right click from the farm is a no-op; mid-distance taps still work. |

## Strengths to keep

Tap-to-move is back (mid-distance), south camera pad holds (~80px above hotbar), north header pad keeps Orion below DAY/season, bed has a sleep banner, Pip lives only in the shop, sword button is mine-only on the overworld, Junie is a real farm NPC, shop interior exists, warm wooden HUD, fullscreen. Mine combat/shards not re-checked this pass (entrance missing).

## How to use this

1. Take the top open Critical or High.
2. One playable change.
3. Hard-refresh the live URL and play it.
4. Mark the row `Done` (and the date) only after that playtest.
