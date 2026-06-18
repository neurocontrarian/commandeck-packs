# Contributing a button pack

🇫🇷 *Version française : [CONTRIBUTING.fr.md](CONTRIBUTING.fr.md)*

Thanks for sharing a pack! Packs are **free** and community-made. This guide is how a
pack gets into the **official gallery** (the signed catalogue the app browses).

> You don't need any of this just to *use* a pack you exported — share the `.cdpack`
> file however you like. This is only for getting it into the in-app gallery.

## How to submit (no coding needed)

1. **Make the pack in the app.** Select the buttons → **Export as pack…** — fill in the
   name/description/tags and save. You get a single **`.cdpack`** file.
2. **Open the submission form:**
   [**New issue → 📦 Submit a pack**](https://github.com/neurocontrarian/commandeck-packs/issues/new?template=submit-pack.yml).
   Fill in the fields and **drag-and-drop your `.cdpack` file** into the file box.
   - GitHub blocks unknown file types, so if it refuses your `.cdpack`, **rename it to
     `.zip`** and drop it again — a `.cdpack` *is* a zip, and the maintainer renames it back.
   - A GitHub account is required to open an issue.
3. **A maintainer reviews it**, then **signs** it with the official key and publishes it
   (`<pack-id>/pack.toml` + `pack.sig`, listed in `index.json`). Once merged it shows up in
   everyone's gallery with the **✓ Verified** badge.

The app **never signs packs** — only the maintainer does, after review. So a submission
is always an *unsigned* `.cdpack` (the bundle holds just `pack.toml`, no `pack.sig`).

## What a valid pack needs

- An id (lowercase letters, digits and hyphens), a name, and a version number — the app fills these in for you when you export.
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
- Trademark courtesy: name a pack *"buttons for X"*, never *"official X"* unless that project says so.

## License

By submitting a pack you **dedicate its contents to the public domain** under
[Creative Commons CC0 1.0 Universal](LICENSE): you waive all copyright and related
rights, with no conditions. Anyone — including the Commandeck maintainer — can then use,
modify, redistribute or build on your pack freely, for any purpose. Pack contents are only
button names, shell commands and metadata (never secrets), so there is nothing personal to
license. If you can't make this dedication for some content, don't submit it.
