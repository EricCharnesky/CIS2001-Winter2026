# First in First Out
class CircularQueue:

    def __init__(self):
        self._data = [None] * 10
        self._front_index = 0
        self._back_index = 0
        self._number_of_items = 0

    # O(1) - doesn't continuously take up memory
    def enqueue(self, item):
        self._data[self._back_index] = item
        self._back_index += 1
        # circles back to the front
        if self._back_index == len(self._data):
            self._back_index = 0
        self._number_of_items += 1
        self._ensure_space()

    def _ensure_space(self):
        if self._number_of_items == len(self._data):
            new_data = [None] * ( len(self._data) * 2 )
            new_index = 0
            for index in range(self._front_index, len(self._data)):
                new_data[new_index] = self._data[index]
                new_index += 1
            for index in range(self._back_index):
                new_data[new_index] = self._data[index]
                new_index += 1
            self._data = new_data
            self._front_index = 0
            self._back_index = new_index

    # O(1)
    def dequeue(self):
        # TODO - sanity check the front index
        # TODO - optimize space complexity by resizing smaller if needed
        item = self._data[self._front_index]
        self._data[self._front_index] = None
        self._front_index += 1
        if self._front_index == len(self._data):
            self._front_index = 0
        self._number_of_items -= 1
        return item

    # O(1)
    def first(self):
        # TODO - sanity check index
        return self._data[self._front_index]

    def __len__(self):
        return self._number_of_items

    def is_empty(self):
        return self._number_of_items == 0


class FastBadQueue:

    def __init__(self):
        self._data = []
        self._front_index = 0

    # O(1)
    def enqueue(self, item):
        self._data.append(item)

    # O(1)
    def dequeue(self):
        # TODO - sanity check the front index
        item = self._data[self._front_index]
        self._data[self._front_index] = None
        self._front_index += 1
        return item

    # O(1)
    def first(self):
        # TODO - sanity check index
        return self._data[self._front_index]

    def __len__(self):
        return len(self._data) - self._front_index

    def is_empty(self):
        return len(self._data) == self._front_index

class SlowQueue:

    def __init__(self):
        self._data = []

    # O(1)
    def enqueue(self, item):
        self._data.append(item)

    # O(n)
    def dequeue(self):
        return self._data.pop(0)

    # O(1)
    def first(self):
        return self._data[0]

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

# First In Last Out
class Stack:

    def __init__(self):
        self._data = []

    # adds to top of stack
    # O(1)
    def push(self, item):
        self._data.append(item)

    # return the item on top
    # O(1)
    def peek(self):
        return self._data[-1]

    # remove and return the item on top
    # O(1)
    def pop(self):
        return self._data.pop()

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0


queue = CircularQueue()

for number in range(7):
    queue.enqueue(number)

for number in range(3):
    print(queue.dequeue())

for number in range(7, 13):
    queue.enqueue(number)

while not queue.is_empty():
    print(queue.dequeue())