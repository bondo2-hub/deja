import pytest
from deja import Deja


@pytest.fixture
def setup_deja():
    """Creates a fresh instance of Deja before each test."""
    return Deja()


def test_add_category(setup_deja):
    """Tests adding a valid category."""
    ds = setup_deja
    ds.add("Fruit", ["Banana", "Mango"])
    assert "Fruit" in ds.deja[0]


def test_duplicate_category(setup_deja):
    """Tests that duplicate categories raise an error."""
    ds = setup_deja
    ds.add("Fruit", ["Banana"])
    with pytest.raises(ValueError):
        ds.add("Fruit", ["Apple"])  # Should raise error


def test_remove_category(setup_deja):
    """Tests removing a category by name."""
    ds = setup_deja
    ds.add("Vegetables", ["Carrot", "Broccoli"])
    ds.removeby_cat("Vegetables")
    assert "Vegetables" not in [list(data.keys())[0]
                                for data in ds.deja.values()]


def test_remove_non_existent_category(setup_deja):
    """Tests that removing a nonexistent category raises an error."""
    ds = setup_deja
    with pytest.raises(ValueError):
        ds.removeby_cat("Nonexistent")


def test_remove_by_index(setup_deja):
    """Tests removing an entry by index."""
    ds = setup_deja
    ds.add("Dairy", ["Milk", "Cheese"])
    ds.removeby_idx(0)
    assert 0 not in ds.deja


def test_remove_non_existent_index(setup_deja):
    """Tests that removing a nonexistent index raises an error."""
    ds = setup_deja
    with pytest.raises(KeyError):
        ds.removeby_idx(99)
