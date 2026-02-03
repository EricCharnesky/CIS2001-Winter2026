class FixedSizeArray:

    def __init__(self):
        self._data = [None] * 10
        self._max_size = 10
        self._number_of_items = 0

    # O(n)
    def _resize(self):
        self._max_size *= 2
        new_data = [None] * self._max_size
        for index in range(self._number_of_items):
            new_data[index] = self._data[index]
        self._data = new_data

    # on average O(1)
    def append(self, item):
        if self._max_size == self._number_of_items:
            self._resize()

        # self._number_of_items is the next available index
        self._data[self._number_of_items] = item
        self._number_of_items += 1

    # O(n)
    def remove(self, value):
        for index in range(self._number_of_items):
            if self._data[index] == value:
                for index_to_shift in range(index+1, self._number_of_items):
                    self._data[index_to_shift-1] = self._data[index_to_shift]
                self._number_of_items -= 1
                break
        else:
            raise ValueError("item not found")

    # O(1)
    def get(self, index):
        return self._data[index]

    # O(n)
    def find(self, value):
        for index in range(self._number_of_items):
            if self._data[index] == value:
                return index
        raise ValueError("not found")


    def __len__(self):
        return self._number_of_items
