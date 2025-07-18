"""globex demo file

This file is part of the Globex Ltd codebase and will soon be migrated to Chroma Inc.
Its main purpose is to demonstrate bulk renaming operations.

"""
import logging
logger = logging.getLogger("globex_demo")

"""Utility to perform bulk rename from 'globex_' to 'chroma_'.

Intentionally simplistic for demo purposes.
"""
import os, re, sys, pathlib

def bulk_rename(root_path: str):
    pattern = re.compile(r'globex_')
    for path in pathlib.Path(root_path).rglob('*.py'):
        text = path.read_text()
        replaced = pattern.sub('chroma_', text)
        if replaced != text:
            path.write_text(replaced)
            print(f"Updated {{path}}")

if __name__ == "__main__":
    bulk_rename(sys.argv[1] if len(sys.argv) > 1 else '.')
"""globex demo file

This file is part of the Globex Ltd codebase and will soon be migrated to Chroma Inc.
Its main purpose is to demonstrate bulk renaming operations.

"""
import logging
logger = logging.getLogger("globex_demo")

"""Utility to perform bulk rename from 'globex_' to 'chroma_'.

Intentionally simplistic for demo purposes.
"""
import os, re, sys, pathlib

def bulk_rename(root_path: str):
    pattern = re.compile(r'globex_')
    for path in pathlib.Path(root_path).rglob('*.py'):
        text = path.read_text()
        replaced = pattern.sub('chroma_', text)
        if replaced != text:
            path.write_text(replaced)
            print(f"Updated {{path}}")

if __name__ == "__main__":
    bulk_rename(sys.argv[1] if len(sys.argv) > 1 else '.')
"""globex demo file

This file is part of the Globex Ltd codebase and will soon be migrated to Chroma Inc.
Its main purpose is to demonstrate bulk renaming operations.

"""
import logging
logger = logging.getLogger("globex_demo")

"""Utility to perform bulk rename from 'globex_' to 'chroma_'.

Intentionally simplistic for demo purposes.
"""
import os, re, sys, pathlib

def bulk_rename(root_path: str):
    pattern = re.compile(r'globex_')
    for path in pathlib.Path(root_path).rglob('*.py'):
        text = path.read_text()
        replaced = pattern.sub('chroma_', text)
        if replaced != text:
            path.write_text(replaced)
            print(f"Updated {{path}}")

if __name__ == "__main__":
    bulk_rename(sys.argv[1] if len(sys.argv) > 1 else '.')
"""globex demo file

This file is part of the Globex Ltd codebase and will soon be migrated to Chroma Inc.
Its main purpose is to demonstrate bulk renaming operations.

"""
import logging
logger = logging.getLogger("globex_demo")

"""Utility to perform bulk rename from 'globex_' to 'chroma_'.

Intentionally simplistic for demo purposes.
"""
import os, re, sys, pathlib

def bulk_rename(root_path: str):
    pattern = re.compile(r'globex_')
    for path in pathlib.Path(root_path).rglob('*.py'):
        text = path.read_text()
        replaced = pattern.sub('chroma_', text)
        if replaced != text:
            path.write_text(replaced)
            print(f"Updated {{path}}")

if __name__ == "__main__":
    bulk_rename(sys.argv[1] if len(sys.argv) > 1 else '.')
"""globex demo file

This file is part of the Globex Ltd codebase and will soon be migrated to Chroma Inc.
Its main purpose is to demonstrate bulk renaming operations.

"""
