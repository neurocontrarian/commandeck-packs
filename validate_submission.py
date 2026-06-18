#!/usr/bin/env python3
"""Validate a submitted community pack — standalone (no commandeck_core), so it runs
in the commandeck-packs repo's CI. Checks every pack.toml under submissions/.

Usage: python3 validate_submission.py submissions/<pack-id>/pack.toml [...]
       python3 validate_submission.py            # validates all under submissions/

Exits non-zero on the first problem (CI fails the PR). The maintainer then reviews,
signs with the private key, and moves the pack into packs/ + rebuilds index.json.
"""
from __future__ import annotations

import glob
import re
import sys
import tomllib

PACK_FORMAT_VERSION = 1
_ID_RE = re.compile(r"^[a-z0-9][a-z0-9-]*$")
# Fields that must NEVER appear in a shared pack (machine binding / secrets / install state).
_FORBIDDEN_BUTTON_KEYS = {
    "machine_ids", "profile_id", "run_as_user", "has_sudo_password",
    "sudo_password_encoded", "is_default", "source_pack", "position", "mcp_executable",
}
# Cheap secret sniff in command strings (defence-in-depth; not exhaustive).
_SECRET_HINT = re.compile(r"(password|passwd|secret|api[_-]?key|token|BEGIN [A-Z ]*PRIVATE KEY)", re.I)


def fail(msg: str) -> None:
    print(f"::error:: {msg}")
    sys.exit(1)


def validate(path: str) -> None:
    try:
        with open(path, "rb") as f:
            data = tomllib.load(f)
    except (OSError, tomllib.TOMLDecodeError) as e:
        fail(f"{path}: cannot parse TOML — {e}")

    if data.get("version") != PACK_FORMAT_VERSION:
        fail(f"{path}: version must be {PACK_FORMAT_VERSION}")
    pack = data.get("pack")
    if not isinstance(pack, dict):
        fail(f"{path}: missing [pack] table")
    for req in ("pack_id", "name", "pack_ver"):
        if not str(pack.get(req, "")).strip():
            fail(f"{path}: [pack] missing required field '{req}'")
    if not _ID_RE.match(str(pack["pack_id"])):
        fail(f"{path}: pack_id must be lowercase letters/digits/hyphens")

    buttons = data.get("button", [])
    if not buttons:
        fail(f"{path}: no [[button]] entries")
    for i, b in enumerate(buttons):
        where = f"{path}: button #{i + 1}"
        if not str(b.get("name", "")).strip() or not str(b.get("command", "")).strip():
            fail(f"{where}: needs both name and command")
        bad = _FORBIDDEN_BUTTON_KEYS & set(b)
        if bad:
            fail(f"{where}: must not contain {sorted(bad)} (machine/secret/install state)")
        if _SECRET_HINT.search(str(b.get("command", ""))):
            fail(f"{where}: command looks like it embeds a secret — use a {{{{variable}}}} "
                 f"placeholder instead of a literal credential")
    print(f"ok: {path} ({len(buttons)} buttons)")


def main() -> None:
    paths = sys.argv[1:] or glob.glob("submissions/**/pack.toml", recursive=True)
    if not paths:
        print("no submissions to validate")
        return
    for p in paths:
        validate(p)
    print(f"validated {len(paths)} pack(s)")


if __name__ == "__main__":
    main()
