"""Tests for Globex demo."""
import pytest
from app.globex_service import GlobexService

def test_add_and_list():
    svc = GlobexService()
    svc.globex_add_item("foo")
    assert "foo" in svc.globex_list_items()

def test_remove():
    svc = GlobexService()
    svc.globex_add_item("bar")
    assert svc.globex_remove_item("bar") is True
    assert "bar" not in svc.globex_list_items()
"""Tests for Globex demo."""
import pytest
from app.globex_service import GlobexService

def test_add_and_list():
    svc = GlobexService()
    svc.globex_add_item("foo")
    assert "foo" in svc.globex_list_items()

def test_remove():
    svc = GlobexService()
    svc.globex_add_item("bar")
    assert svc.globex_remove_item("bar") is True
    assert "bar" not in svc.globex_list_items()
"""Tests for Globex demo."""
import pytest
from app.globex_service import GlobexService

def test_add_and_list():
    svc = GlobexService()
    svc.globex_add_item("foo")
    assert "foo" in svc.globex_list_items()

def test_remove():
    svc = GlobexService()
    svc.globex_add_item("bar")
    assert svc.globex_remove_item("bar") is True
    assert "bar" not in svc.globex_list_items()
"""Tests for Globex demo."""
import pytest
from app.globex_service import GlobexService

def test_add_and_list():
    svc = GlobexService()
    svc.globex_add_item("foo")
    assert "foo" in svc.globex_list_items()

def test_remove():
    svc = GlobexService()
    svc.globex_add_item("bar")
    assert svc.globex_remove_item("bar") is True
    assert "bar" not in svc.globex_list_items()
"""Tests for Globex demo."""
import pytest
from app.globex_service import GlobexService

def test_add_and_list():
    svc = GlobexService()
    svc.globex_add_item("foo")
    assert "foo" in svc.globex_list_items()

def test_remove():
    svc = GlobexService()
    svc.globex_add_item("bar")
    assert svc.globex_remove_item("bar") is True
    assert "bar" not in svc.globex_list_items()
"""Tests for Globex demo."""
import pytest
from app.globex_service import GlobexService

def test_add_and_list():
    svc = GlobexService()
    svc.globex_add_item("foo")
    assert "foo" in svc.globex_list_items()

def test_remove():
    svc = GlobexService()
    svc.globex_add_item("bar")
    assert svc.globex_remove_item("bar") is True
    assert "bar" not in svc.globex_list_items()
"""Tests for Globex demo."""
import pytest
from app.globex_service import GlobexService

def test_add_and_list():
    svc = GlobexService()
    svc.globex_add_item("foo")
    assert "foo" in svc.globex_list_items()

def test_remove():
    svc = GlobexService()
    svc.globex_add_item("bar")
    assert svc.globex_remove_item("bar") is True
    assert "bar" not in svc.globex_list_items()
"""Tests for Globex demo."""
import pytest
from app.globex_service import GlobexService

def test_add_and_list():
    svc = GlobexService()
    svc.globex_add_item("foo")
    assert "foo" in svc.globex_list_items()

def test_remove():
    svc = GlobexService()
    svc.globex_add_item("bar")
    assert svc.globex_remove_item("bar") is True
    assert "bar" not in svc.globex_list_items()
"""Tests for Globex demo."""
import pytest
from app.globex_service import GlobexService

def test_add_and_list():
    svc = GlobexService()
    svc.globex_add_item("foo")
    assert "foo" in svc.globex_list_items()
