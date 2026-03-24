from stackandqueue import Stack, Queue

class Dock:

    def __init__(self, number_of_items_per_train, number_of_items_per_plane, train_items, plane_items):
        self.trains = [TransportMethod(0, 0, 0)] # offset indexes to match numbers
        for number_of_items in number_of_items_per_train:
            self.trains.append(TransportMethod(number_of_items, len(self.trains), 1) )
        self.planes = [TransportMethod(0, 0, 0)] # offset indexes to match numbers
        for number_of_items in number_of_items_per_plane:
            self.planes.append(TransportMethod(number_of_items, len(self.planes), 5))
        self.train_items = Queue()

        stack_to_add = Stack()
        for train_item in train_items:
            if len(stack_to_add) == 5:
                self.train_items.enqueue(stack_to_add)
                stack_to_add = Stack()
            stack_to_add.push(train_item)

        if len(stack_to_add):
            self.train_items.enqueue(stack_to_add)

        self.plane_items = Queue()
        for plane_item in plane_items:
            self.plane_items.enqueue(plane_item)

    def load_trains(self):
        current_time = 0
        while not self.train_items.is_empty():
            current_stack = self.train_items.dequeue()
            while len(current_stack): # not empty - not 0
                train_number = current_stack.pop()
                current_time = self.trains[train_number].add_item(current_time)

    def load_planes(self):
        current_time = 0
        while not self.plane_items.is_empty():
            plane_number = self.plane_items.dequeue()
            current_time = self.planes[plane_number].add_item(current_time)

    def get_train_full_times(self):
        return " ".join(str(train.get_time_fully_loaded()) for train in self.trains[1:])

    def get_plane_full_times(self):
        return " ".join(str(plane.get_time_fully_loaded()) for plane in self.planes[1:])

class TransportMethod:

    def __init__(self, expected_number_of_items, number, time_to_transport_method):
        self._expected_number_of_items = expected_number_of_items
        self._current_number_of_items = 0
        self._time_fully_loaded = 0
        self._number = number
        self._time_to_transport_method = time_to_transport_method

    def add_item(self, time_started_to_load):
        self._current_number_of_items += 1
        if self._current_number_of_items == self._expected_number_of_items:
            self._time_fully_loaded = time_started_to_load + (self._time_to_transport_method * self._number)
        return time_started_to_load + 2 *  (self._time_to_transport_method * self._number)

    def get_time_fully_loaded(self):
        return self._time_fully_loaded