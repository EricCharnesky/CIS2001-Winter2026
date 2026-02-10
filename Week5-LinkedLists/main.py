class LinkedListStack:

    def __init__(self):
        self._front = None
        self._number_of_items = 0

    # O(1) always
    def add_to_front(self, item):
        self._front = self.Node(item, self._front)
        self._number_of_items += 1

    # O(1) always
    def remove_front(self):
        if self.is_empty():
            raise ValueError("Empty")
        item = self._front.item
        self._front = self._front.next
        self._number_of_items -= 1
        return item

    # O(1)
    def front(self):
        if self.is_empty():
            raise ValueError("Empty")
        return self._front.item

    def is_empty(self):
        return self._front is None

    def __len__(self):
        return self._number_of_items

    class Node:

        def __init__(self, item, next = None):
            self.item = item
            self.next = next


class LinkedListDeque:

    def __init__(self):
        self._front = None
        self._back = None
        self._number_of_items = 0

    # O(1) always
    def add_to_front(self, item):
        new_front = self.Node(item, self._front)
        if self._front is not None:
            self._front.previous = new_front
        self._front = new_front
        # same as below but easier on the eyes
        # self._front = self.Node(item, self._front)
        # self._front.next.previous = self._front
        if self._back is None:
            self._back = self._front
        self._number_of_items += 1

    # O(1)
    def add_to_back(self, item):
        if self.is_empty():
            self.add_to_front(item)
        else:
            self._back.next = self.Node(item, next=None, previous=self._back)
            self._back = self._back.next

        self._number_of_items += 1

    # O(1) always
    def remove_front(self):
        self._check_empty()
        item = self._front.item
        self._front = self._front.next

        if self._front is None:
            self._back = None
        else:
            self._front.previous = None
        self._number_of_items -= 1
        return item

    def _check_empty(self):
        if self.is_empty():
            raise ValueError("Empty")

    # O(1)
    def remove_back(self):
        self._check_empty()
        item = self._back.item
        self._back = self._back.previous

        if self._back is None:
            self._front = None
        else:
            self._back.next = None
        self._number_of_items -= 1
        return item

    # O(1)
    def front(self):
        self._check_empty()
        return self._front.item

    def back(self):
        self._check_empty()
        return self._back.item

    def is_empty(self):
        return self._front is None

    def __len__(self):
        return self._number_of_items

    class Node:

        def __init__(self, item, next = None, previous = None):
            self.item = item
            self.next = next
            self.previous = previous


class CircularDoublyLinkedList:

    def __init__(self):
        self._dummy_node = self.Node(None)
        self._dummy_node.next = self._dummy_node
        self._dummy_node.previous = self._dummy_node
        self._number_of_items = 0

    # O(1) always
    def add_to_front(self, item):
        self._add_between(item, next=self._dummy_node.next, previous=self._dummy_node)

    # O(1)
    def add_to_back(self, item):
        self._add_between(item, next=self._dummy_node, previous=self._dummy_node.previous)

    # O(1) always
    def remove_front(self):
        return self._remove_node(self._dummy_node.next)

    def _remove_node(self, node):
        self._check_empty()
        item = node.item
        node.next.previous = node.previous
        node.previous.next = node.next
        self._number_of_items -= 1
        return item

    def _check_empty(self):
        if self.is_empty():
            raise ValueError("Empty")

    # O(1)
    def remove_back(self):
        return self._remove_node(self._dummy_node.previous)

    # O(1)
    def front(self):
        self._check_empty()
        return self._dummy_node.next.item

    def back(self):
        self._check_empty()
        return self._dummy_node.previous.item

    def is_empty(self):
        return self._number_of_items == 0

    def __len__(self):
        return self._number_of_items

    def _validate_index(self, index):
        if self.is_empty():
            raise ValueError("empty")
        if index >= self._number_of_items:
            raise IndexError()
        current_node = self._dummy_node.next

        for node in range(index):
            current_node = current_node.next

        return current_node

    # O(n)
    def get_from_index(self, index):
        current_node = self._validate_index(index)

        return current_node.item

    # O(n) slow to find the node to remove by index
    def pop(self, index = None):
        if index is None:
            return self.remove_back()

        current_node = self._validate_index(index)

        return self._remove_node(current_node)

    def _add_between(self, item, next, previous):
        new_node = self.Node(item, next=next, previous=previous)
        new_node.next.previous = new_node
        new_node.previous.next = new_node
        self._number_of_items += 1

    # O(n)
    def insert(self, index, item):
        current_node = self._validate_index(index)
        self._add_between(item, current_node, current_node.previous)


    class Node:

        def __init__(self, item, next = None, previous = None):
            self.item = item
            self.next = next
            self.previous = previous


# stack = LinkedListStack()
#
# for number in range(10):
#     stack.add_to_front(number)
#
# while not stack.is_empty():
#     print(stack.remove_front())

deque = LinkedListDeque()

for number in range(5):
    deque.add_to_back(number)

for number in range(5, 10):
    deque.add_to_front(number)

print(deque.remove_front())
print(deque.remove_back())

while not deque.is_empty():
    print(deque.remove_back())