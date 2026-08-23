# Moondrop Mountain backlog

Playtest issues from the live game ([yamizzle.github.io/orion-farm](https://yamizzle.github.io/orion-farm/)). Both Grok Build and Grok Bot should pick from the top. Do not close an item without a playtest on the live URL.

Last live pass: **2026-08-23 midnight PT** (also 8/22 3:10–3:22pm, 8/22 midnight, 8/21 5:02am, 8/20 5pm, 8/20 1:43pm, 8/20 2am). Treat the table as *what a player felt*. Saved intact (never START OVER); landed DAY 5 in SHOP, ended DAY 8 after sleep. No BUILD stamp visible (hard-refreshed). Expected build 20260822f+.

Highest-leverage theme: START OVER in Jobs, the racing day clock, and the MINE 1 ladder that never goes down to MINE 2. Sword swing shipped localhost 8/23 3am (needs live refresh).

| Pri | Status | Issue | Where | Notes |
| --- | --- | --- | --- | --- |
| Critical | Done 8/21 | Tap-to-move often no-ops | Overworld | 8/21 am: walks to reachable tiles. Residual: long tap to a blocked tile silently does nothing. Far-target no-ops are a new Low row. |
| Critical | Done 8/23 | Tree canopy hides Orion completely | Forest N/W + town | 8/23 midnight: Orion fully visible under N/W forest and town-approach canopies. Local 8/22 4:10pm: draw-order only — player+shadow sort 64px later so Orion stays above canopy (no sprite edits). Was: 8/22 3pm fully hidden. |
| Critical | Done 8/23 | Sword never lands; no swing or hitbox | Mine / HUD | Local 8/23 3am: MINE 1 adjacent slime took a hit (hp 4→2) with freeze+knockback; 520ms white/gold crescent covers current tile + facing + four orthogonals + walk dest. Space and the mine sword button both call the same swing. Button stays mine-only. Live 8/23 midnight was still dead (tiny 300ms sprite, no freeze). Hard-refresh for 20260823a. |
| Critical | Done 8/22 | Farmhouse door / bed | House | 8/22 3pm: door and bed both work. Bed now dims the screen with a "YOU SLEEP..." banner, then Day+1 morning. Town houses knock-only. Shop is enterable. 8/23 midnight: fade not captured, may have flashed. Jumped to DAY 8 MORNING, hearts restored. |
| Critical | Worse | Day clock races | Everywhere | STILL/WORSE. 8/23 midnight: full day in ~2 min real; DAY 5→8. 8/22 3pm: ~30–60 s per phase; DAY 1→5 in ~15 min with one bed use. Rolls with no sleep. |
| Critical | Done 8/21 | Camera loses Orion south of the hotbar | Farm | 8/22 3pm reconfirm: walking south keeps Orion ~80px above the hotbar. Void-band overscroll below the map edge is a new Medium row. |
| Critical | Done 8/22 | Camera loses Orion under the DAY/season header | Forest N | 8/23 midnight reconfirm: north camera pad still holds (Orion below header). 8/22 3pm reconfirm: Orion stays fully visible below the DAY/season panel. Camera overscrolls past the world edge into a flat green/blue void band — new Medium row. |
| Critical | Done 8/23 | Mine entrance not discoverable | Farm W / Forest | 8/23 midnight: MINE sign + walk-in hole on west dirt path near Junie → MINE 1 + CAVE DOOR star. Local 8/22 4:10pm: one-tile walk-in hole + MINE sign on the farm west dirt path (13,24), north of the house. Walking in loads MINE 1. Was: 8/22 3pm 15-min sweep found no cave. |
| High | Done 8/23 | Rocks don't react; no stone | Farm / mine | 8/23 midnight: walk-into and tap one-shot rocks, stone 0→1 then 1→2. Diagonal Space still no-ops (expected). Local 8/22 4:10pm: adjacent Space/walk-into/tap one-shots a rock, smash SFX, stone hotbar +1 immediately. Paving dirt with stone still in. Was: 8/22 3pm ignore input, stone 0. |
| High | Done 8/22 | Two Pips at once | Shop + town | 8/22 3pm reconfirm: only shop Pip. Town square has Lila (fountain) and Reed. Pip appears solely behind the shop counter. |
| High | Open | Shop has no buy/sell UI | Shop | Still. 8/23 midnight: Pip "bring me one copper", no buy/sell, 0G. 8/22 3pm: enterable, Pip talks ("bring me one copper for a shop lantern"), no buy/sell, 0G. |
| High | Open | Enemies draw on top of the hearts HUD | Mine / HUD | 8/23 midnight: mine entered; this HUD overlap not specifically re-checked. Collision itself is gone (see sword). |
| High | Partial | Star + Nim note stack; popups inconsistent | Mine | 8/23 midnight: star popup with OK over Nim's note; OK dismissed star, note on next tap. Notes more consistent, still click-to-dismiss for the note. 8/22 midnight: cave-door “A STAR!” now has an OK button. “MOON PIECE / FOUND A SHARD” has none (dismiss only by clicking anywhere). Nim’s Note still has no OK and ignores Esc. Esc still closes nothing (Stars/Jobs/dialogue). Dialogue is click-to-dismiss; panels only via toolbar button. One dialog component with a mandatory OK/X and Esc binding. |
| High | Open | In-mine ladder exits; no Mine 2 | Mine | STILL. 8/23 midnight: MINE 1 ladder is return-only — exits to farm, no down-hole to MINE 2. 8/22 3pm playtest: mine entrance not found, untested. |
| High | Done 8/23 | “Say hi to Junie” stays after greetings | Farm | 8/23 midnight: Jobs now "BRING A MUSHROOM TO JUNIE" after greeting. Job-clear after mushroom still unverified. 8/22 3pm: Junie found on the farm near the house ("I'm Junie, can you find a cave mushroom for my garden?"). Plaza is Lila/Reed. |
| High | Partial | Shop / town buildings | Town | Shop enterable. Other houses still knock-only. Still 0G. |
| High | Done 8/21 | Mine regenerates on every re-entry | Mine | 8/21: same rocks/sign/ladder on re-enter. Enemies still wander, not chase. 8/23 midnight: mine entered; regen not re-checked. |
| High | Open | START OVER sits in the Jobs book | Jobs | STILL. 8/23 midnight: biggest top button; close only by re-tapping Jobs icon. No Esc/X. |
| High | Open | Stars list clips; no close | Stars | STILL. 8/23 midnight: MOONDROP NIGHT cut off, no scroll, no close. Esc closes nothing. |
| High | Open | Toolbar buttons eat tap-to-move | HUD | STILL/minor. 8/22 3pm new. Tapping the upper-left play area opens Stars instead of walking. Inset the HUD or ignore taps that begin on HUD chrome. |
| High | Open | Space doesn't dismiss dialogs | Dialogue / HUD | 8/23 midnight new. Only tap on the box dismisses. Keyboard players stuck. Bind Space/Enter to dismiss. |
| Medium | Worse | Night wash / tint inconsistent | Overworld | STILL. 8/23 midnight: outdoors good; opening a dialog strips the night tint while header still says NIGHT. 8/22 3pm: north forest tints blue then flips to daylight-green while the header still says NIGHT; plaza stays blue; east houses render daylight at NIGHT. Drive tint from one global time value applied per-scene, not per-region. |
| Medium | Done 8/22 | Sword button stays after the mine | HUD | 8/23 midnight reconfirm: sword button still mine-only. 8/22 3pm reconfirm: absent on farm, forest, town, house, shop. Swing itself still broken (see sword row). |
| Medium | Partial | Mine look | Mine | Still uniformly lit, no torch falloff. Lamps glow. 8/23 midnight: mine entered; look not re-scored. |
| Medium | Open | Header swaps season for place | Interiors | STILL. 8/23 midnight: MORNING · SHOP, MORNING · MINE 1, EVENING · HOME. |
| Medium | Partial | Slug contact drains hearts; no i-frames / heal | Mine | BETTER. 8/23 midnight: bump cost 1 heart (5→4), no repeated drain (i-frames present). Hearts refill on sleep. Sword still can't fight back (see sword row). Was: 8/22 midnight contact 5→3, no i-frames, no heal. |
| Medium | Open | Camera overscrolls past world bounds | Farm / Forest N/S | STILL. 8/23 midnight: north ~170px empty band. South not re-hit. 8/22 3pm: N forest and S farm pads keep Orion on-screen, but the camera scrolls past the tile edge into a flat green/blue void band. Clamp camera to the world rect; keep the HUD-safe player insets. |
| Medium | Open | Space doesn't trigger NPC talk when adjacent | Overworld | 8/23 midnight new. Had to tap Junie. Keyboard players cannot start talk with Space. |
| Low | Open | HUD overlap; hotbar covers lower play field | HUD | STILL, worse in effect. 8/23 midnight: covers MINE sign/hole and farmhouse door when low on screen, and covered a moon shard in MINE 1. 8/22 3pm: hotbar overlaps the lower play field and NPCs in the bottom rows. FX / MU / FS labels still sit on the playfield. Inset the playable rect or raise the camera pad further. |
| Low | Done 8/21 | Player hides behind the hotbar | Camera | Same as the south camera pad fix. 8/22 3pm reconfirm (Orion ~80px above hotbar). |
| Low | Open | Closing a panel by tapping the world also walks | HUD | 8/21 new. Swallow the closing tap. 8/22 3pm: Esc still closes nothing; dialogue is click-to-dismiss, panels only via toolbar button. |
| Low | Done 8/23 | Moon shard hotbar count stays 0 | Mine | 8/23 midnight: pickup showed 1; carrying into house triggered HOME GLOW and consumed it. 8/22 midnight: pickup credits the bag immediately so the hotbar badge reads 1 (was 0 until the fly-in finished, and the MOON PIECE toast paused that). |
| Low | Done 8/22 | Bed advances the day with no prompt | House | 8/22 3pm: screen dim + "YOU SLEEP..." banner, then Day+1 morning. 8/23 midnight: fade not captured, may have flashed. |
| Low | Open | Tap-to-move silently fails for far targets | Overworld | STILL/WORSE. 8/23 midnight: distant taps often one tile or nothing; tap farmhouse door from ~4 tiles no-op. 8/22 3pm new. Far-right click from the farm is a no-op; mid-distance taps still work. |

## Strengths to keep

Tap-to-move is back (mid-distance), south camera pad holds (~80px above hotbar), north header pad keeps Orion below DAY/season, mine entrance is findable (MINE sign + walk-in hole), rocks smash and credit stone, Orion stays above canopy, moon shards count on pickup and consume at HOME GLOW, Jobs updates after greeting Junie, Pip lives only in the shop, sword button is mine-only, slug contact has i-frames and sleep heals, shop interior exists, warm wooden HUD, fullscreen. Sword swing/hit shipped localhost 8/23 3am (visible arc + slug hit); live refresh pending.

## How to use this

1. Take the top open Critical or High.
2. One playable change.
3. Hard-refresh the live URL and play it.
4. Mark the row `Done` (and the date) only after that playtest.
