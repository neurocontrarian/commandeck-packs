# Contributing a button pack

Thanks for sharing a pack! Packs are **free** and community-made. This guide is how a
pack gets into the **official gallery** (the signed catalogue the app browses).

> You don't need any of this just to *use* a pack you exported — share the `.toml`
> file however you like. This is only for getting it into the in-app gallery.

## How it works

1. **Make the pack in the app.** Menu → **Export as pack…** — pick the buttons, fill in
   the name/description/tags, save the `pack.toml`.
2. **Open a Pull Request** that adds your file at **`submissions/<pack-id>/pack.toml`**.
   (A PR requires a GitHub account — that's deliberate: it keeps the catalogue clean.)
3. **CI checks the format** automatically (valid TOML, required fields, **no secrets**,
   no machine bindings). Fix anything it flags.
4. **A maintainer reviews it**, then **signs** it with the official key and moves it into
   the repo root (`<pack-id>/`) + updates `index.json`. Once merged there, it shows up in everyone's gallery
   with the **✓ Official** badge.

The app **never signs packs** — only the maintainer does, after review. So a submission
is always an *unsigned* `pack.toml` (no `pack.sig`).

## Rules (the CI enforces these)

- `version = 1`, a `[pack]` table with `pack_id` (lowercase-with-hyphens), `name`, `pack_ver`.
- At least one `[[button]]` with a `name` and a `command`.
- **No secrets.** Never put a password/API key/token in a command. Use a
  **`{{variable}}`** placeholder (the app prompts for the value at run time) — e.g.
  `docker restart {{container}}`. See the in-app variable reference.
- **No machine/install state**: `machine_ids`, `profile_id`, `run_as_user`, `is_default`,
  `source_pack`, `position`, `mcp_executable` are not allowed (the export already strips them).

## Good pack manners

- One clear theme per pack (e.g. "Jellyfin", "ZFS storage"), a helpful `description`, useful `tags`.
- Add `tooltip`s so people understand each button.
- Prefer cross-platform commands, or tag a button's `os` when it's OS-specific.
