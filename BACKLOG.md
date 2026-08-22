# Moondrop Mountain backlog

Playtest issues from the live game ([yamizzle.github.io/orion-farm](https://yamizzle.github.io/orion-farm/)). Both Grok Build and Grok Bot should pick from the top. Do not close an item without a playtest on the live URL.

Last live pass: **2026-08-22 midnight PT** (also 8/21 5:02am, 8/20 5pm, 8/20 1:43pm, 8/20 2am). Treat the table as *what a player felt*. Saved intact (never START OVER); day advanced 191→195 via bed/clock.

Highest-leverage theme: make tap-to-move, chop/smash, and the sword *feel* like they work. North camera pad shipped 8/22 (pair with the south hotbar pad).

| Pri | Status | Issue | Where | Notes |
| --- | --- | --- | --- | --- |
| Critical | Done 8/21 | Tap-to-move often no-ops | Overworld | 8/21 am: walks to reachable tiles. Residual: long tap to a blocked tile silently does nothing. |
| Critical | Worse | Tree canopy hides Orion completely | Forest N/W | 8/22 midnight: escalated. North/west forest canopies hide him *completely* — multiple frames where the player is unfindable, not just partially. WASD freeze from 8/21 is still gone. Draw player above canopy / punch a hole. |
| Critical | Done 8/22 | Sword never lands; no swing or hitbox | Mine / HUD | 8/22: mine Space/button always plays a visible arc; hitbox covers current, adjacent, and walk-destination tiles. Button stays mine-only. |
| Critical | Partial | Farmhouse door / bed | House | 8/22: door and bed both work. Bed advances the day instantly with no sleep prompt, fade, or confirm (see Low row). Town houses knock-only. Shop is enterable. |
| Critical | Worse | Day clock races | Everywhere | Still. 8/22: ~30–60 s per phase; 4 in-game days (191→195) in ~12 min. Rolls with no sleep. |
| Critical | Done 8/21 | Camera loses Orion south of the hotbar | Farm | 8/22 reconfirm: walking south keeps Orion fully visible above the hotbar; expected green strip under the last grass row. |
| Critical | Done 8/22 | Camera loses Orion under the DAY/season header | Forest N | 8/22: north clamp insets by header + sprite height so Orion stays fully below the DAY/season panel; south hotbar pad unchanged. |
| High | Open | Rocks vanish with no stone | Farm / mine | Still. Repeat taps, count stays 0. |
| High | Done 8/22 | Two Pips at once | Shop + town | 8/22: town square has only Lila (fountain) and Reed. Pip appears solely behind the shop counter. |
| High | Open | Shop has no buy/sell UI | Shop | Still. Enterable, 0G, no prices. |
| High | Open | Enemies draw on top of the hearts HUD | Mine / HUD | Not re-shot 8/22. Collision itself is gone (see sword). |
| High | Open | Star + Nim note stack; popups inconsistent | Mine | Still stack on entry. 8/22: cave-door “A STAR!” now has an OK button (was missing). “MOON PIECE / FOUND A SHARD” has none (dismiss only by clicking anywhere). Nim’s Note still has no OK and ignores Esc. One dialog component with a mandatory OK/X and Esc binding. |
| High | Open | In-mine ladder exits; no Mine 2 | Mine | Still. Ladder exits to surface. |
| High | Open | “Say hi to Junie” stays after greetings | Town | Still SAY HI TO JUNIE. Plaza NPCs are Lila and Reed (Pip is shop-only). Junie not found. |
| High | Partial | Shop / town buildings | Town | Shop enterable. Other houses still knock-only. Still 0G. |
| High | Done 8/21 | Mine regenerates on every re-entry | Mine | 8/21: same rocks/sign/ladder on re-enter. Enemies still wander, not chase. |
| High | Open | START OVER sits in the Jobs book | Jobs | Still the primary button. No Esc/X. |
| High | Open | Stars list clips; no close | Stars | Still. MOONDROP NIGHT cut off, no scroll. |
| Medium | Worse | Night wash / tint inconsistent | Overworld | 8/22: at NIGHT, plaza and near-farm render fully blue-tinted, while north forest and mine-entrance screens render in full daylight with the header still reading NIGHT. Drive tint from one global time value applied per-scene, not per-region. Mine still fully lit (lamps do glow); player not night-tinted in mine. |
| Medium | Done 8/22 | Sword button stays after the mine | HUD | 8/22: sword button only renders inside MINE 1; absent on farm, forest, town, shop. |
| Medium | Partial | Mine look | Mine | Still uniformly lit, no torch falloff. Lamps glow. |
| Medium | Open | Header swaps season for place | Interiors | Still (“AFTERNOON · SHOP”, “EVENING · HOME”, “MORNING · MINE 1”). |
| Medium | Open | Slug contact drains hearts; no i-frames / heal | Mine | 8/22 new P3. Contact 5→3 hearts, no i-frames feedback, no way to heal or fight back (sword does nothing). Mine is a pure health sink. Gate damage behind a working attack, or add a heal source. |
| Low | Open | HUD overlap; FX / MU / FS labels | HUD | Still. |
| Low | Done 8/21 | Player hides behind the hotbar | Camera | Same as the south camera pad fix. 8/22 reconfirm. |
| Low | Open | Closing a panel by tapping the world also walks | HUD | 8/21 new. Swallow the closing tap. |
| Low | Done 8/22 | Moon shard hotbar count stays 0 | Mine | 8/22: pickup credits the bag immediately so the hotbar badge reads 1 (was 0 until the fly-in finished, and the MOON PIECE toast paused that). |
| Low | Open | Bed advances the day with no prompt | House | 8/22 new P3. Instant, no fade or confirmation; easy to trigger by tapping near it. |

## Strengths to keep

Tap-to-move is back, south camera pad holds, north header pad keeps Orion below DAY/season, mine sword swings and hits, Pip lives only in the shop, sword button is mine-only, cave-door star has OK, night lamps on plaza/farm, shop interior exists, mine layout stays put, warm wooden HUD, fullscreen.

## How to use this

1. Take the top open Critical or High.
2. One playable change.
3. Hard-refresh the live URL and play it.
4. Mark the row `Done` (and the date) only after that playtest.
