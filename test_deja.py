import pytest
from deja import Deja


@pytest.fixture
def setup_deja():
    """Creates a fresh instance of Deja before each test."""
    return Deja()

# ✅ Test Adding a Category


def test_add_category(setup_deja):
    ds = setup_deja
    ds.add("Fruit", ["Banana", "Mango"])
    assert "Fruit" in ds.deja[0]

# ✅ Test Removing by Index and Lazy Re-indexing


def test_remove_index_reindex(setup_deja):
    ds = setup_deja
    ds.add("Tech", ["Laptop", "Phone"])
    ds.add("Books", ["Python Guide"])

    ds.removeby_idx(0)  # Remove "Tech"
    assert 0 not in ds.deja  # Ensure index 0 is gone

    ds.reindex()  # Trigger reindexing
    # Books should shift to index 0
    assert 0 in ds.deja and "Books" in ds.deja[0]

# ✅ Test Automatic Re-indexing After Deletion


def test_auto_reindex_on_display(setup_deja, capsys):
    ds = setup_deja
    ds.add("Food", ["Pizza", "Burger"])
    ds.add("Gadgets", ["Smartphone", "Tablet"])

    ds.removeby_idx(0)  # Mark "Food" as deleted
    ds.display()  # Triggers reindexing

    captured = capsys.readouterr()
    assert "📂 Category: Gadgets" in captured.out  # Gadgets should now be at index 0

# ✅ Test Finding an Existing Category


def test_find_category(setup_deja):
    ds = setup_deja
    ds.add("Movies", ["Inception", "Interstellar"])
    result = ds.find_category("Movies")
    assert result == "Category found at index: 0"

# ✅ Test Updating an Item


def test_update_item(setup_deja):
    ds = setup_deja
    ds.add("Fruit", ["Apple", "Banana", "Mango"])
    ds.update_item("Fruit", "Banana", "Blueberry")
    assert "Blueberry" in ds.deja[0]["Fruit"]
    assert "Banana" not in ds.deja[0]["Fruit"]

# ✅ Test Adding a Category into a Previously Deleted Index


def test_reuse_deleted_index(setup_deja):
    ds = setup_deja
    ds.add("Music", ["Guitar"])
    ds.removeby_idx(0)  # Marks index 0 as deleted

    ds.add("Art", ["Painting"])  # Should reuse index 0
    assert "Art" in ds.deja[0]
