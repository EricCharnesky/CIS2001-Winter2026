from rectangle import Rectangle

class Square(Rectangle):

    def set_length(self, length):
        super().set_length(length)
        super().set_width(length)

    def set_width(self, width):
        super().set_length(width)
        super().set_width(width)

    def set_side_length(self, side_index, length):
        # don't have to validate the index
        self.set_length(length)