import copy
from typing import Generic, TypeVar

class PList(Generic[TypeVar('T')]):
    """A protected list class that allows for the original list to be updated to match the current list.

    Args:
        Generic (TypeVar('T')): See https://docs.python.org/3/library/typing.html#typing.Generic
    """
    def __init__(self, initial_list: list=None):
        """A protected list class that allows for the original list to be updated to match the current list.

        Args:
            initial_list (list, optional): The initial list to set the original and current attributes to. Defaults to None.
        """
        if initial_list is None:
            initial_list: list = []
        self._original: list = initial_list
        self._current: list = copy.deepcopy(self._original)

    def __getitem__(self, index: int) -> any:
        """Returns the item at the given index in the current attribute.

        Args:
            index (int): The index to get the item at.

        Returns:
            any: The item at the given index in the current attribute.
        """
        return self._current[index]

    def __setitem__(self, index: int, value: any):
        """Sets the item at the given index in the current attribute to the given value.

        Args:
            index (int): The index to set the item at.
            value (any): The value to set the item to.
        """
        self._current[index] = value

    def __len__(self) -> int:
        """Returns the length of the current attribute.

        Returns:
            int: Length of the current attribute.
        """
        return len(self._current)

    def __iter__(self) -> iter:
        """Returns an iterator of the current attribute.

        Returns:
            iter: Iterator of the current attribute.
        """
        return iter(self._current)

    def __contains__(self, item: any) -> bool:
        """Returns True if the current attribute contains the given item.

        Args:
            item (any): The item to search for.

        Returns:
            bool: True if the current attribute contains the given item.
        """
        return item in self._current
    
    def __str__(self) -> str:
        """Returns a string representation of the current attribute.

        Returns:
            str: String representation of the current attribute.
        """
        return str(self._current)
    
    def __repr__(self) -> str:
        """Returns a string representation of the current attribute.

        Returns:
            str: String representation of the current attribute.
        """
        return repr(self._current)
    
    def __add__(self, other: iter) -> list:
        """Adds the current attribute to the given iterable.

        Args:
            other (iter): The iterable to add the current attribute to.

        Returns:
            list: The current attribute plus the given iterable.
        """
        return self._current + other
    
    def __radd__(self, other: iter) -> list:
        """Adds the current attribute to the given iterable.

        Args:
            other (iter): The iterable to add the current attribute to.

        Returns:
            list: The current attribute plus the given iterable.
        """
        return other + self._current
    
    def __iadd__(self, other: iter) -> list:
        """Adds the given iterable to the current attribute.

        Args:
            other (iter): The iterable to add to the current attribute.

        Returns:
            list: The current attribute plus the given iterable.
        """
        self._current += other
        return self._current
    
    def __mul__(self, other: iter) -> list:
        """Multiplies the current attribute by the given iterable.

        Args:
            other (iter): The iterable to multiply the current attribute by.

        Returns:
            list: The current attribute multiplied by the given iterable.
        """
        return self._current * other
    
    def __rmul__(self, other: iter) -> list:
        """Multiplies the given iterable by the current attribute.

        Args:
            other (iter): The iterable to multiply the current attribute by.

        Returns:
            list: The current attribute multiplied by the given iterable.
        """
        return other * self._current
    
    def __imul__(self, other: iter) -> list:
        """Multiplies the current attribute by the given iterable.

        Args:
            other (iter): The iterable to multiply the current attribute by.

        Returns:
            list: The current attribute multiplied by the given iterable.
        """
        self._current *= other
        return self._current
    
    def __delitem__(self, index: int):
        """Deletes the item at the given index from the current attribute.

        Args:
            index (int): The index to delete the item from.
        """
        self._current.__delitem__(index)

    def __reversed__(self) -> iter:
        """Returns a reversed iterator of the current attribute.

        Returns:
            iter: Reversed iterator of the current attribute.
        """
        return reversed(self._current)
    
    def __eq__(self, other) -> bool:
        """Returns True if the current attribute is equal to the given attribute.

        Args:
            other (_type_): The attribute to compare to.

        Returns:
            bool: True if the current attribute is equal to the given attribute.
        """
        return self._current == other
    
    def __ne__(self, other) -> bool:
        """Returns True if the current attribute is not equal to the given attribute.

        Args:
            other (_type_): The attribute to compare to.

        Returns:
            bool: True if the current attribute is not equal to the given attribute.
        """
        return self._current != other
    
    def __lt__(self, other) -> bool:
        """Returns True if the current attribute is less than the given attribute.

        Args:
            other (_type_): The attribute to compare to.

        Returns:
            bool: True if the current attribute is less than the given attribute.
        """
        return self._current < other
    
    def __le__(self, other) -> bool:
        """Returns True if the current attribute is less than or equal to the given attribute.

        Returns:
            bool: True if the current attribute is less than or equal to the given attribute.
        """
        return self._current <= other
    
    def __gt__(self, other) -> bool:
        """Returns True if the current attribute is greater than the given attribute.

        Args:
            other (_type_): The attribute to compare to.

        Returns:
            bool: True if the current attribute is greater than the given attribute.
        """
        return self._current > other
    
    def __ge__(self, other) -> bool:
        """Returns True if the current attribute is greater than or equal to the given attribute.

        Args:
            other (_type_): The attribute to compare to.

        Returns:
            bool: True if the current attribute is greater than or equal to the given attribute.
        """
        return self._current >= other
    
    def append(self, value):
        """Appends the given value to the current attribute.

        Args:
            value (_type_): The value to append.
        """
        self._current.append(value)

    def extend(self, iterable: iter):
        """Extends the current attribute with the given iterable.

        Args:
            iterable (iter): The iterable to extend the current attribute with.
        """
        self._current.extend(iterable)

    def pop(self, index=-1):
        """Removes and returns the item at the given index from the current attribute.

        Args:
            index (int, optional): The index to remove the item from. Defaults to -1.
        """
        self._current.pop(index)

    def remove(self, value):
        """Removes the first occurrence of the given value from the current attribute.

        Args:
            value (_type_): The value to remove.
        """
        self._current.remove(value)

    def insert(self, index: int, value):
        """Inserts the given value at the given index in the current attribute.

        Args:
            index (int): The index to insert the value at.
            value (_type_): The value to insert.
        """
        self._current.insert(index, value)

    def clear(self):
        """Clears the current attribute.
        """
        self._current.clear()

    def copy(self) -> list:
        """Returns a shallow copy of the current attribute.

        Returns:
            list: Shallow copy of the current attribute.
        """
        return self._current.copy()
    
    def count(self, value) -> int:
        """Returns the number of occurrences of the given value in the current attribute.

        Args:
            value (_type_): The value to search for.

        Returns:
            int: The number of occurrences of the given value in the current attribute.
        """
        return self._current.count(value)
    
    def index(self, value, start=0, stop=None):
        """Returns the index of the first occurrence of the given value in the current attribute.

        Args:
            value (_type_): The value to search for.
            start (int, optional): If specified, the search starts at the given index. Defaults to 0.
            stop (_type_, optional): If specified, the search stops at the given index. Defaults to None.

        Returns:
            _type_: _description_
        """
        return self._current.index(value, start, stop)
    
    def reverse(self):
        """Reverses the current attribute in place.
        """
        self._current.reverse()

    def sort(self, key=None, reverse=False):
        """Sorts the current attribute in place.

        Args:
            key (_type_, optional): If specified, the key function is called on each list item before comparison. Defaults to None.
            reverse (bool, optional): If True, the list is sorted in reverse order. Defaults to False.
        """
        self._current.sort(key, reverse)

    def reset(self):
        """Resets the current attribute to match the original attribute.
        """
        self._current = copy.deepcopy(self._original)

    def update(self):
        """Updates the original attribute to match the current attribute.
        If the current attribute is longer than the original attribute, the original attribute is extended with the extra items.
        If the current attribute is shorter than the original attribute, the original attribute is truncated to the length of the current attribute.
        """
        if len(self._current) < len(self._original):
            for index, _ in enumerate(self._original):
                if index >= len(self._current):
                    for index in reversed(range(len(self._current), len(self._original))):
                        del self._original[index]
                else:
                    self._original[index] = self._current[index]
        elif len(self._current) > len(self._original):
            for index, item in enumerate(self._current):
                if index >= len(self._original):
                    self._original.append(item)
                else:
                    self._original[index] = item
        else:
            for index, item in enumerate(self._current):
                self._original[index] = item

    @property
    def original(self) -> list:
        """Returns a deep copy of the original attribute.

        Returns:
            list: Deep copy of the original attribute.
        """
        return copy.deepcopy(self._original)
    
    @property
    def current(self) -> list:
        """Returns a copy of the current attribute.

        Returns:
            list: Deep copy of the current attribute.
        """
        return copy.deepcopy(self._current)
    
    @current.setter
    def current(self, other: list):
        """Sets the current attribute to the given list.
        If the given list is longer than the current attribute, the current attribute is extended with the extra items.
        If the given list is shorter than the current attribute, the current attribute is truncated to the length of the given list.

        Args:
            other (list): A list to set the current attribute to.
        """
        if len(other) > len(self._current):
            for index, item in enumerate(other):
                if index >= len(self._current):
                    self._current.append(item)
                else:
                    self._current[index] = item
        elif len(other) < len(self._current):
            for index, _ in enumerate(self._current):
                if index >= len(other):
                    for index in reversed(range(len(other), len(self._current))):
                        del self._current[index]
                else:
                    self._current[index] = other[index]
        else:
            for index, item in enumerate(other):
                self._current[index] = item