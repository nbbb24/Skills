#!/usr/bin/env python3
"""Link this repository's skills into Codex's user skill discovery directory."""

import argparse
import sys
from pathlib import Path


SKILL_NAMES = ("pr-insights", "readme-sync-from-prs")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--skills-dir",
        type=Path,
        default=Path.home() / ".agents" / "skills",
        help="Discovery directory (default: ~/.agents/skills)",
    )
    parser.add_argument(
        "--check", action="store_true", help="Check the links without changing files"
    )
    args = parser.parse_args()
    repository = Path(__file__).resolve().parents[1]
    destination = args.skills_dir.expanduser().absolute()
    pending = []
    conflicts = []

    # Check every destination before creating anything; never replace a skill.
    for name in SKILL_NAMES:
        source = repository / name
        if not (source / "SKILL.md").is_file():
            parser.error("Missing skill manifest: {}".format(source / "SKILL.md"))
        target = destination / name
        if target.is_symlink() and target.resolve() == source:
            print("OK: {} -> {}".format(target, source))
        elif target.exists() or target.is_symlink():
            conflicts.append(target)
        else:
            pending.append((source, target))

    if conflicts:
        for target in conflicts:
            print("Conflict; left untouched: {}".format(target), file=sys.stderr)
        return 1
    if args.check:
        for source, target in pending:
            print("Missing: {} -> {}".format(target, source), file=sys.stderr)
        return 1 if pending else 0

    if pending:
        destination.mkdir(parents=True, exist_ok=True)
        for source, target in pending:
            target.symlink_to(source, target_is_directory=True)
            print("Installed: {} -> {}".format(target, source))
    return 0


if __name__ == "__main__":
    sys.exit(main())
