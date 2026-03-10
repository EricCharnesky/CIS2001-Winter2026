import random


class MinPriorityQueue:

    def __init__(self):
        self._data = []

    def is_empty(self):
        return len(self._data) == 0

    def __len__(self):
        return len(self._data)

    def _parent_index(self, index):
        return (index - 1)//2

    def _left_index(self, index):
        return index*2 + 1

    def _right_index(self, index):
        return index*2 + 2

    def _upheap(self, index):
        if index != 0:
            parent_index = self._parent_index(index)
            if self._data[index] < self._data[parent_index]:
                self._data[index], self._data[parent_index] = self._data[parent_index], self._data[index]
                self._upheap(parent_index)

    def _downheap(self, index):
        left_child_index = self._left_index(index)
        right_child_index = self._right_index(index)

        smallest_child_index = None
        if left_child_index < len(self._data):
            smallest_child_index = left_child_index
        if right_child_index < len(self._data):
            if self._data[right_child_index] < self._data[left_child_index]:
                smallest_child_index = right_child_index

        if smallest_child_index and self._data[smallest_child_index] < self._data[index]:
            self._data[smallest_child_index], self._data[index] = self._data[index], self._data[smallest_child_index]
            self._downheap(smallest_child_index)

    def get_min(self):
        value = self._data[0]
        if len(self._data) == 1:
            return self._data.pop()
        else:
            self._data[0] = self._data.pop()
            self._downheap(0)
        return value

    def append(self, data):
        index = len(self._data)
        self._data.append(data)
        self._upheap(index)



priority_queue = MinPriorityQueue()

for number in range(50):
    priority_queue.append(random.randint(1, 1000))

while not priority_queue.is_empty():
    print(priority_queue.get_min())
