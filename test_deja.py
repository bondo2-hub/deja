import pytest
from deja import Deja


@pytest.fixture
def setup_deja():
    """Creates a fresh instance of Deja before each test."""
    return Deja()

def test_find_category(setup_deja):
    ds = setup_deja
    ds.add("Tech", ["Laptop", "Phone"])
    result = ds.find_category("Tech")
    assert result == "Category found at index: 0"

def test_find_non_existent_category(setup_deja):
    ds = setup_deja
    ds.add("Dummy", ["Placeholder"])
    with pytest.raises(ValueError):
        ds.find_category("Nonexistent")

def test_rename_category(setup_deja):
    ds = setup_deja
    ds.add("Games", ["Chess", "Poker"])
    ds.rename_category("Games", "Board Games")
    assert "Board Games" in ds.deja[0]

def test_rename_non_existent_category(setup_deja):
    ds = setup_deja
    ds.add("Dummy", ["Placeholder"])
    with pytest.raises(ValueError):
        ds.rename_category("Invalid", "NewCategory")

def test_invalid_add(setup_deja):
    ds = setup_deja
    with pytest.raises(TypeError):
        ds.add(123, ["Item"])
    with pytest.raises(TypeError):
        ds.add("Category", 123)

def test_find_in_empty_structure(setup_deja):
    ds = setup_deja
    with pytest.raises(RuntimeError):
        ds.find_category("AnyCategory")