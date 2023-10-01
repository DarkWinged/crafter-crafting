import copy

class PList:
    def __init__(self, initial_list: list=None):
        if initial_list is None:
            initial_list: list = []
        self._original: list = initial_list
        self._changed: list = copy.deepcopy(self._original)

    def __getitem__(self, index):
        return self._changed[index]

    def __setitem__(self, index, value):
        self._changed[index] = value

    def __len__(self):
        return len(self._changed)

    def __iter__(self):
        return iter(self._changed)

    def __contains__(self, item):
        return item in self._changed
    
    def __str__(self):
        return str(self._changed)
    
    def __repr__(self):
        return repr(self._changed)
    
    def __add__(self, other):
        return self._changed + other
    
    def __radd__(self, other):
        return other + self._changed
    
    def __iadd__(self, other):
        self._changed += other
        return self._changed
    
    def __mul__(self, other):
        return self._changed * other
    
    def __rmul__(self, other):
        return other * self._changed
    
    def __imul__(self, other):
        self._changed *= other
        return self._changed
    
    def __delitem__(self, index):
        self._changed.__delitem__(index)

    def __reversed__(self):
        return reversed(self._changed)
    
    def __eq__(self, other):
        return self._changed == other
    
    def __ne__(self, other):
        return self._changed != other
    
    def __lt__(self, other):
        return self._changed < other
    
    def __le__(self, other):
        return self._changed <= other
    
    def __gt__(self, other):
        return self._changed > other
    
    def __ge__(self, other):
        return self._changed >= other
    
    def append(self, value):
        self._changed.append(value)

    def extend(self, iterable):
        self._changed.extend(iterable)

    def pop(self, index=-1):
        self._changed.pop(index)

    def remove(self, value):
        self._changed.remove(value)

    def insert(self, index, value):
        self._changed.insert(index, value)

    def clear(self):
        self._changed.clear()

    def copy(self):
        return self._changed.copy()
    
    def count(self, value):
        return self._changed.count(value)
    
    def index(self, value, start=0, stop=None):
        return self._changed.index(value, start, stop)
    
    def reverse(self):
        self._changed.reverse()

    def sort(self, key=None, reverse=False):
        self._changed.sort(key, reverse)

    def reset(self):
        self._changed = copy.deepcopy(self._original)

    def update(self):
        if len(self._changed) < len(self._original):
            for index, _ in enumerate(self._original):
                if index >= len(self._changed):
                    while len(self._changed) > len(self._original):
                        self._changed.pop()
                else:
                    self._original[index] = self._changed[index]
        elif len(self._changed) > len(self._original):
            for index, item in enumerate(self._changed):
                if index >= len(self._original):
                    self._original.append(item)
                else:
                    self._original[index] = item
        else:
            for index, item in enumerate(self._changed):
                self._original[index] = item

    @property
    def original(self):
        return copy.deepcopy(self._original)