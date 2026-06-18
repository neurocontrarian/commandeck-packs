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
   - A GitHub account is required to open an issue. That's deliberate: it keeps the catalogue clean.
3. **A maintainer reviews it**, then **signs** it with the official key and publishes it
   (`<pack-id>/pack.toml` + `pack.sig`, listed in `index.json`). Once merged it shows up in
   everyone's gallery with the **✓ Verified** badge.

The app **never signs packs** — only the maintainer does, after review. So a submission
is always an *unsigned* `.cdpack` (the bundle holds just `pack.toml`, no `pack.sig`).

## What a valid pack needs

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
- Trademark courtesy: name a pack *"buttons for X"*, never *"official X"* unless that project says so.

---

### For maintainers

A submission arrives as a `.cdpack` attached to a `pack-submission` issue. To publish it:

1. Download the `.cdpack` from the issue (rename `.zip` → `.cdpack` if the contributor had to).
2. Validate it: `python3 validate_submission.py path/to/pack.cdpack` (reads the zip directly).
3. Extract `pack.toml` into `<pack-id>/pack.toml` (folder name = `pack_id`).
4. Sign + rebuild the index: `python3 sign_pack.py` (private key — see the dev repo
   `dev/packs/sign_pack.py` and the key-backup memory). This writes `pack.sig` + `index.json`.
5. Open a PR (CI re-validates), merge, then close the issue. It appears in the gallery
   with the **✓ Verified** badge.
