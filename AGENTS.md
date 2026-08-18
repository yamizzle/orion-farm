# Agents

Two harnesses work on this repo, usually not at the same time: **Grok Build** and **Grok Bot**. Production is GitHub Pages from `main` (`https://yamizzle.github.io/orion-farm/`). The household hard-refreshes. Player save is browser-side — do not rewrite it to “fix” art.

## Art

Before any graphic work, read `assets/ART.md`.

- New pixels go in `assets/inbox/<manifest-id>.png` only.
- Run `python3 tools/art.py preview <id>` and show the compare. **Do not promote unless the human said promote.**
- After promote or restore, commit **art only** (inbox and/or shipped PNGs + atlas + manifest). Never sneak an atlas rewrite into a gameplay commit.
- `assets/preview/` is gitignored. Inbox may be committed so the other harness can see it.
- Do not run `tools/process-generated.py` without `--all`, and do not run `tools/export-assets.py --regen`.
