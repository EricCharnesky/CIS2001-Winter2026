from polygon import Polygon

class Rectangle(Polygon):

    def __init__(self):
        super().__init__(4)

    def get_area(self):
        return self.get_side_length(0) * self.get_side_length(1)

    def set_side_length(self, side_index, length):
        self._is_valid_side_index(side_index)
        if side_index % 2: # is non 0
            super().set_side_length(1, length)
            super().set_side_length(3, length)
        else:
            super().set_side_length(0, length)
            super().set_side_length(2, length)

    def set_length(self, length):
        super().set_side_length(0, length)
        super().set_side_length(2, length)

    def set_width(self, width):
        super().set_side_length(1, width)
        super().set_side_length(3, width)

    def get_length(self):
        return self.get_side_length(0)

    def get_width(self):
        return self.get_side_length(1)
