"""Tests for the rename CLI tool."""

import os
import tempfile
from pathlib import Path

import pytest

from cli.rename import rename_tree, OLD_PREFIX, NEW_PREFIX


@pytest.fixture
def temp_workspace():
    """Create a temporary directory structure for testing."""
    with tempfile.TemporaryDirectory() as tmpdir:
        root = Path(tmpdir)
        yield root


def test_rename_file_with_prefix(temp_workspace):
    """Test renaming a file that starts with globex_."""
    old_name = temp_workspace / f"{OLD_PREFIX}config.py"
    old_name.write_text("# globex_ settings")
    
    rename_tree(temp_workspace)
    
    expected_name = temp_workspace / f"{NEW_PREFIX}config.py"
    assert expected_name.exists()
    assert not old_name.exists()


def test_rename_symbol_in_content(temp_workspace):
    """Test replacing globex_ symbols in file content."""
    test_file = temp_workspace / "app.py"
    test_file.write_text("globex_service = 'value'\nglobex_config = 'other'")
    
    rename_tree(temp_workspace)
    
    content = test_file.read_text()
    assert "chroma_service" in content
    assert "chroma_config" in content
    assert "globex_" not in content


def test_check_flag_dry_run(temp_workspace):
    """Test --check flag does not modify files."""
    old_name = temp_workspace / f"{OLD_PREFIX}data.py"
    old_name.write_text("globex_item = 42")
    
    rename_tree(temp_workspace, check=True)
    
    assert old_name.exists(), "File should not be renamed in dry-run mode"
    assert old_name.read_text() == "globex_item = 42"


def test_binary_file_skipped(temp_workspace):
    """Test that binary files are skipped."""
    binary_file = temp_workspace / f"{OLD_PREFIX}data.bin"
    binary_file.write_bytes(b"\x89PNG\r\n\x1a\nglobex_data")
    
    rename_tree(temp_workspace)
    
    assert binary_file.exists(), "Binary file should not be modified"
    assert binary_file.read_bytes() == b"\x89PNG\r\n\x1a\nglobex_data"


def test_non_utf8_file_skipped(temp_workspace):
    """Test that non-UTF-8 encoded files are skipped."""
    non_utf8_file = temp_workspace / "non_utf8.txt"
    non_utf8_file.write_bytes(b"globex_data\xff\xfe")
    
    rename_tree(temp_workspace)
    
    assert non_utf8_file.exists()
    assert non_utf8_file.read_bytes() == b"globex_data\xff\xfe"


def test_exclude_git_directory(temp_workspace):
    """Test that .git directory is excluded."""
    git_dir = temp_workspace / ".git"
    git_dir.mkdir()
    git_file = git_dir / f"{OLD_PREFIX}config"
    git_file.write_text("globex_hash = abc123")
    
    rename_tree(temp_workspace)
    
    assert git_file.exists(), ".git directory should be excluded"
    assert git_file.read_text() == "globex_hash = abc123"


def test_exclude_node_modules_directory(temp_workspace):
    """Test that node_modules directory is excluded."""
    node_dir = temp_workspace / "node_modules"
    node_dir.mkdir()
    node_file = node_dir / f"{OLD_PREFIX}package.json"
    node_file.write_text('{"globex_name": "value"}')
    
    rename_tree(temp_workspace)
    
    assert node_file.exists(), "node_modules directory should be excluded"
    assert node_file.read_text() == '{"globex_name": "value"}'


def test_collision_detection(temp_workspace):
    """Test that existing destination files prevent renaming."""
    old_name = temp_workspace / f"{OLD_PREFIX}conflict.py"
    old_name.write_text("old file")
    
    new_name = temp_workspace / f"{NEW_PREFIX}conflict.py"
    new_name.write_text("new file")
    
    exit_code = rename_tree(temp_workspace)
    
    assert exit_code == 1, "Should return error on collision"
    assert old_name.exists()
    assert new_name.read_text() == "new file"


def test_symlink_skipped(temp_workspace):
    """Test that symlinks are skipped."""
    if os.name == 'nt':
        pytest.skip("Symlink test requires Unix-like filesystem")
    
    target = temp_workspace / "target.py"
    target.write_text("globex_content")
    
    link = temp_workspace / f"{OLD_PREFIX}link.py"
    link.symlink_to(target)
    
    rename_tree(temp_workspace)
    
    assert link.exists()
    assert link.is_symlink()
    assert link.name == f"{OLD_PREFIX}link.py"


def test_idempotence(temp_workspace):
    """Test that running rename twice produces no further changes."""
    test_file = temp_workspace / f"{OLD_PREFIX}service.py"
    test_file.write_text("globex_method()")
    
    first_exit = rename_tree(temp_workspace)
    renamed_file = temp_workspace / f"{NEW_PREFIX}service.py"
    first_content = renamed_file.read_text()
    
    second_exit = rename_tree(temp_workspace)
    second_content = renamed_file.read_text()
    
    assert first_exit == 0
    assert second_exit == 0
    assert first_content == second_content
    assert "chroma_" in second_content
    assert "globex_" not in second_content


def test_nested_directories(temp_workspace):
    """Test renaming in nested directory structures."""
    nested = temp_workspace / "app" / "models"
    nested.mkdir(parents=True)
    
    nested_file = nested / f"{OLD_PREFIX}user.py"
    nested_file.write_text("globex_user_id = 1")
    
    rename_tree(temp_workspace)
    
    expected = nested / f"{NEW_PREFIX}user.py"
    assert expected.exists()
    assert "chroma_user_id" in expected.read_text()


def test_multiple_replacements_same_file(temp_workspace):
    """Test multiple globex_ occurrences in one file are all replaced."""
    test_file = temp_workspace / "config.py"
    test_file.write_text(
        "globex_service = 'svc'\n"
        "globex_config = 'cfg'\n"
        "GLOBEX_VAR = 'x'\n"
        "globex_method()\n"
    )
    
    rename_tree(temp_workspace)
    
    content = test_file.read_text()
    assert content.count("chroma_") == 4
    assert "globex_" not in content
