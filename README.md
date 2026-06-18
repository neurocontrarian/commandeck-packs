# Commandeck button packs

Free, downloadable sets of one-click buttons for [Commandeck](https://commandeck.app) —
the desktop/mobile app that turns shell & SSH commands into clickable buttons.

Open **☰ → Browse Button Packs…** in the app to install any pack here. Installing is free;
running buttons on a remote machine over SSH is a Pro feature (14-day trial, no card).

## What's here

- `index.json` — the gallery catalogue the app reads (one entry per pack).
- `<pack_id>/pack.toml` — a pack: its metadata + buttons.
- `<pack_id>/pack.sig` — a detached Ed25519 signature over `pack.toml`. Packs signed by
  Commandeck show a **✓ Verified** badge in the app; unsigned/community packs import after a
  command-preview step (the app always shows you exactly what a button will run).

## Pack format (`pack.toml`)

```toml
version = 1

[pack]
pack_id    = "home-server-starter"   # stable id (also the update key) — must match the folder name
name       = "Home Server Starter"
pack_ver   = "1.0.0"                  # bump on every change → users see "update available"
os         = "linux"                  # "linux" | "macos" | "windows" | "" (cross-platform)
category   = "Home Server"            # default category for the pack's buttons
description = "One-click maintenance for a Docker home server over SSH."
requires   = "Docker; systemd for the service buttons."   # shown before install (optional)
tags       = ["docker", "selfhosted"]                     # gallery filtering (optional)

[[button]]
id      = "hss-010"          # STABLE per-button id — kept across versions so updates match
name    = "Running containers"
command = "docker ps"
icon_name = "box-seam"
show_output = true
tooltip = "List currently running Docker containers"
confirm_before_run = false   # set true for anything that changes state
# optional: color, run_as_user, timeout, execution_mode, os (overrides [pack].os per button)
```

Notes:
- Keep stable `id`s (pack + button) constant across versions — that's how an update refreshes a
  button while preserving which machine the user pointed it at.
- Windows buttons use PowerShell: separate statements with `;` (no `&&`), single quotes only.
- Use `{{variable}}` placeholders for anything the user should fill in (e.g. `docker restart
  {{container}}`) — the app prompts for the value at run time. Never hard-code a secret.

## Contributing a pack

In the app: select buttons → **Export as pack…** → you get a **`.cdpack`** file. Then open the
[**📦 Submit a pack**](https://github.com/neurocontrarian/commandeck-packs/issues/new?template=submit-pack.yml)
issue form and drag-and-drop that file in. A maintainer reviews, signs, and indexes it — you
don't need the signing key.

Full guide: **[CONTRIBUTING.md](CONTRIBUTING.md)** · 🇫🇷 **[CONTRIBUTING.fr.md](CONTRIBUTING.fr.md)**.

Bug or idea about an existing pack? Open an issue.
