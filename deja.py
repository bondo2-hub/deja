from messages import MESSAGES

class Deja:
    def __init__(self):
        self.CLASS_NAME = 'DEJA'
        self.deja = {}

    def add(self, category, items):
        """Adds a new category with validation."""
        if not isinstance(category, str):
            raise TypeError(MESSAGES["invalid_category_type"])

        if not isinstance(items, (list, str)):
            raise TypeError(MESSAGES["invalid_items_type"])

        for data in self.deja.values():
            if category.lower() in (name.lower() for name in data.keys()):
                raise ValueError(MESSAGES["category_exists"])

        next_index = len(self.deja)
        self.deja[next_index] = {category: items if isinstance(items, list) else [
            items]}

    def display(self):
        """Visual representation of stored data."""
        if not self.deja:
            print(MESSAGES["no_categories_exist"])
        else:
            width = max(len(msg) for msg in MESSAGES.values()) + 10
            print("\n" + "=" * width)
            print(MESSAGES["data_header"].format(class_name=self.CLASS_NAME))
            print("=" * width)
            for idx, data in self.deja.items():
                for category, items in data.items():
                    print(MESSAGES["index_display"].format(
                        idx=idx, category=category, items=items))
            print("=" * width + "\n")

    def removeby_cat(self, category_name):
        """Removes a category by name with validation."""
        if not isinstance(category_name, str):
            raise TypeError(MESSAGES["invalid_category_type"])

        cats_to_remove = [idx for idx,
                          data in self.deja.items() if category_name in data]

        if not cats_to_remove:
            raise ValueError(MESSAGES["category_not_found"].format(
                category=category_name))

        for idx in cats_to_remove:
            try:
                del self.deja[idx]
            except KeyError:
                raise KeyError(MESSAGES["index_not_found"].format(index=idx))
            except Exception as e:
                raise RuntimeError(
                    MESSAGES["unexpected_error"].format(error=e))

    def removeby_idx(self, index):
        """Removes an entry by index with proper validation."""
        if not isinstance(index, int):
            raise TypeError("Index must be an integer.")

        if index not in self.deja:
            raise KeyError(MESSAGES["index_not_found"].format(index=index))

        try:
            del self.deja[index]
        except KeyError:
            raise KeyError(MESSAGES["index_not_found"].format(index=index))
        except Exception as e:
            raise RuntimeError(MESSAGES["unexpected_error"].format(error=e))

    def __repr__(self) -> str:
        return str(self.deja)

    def find_category(self, category_name):
        """Finds a category with validation."""
        if not isinstance(category_name, str):
            raise TypeError(MESSAGES["invalid_category_type"])

        if not self.deja:
            raise RuntimeError(MESSAGES["no_categories_exist"])

        for idx, data in self.deja.items():
            if category_name in data:
                result = MESSAGES["category_found"].format(index=idx)
                print(result)
                return result

        print(MESSAGES["category_not_found"].format(category=category_name))
        raise ValueError(MESSAGES["category_not_found"].format(
            category=category_name))

    def rename_category(self, target_category, new_category_name):
        """Renames a current category with proper validation."""
        if not isinstance(new_category_name, str):
            raise TypeError(MESSAGES["invalid_category_type"])

        if not self.deja:
            raise RuntimeError(MESSAGES["no_categories_exist"])

        if any(new_category_name in data for data in self.deja.values()):
            raise ValueError(MESSAGES["category_exists"])

        for idx, data in self.deja.items():
            if target_category in data:
                data[new_category_name] = data.pop(target_category)
                return MESSAGES["category_renamed"].format(old=target_category, new=new_category_name)

        raise ValueError(MESSAGES["category_not_found"].format(
            category=target_category))
    