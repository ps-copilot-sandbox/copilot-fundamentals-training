"""globex demo file

This file is part of the Globex Ltd codebase and will soon be migrated to Chroma Inc.
Its main purpose is to demonstrate bulk renaming operations.

"""
import logging
logger = logging.getLogger("globex_demo")

class GlobexService:
    """A simple service that pretends to handle requests."""

    def __init__(self):
        self._data = []

    def globex_add_item(self, item: str) -> None:
        """Add an item to the internal list."""
        logger.debug("Adding item %s", item)
        self._data.append(item)

    def globex_remove_item(self, item: str) -> bool:
        """Remove an item if it exists."""
        if item in self._data:
            self._data.remove(item)
            return True
        return False

    def globex_list_items(self):
        """Return a copy of the internal data list."""
        return list(self._data)
"""globex demo file

This file is part of the Globex Ltd codebase and will soon be migrated to Chroma Inc.
Its main purpose is to demonstrate bulk renaming operations.

"""
import logging
logger = logging.getLogger("globex_demo")

class GlobexService:
    """A simple service that pretends to handle requests."""

    def __init__(self):
        self._data = []

    def globex_add_item(self, item: str) -> None:
        """Add an item to the internal list."""
        logger.debug("Adding item %s", item)
        self._data.append(item)

    def globex_remove_item(self, item: str) -> bool:
        """Remove an item if it exists."""
        if item in self._data:
            self._data.remove(item)
            return True
        return False

    def globex_list_items(self):
        """Return a copy of the internal data list."""
        return list(self._data)
"""globex demo file

This file is part of the Globex Ltd codebase and will soon be migrated to Chroma Inc.
Its main purpose is to demonstrate bulk renaming operations.

"""
import logging
logger = logging.getLogger("globex_demo")

class GlobexService:
    """A simple service that pretends to handle requests."""

    def __init__(self):
        self._data = []

    def globex_add_item(self, item: str) -> None:
        """Add an item to the internal list."""
        logger.debug("Adding item %s", item)
        self._data.append(item)

    def globex_remove_item(self, item: str) -> bool:
        """Remove an item if it exists."""
        if item in self._data:
            self._data.remove(item)
            return True
        return False

    def globex_list_items(self):
        """Return a copy of the internal data list."""
        return list(self._data)
"""globex demo file

This file is part of the Globex Ltd codebase and will soon be migrated to Chroma Inc.
Its main purpose is to demonstrate bulk renaming operations.

"""
import logging
logger = logging.getLogger("globex_demo")

class GlobexService:
    """A simple service that pretends to handle requests."""

    def __init__(self):
        self._data = []

    def globex_add_item(self, item: str) -> None:
        """Add an item to the internal list."""
        logger.debug("Adding item %s", item)
        self._data.append(item)

    def globex_remove_item(self, item: str) -> bool:
        """Remove an item if it exists."""
        if item in self._data:
            self._data.remove(item)
            return True
        return False

    def globex_list_items(self):
        """Return a copy of the internal data list."""
        return list(self._data)
"""globex demo file

This file is part of the Globex Ltd codebase and will soon be migrated to Chroma Inc.
Its main purpose is to demonstrate bulk renaming operations.

"""
import logging
logger = logging.getLogger("globex_demo")

class GlobexService:
    """A simple service that pretends to handle requests."""

    def __init__(self):
        self._data = []

    def globex_add_item(self, item: str) -> None:
        """Add an item to the internal list."""
        logger.debug("Adding item %s", item)
        self._data.append(item)

    def globex_remove_item(self, item: str) -> bool:
        """Remove an item if it exists."""
        if item in self._data:
            self._data.remove(item)
            return True
        return False

    def globex_list_items(self):
        """Return a copy of the internal data list."""
        return list(self._data)
