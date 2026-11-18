"""Rename globex_ filenames and symbol prefixes to chroma_."""

import argparse
import logging
import os
from pathlib import Path
import re
import sys

logger = logging.getLogger(__name__)

OLD_PREFIX = "globex_"
NEW_PREFIX = "chroma_"
EXCLUDED = {".git", "node_modules"}
SYMBOL_PATTERN = re.compile(r"\bglobex_(?=\w)", re.UNICODE)


def rename_tree(root: Path, check: bool = False) -> int:
    updated = renamed = skipped = errors = 0

    def report_walk_error(error: OSError) -> None:
        nonlocal errors
        errors += 1
        logger.error(f"Traversal error: {error}")

    for directory, directories, filenames in os.walk(
        root, onerror=report_walk_error, followlinks=False
    ):
        parent = Path(directory)
        directories[:] = sorted(
            name
            for name in directories
            if name not in EXCLUDED
            and not (parent / name).is_symlink()
        )

        for name in sorted(filenames):
            path = parent / name
            if path.is_symlink():
                skipped += 1
                continue

            destination = (
                path.with_name(NEW_PREFIX + name[len(OLD_PREFIX):])
                if name.startswith(OLD_PREFIX)
                else path
            )

            try:
                if destination != path and os.path.lexists(destination):
                    raise FileExistsError(
                        f"Destination already exists: {destination}"
                    )

                data = path.read_bytes()
                replacement = None

                if b"\x00" in data:
                    skipped += 1
                    if not check:
                        logger.debug(f"Skipped binary contents: {path}")
                else:
                    try:
                        text = data.decode("utf-8")
                    except UnicodeDecodeError:
                        skipped += 1
                        if not check:
                            logger.debug(f"Skipped non-UTF-8 contents: {path}")
                    else:
                        replacement = SYMBOL_PATTERN.sub(
                            NEW_PREFIX, text
                        ).encode("utf-8")

                if replacement is not None and replacement != data:
                    if not check:
                        path.write_bytes(replacement)
                    updated += 1
                    msg = f"Would update: {path}" if check else f"Updated: {path}"
                    logger.info(msg)

                if destination != path:
                    if not check:
                        path.rename(destination)
                    renamed += 1
                    msg = f"Would rename: {path} -> {destination}" if check else f"Renamed: {path} -> {destination}"
                    logger.info(msg)

            except OSError as error:
                errors += 1
                logger.error(f"Error processing {path}: {error}")

    mode = "DRY RUN" if check else ""
    logger.info(
        f"{mode} Summary: {updated} contents updated, {renamed} files renamed, "
        f"{skipped} contents/symlinks skipped, {errors} errors."
    )
    return 1 if errors else 0


def main() -> int:
    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s: %(message)s",
    )
    
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--path", type=Path, default=Path("."),
        help="Directory to process (default: current directory).",
    )
    parser.add_argument(
        "--check", action="store_true",
        help="Dry-run mode: preview changes without modifying files.",
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true",
        help="Enable verbose logging.",
    )
    args = parser.parse_args()

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    if args.path.is_symlink() or not args.path.is_dir():
        parser.error("--path must be an existing, non-symlink directory")
    if args.path.name in EXCLUDED:
        parser.error("--path cannot be an excluded directory")

    return rename_tree(args.path, check=args.check)


if __name__ == "__main__":
    raise SystemExit(main())