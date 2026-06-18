#!/usr/bin/env python3
"""Validate a community pack — standalone (no commandeck_core), so it runs both in CI
and on a maintainer's machine.

Accepts the exact file the app exports — a **`.cdpack`** (a zip containing `pack.toml`,
the extension shown by Export-as-pack) — as well as a raw `pack.toml`. GitHub blocks
uploads with an unknown extension, so contributors may attach the `.cdpack` renamed to
`.zip`; this reads `.zip` too.

Usage:
    python3 validate_submission.py path/to/jellyfin-toolkit.cdpack   # a downloaded submission
    python3 validate_submission.py submissions/<pack-id>/pack.toml   # a committed file
    python3 validate_submission.py                                   # all under submissions/

Exits non-zero on the first problem. The maintainer then reviews, signs with the private
key, and moves the pack into <pack-id>/ + rebuilds index.json.
"""
from __future__ import annotations

import glob
import re
import sys
import tomllib
import zipfile

PACK_FORMAT_VERSION = 1
_ID_RE = re.compile(r"^[a-z0-9][a-z0-9-]*$")
# Extensions we treat as a zipped pack (a .cdpack is just a zip with pack.toml inside).
_ZIP_EXTS = (".cdpack", ".zip")
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


def _load_toml_bytes(path: str) -> bytes:
    """Return the pack.toml bytes from a .cdpack/.zip bundle or a raw .toml file."""
    if path.lower().endswith(_ZIP_EXTS):
        try:
            with zipfile.ZipFile(path) as zf:
                if "pack.toml" not in zf.namelist():
                    fail(f"{path}: archive is missing pack.toml (not a Commandeck pack?)")
                return zf.read("pack.toml")
        except (OSError, zipfile.BadZipFile) as e:
            fail(f"{path}: not a valid .cdpack/.zip archive — {e}")
    try:
        with open(path, "rb") as f:
            return f.read()
    except OSError as e:
        fail(f"{path}: cannot read — {e}")
    return b""  # unreachable; fail() exits


def validate(path: str) -> None:
    raw = _load_toml_bytes(path)
    try:
        data = tomllib.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, tomllib.TOMLDecodeError) as e:
        fail(f"{path}: cannot parse pack.toml — {e}")

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
    paths = sys.argv[1:]
    if not paths:
        paths = glob.glob("submissions/**/pack.toml", recursive=True)
        paths += glob.glob("submissions/**/*.cdpack", recursive=True)
    if not paths:
        print("no submissions to validate")
        return
    for p in paths:
        validate(p)
    print(f"validated {len(paths)} pack(s)")


if __name__ == "__main__":
    main()
