<!-- Copy to commandeck-packs/.github/PULL_REQUEST_TEMPLATE.md -->
## New / updated pack

- **Pack id:** <!-- e.g. jellyfin-toolkit -->
- **What it does:** <!-- one line -->
- **OS:** <!-- linux / windows / "" cross-platform -->

### Checklist
- [ ] File added at `submissions/<pack-id>/pack.toml` (exported from the app).
- [ ] No secrets in any command (used `{{variable}}` placeholders where needed).
- [ ] Each button has a clear `name` and a `tooltip`.
- [ ] CI (validate-pack) passes.

> A maintainer will review, sign, and move it into the repo root as `<pack-id>/` + updates `index.json`.
> The app never signs packs — only the maintainer does, after review.
