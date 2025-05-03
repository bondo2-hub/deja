class Deja:
    def __init__(self):
        self.CLASS_NAME = 'DEJA'
        self.deja = {}

    def add(self, category, items):
        """Adds a new category with validation."""

        for data in self.deja.values():
            if category.lower() in (name.lower() for name in data.keys()):
                raise ValueError(
                    "You can't have items with the same category name")

        if not isinstance(category, str):
            raise TypeError("Category name must be a string.")

        if not isinstance(items, (list, str)):
            raise TypeError("Items must be either a list or a string.")

        next_index = len(self.deja)
        self.deja[next_index] = {category: items if isinstance(items, list) else [
            items]}

    def display(self):
        """Visual representation of stored data."""

        if not self.deja:
            print(self.deja)
        else:
            print("\n" + "="*150)
            print(f"📋  {self.CLASS_NAME} DATA STRUCTURE")
            print("="*150)
            for idx, data in self.deja.items():
                for category, items in data.items():
                    print(
                        f"🔢 Index: {idx} | 📂 Category: {category} → 📦 Items: {items}")
            print("="*150 + "\n")

    def removeby_cat(self, category_name):
        """Removes a category by name with validation."""
        if not isinstance(category_name, str):
            raise TypeError("Category name must be a string.")

        cats_to_remove = []

        for idx, data in self.deja.items():
            if category_name in data:
                cats_to_remove.append(idx)

        if not cats_to_remove:
            raise ValueError(f"Category '{category_name}' not found.")

        for idx in cats_to_remove:
            try:
                del self.deja[idx]
            except KeyError:
                raise KeyError(f"Index {idx} does not exist.")
            except Exception as e:
                raise RuntimeError(f"Unexpected Error: {e}")

    def removeby_idx(self, index):
        """Removes an entry by index with proper validation."""
        if not isinstance(index, int):
            raise TypeError("Index must be an integer.")

        if index not in self.deja:
            raise KeyError(f"Index '{index}' not found.")

        try:
            del self.deja[index]
        except KeyError:
            raise KeyError(f"Index {index} does not exist.")
        except Exception as e:
            raise RuntimeError(f"Unexpected Error: {e}")