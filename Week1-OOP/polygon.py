class Polygon:

    def __init__(self, number_of_sides):
        if number_of_sides < 1:
            # bad form
            # print("error")
            raise ValueError("Invalid number of sides")
        self._number_of_sides = number_of_sides
        self._side_lengths = [0] * number_of_sides

    # if the attribute should not change, don't write a set function
    # def set_number_of_sides(self, number_of_sides):
    #     if number_of_sides < 1:
    #         # bad form
    #         # print("error")
    #         raise ValueError("Invalid number of sides")
    #         # won't run after a raise exception
    #         # self._number_of_sides = 0
    #         # return
    #     self._number_of_sides = number_of_sides
    #     self._side_lengths = [0] * number_of_sides

    def get_number_of_sides(self):
        return self._number_of_sides

    def set_side_length(self, side_index, length):
        self._is_valid_side_index(side_index)
        if length <= 0:
            raise ValueError("Invalid length")
        self._side_lengths[side_index] = length

    def get_side_length(self, side_index):
        self._is_valid_side_index(side_index)
        return self._side_lengths[side_index]

    def get_perimeter(self):
        return sum(self._side_lengths)

    def get_area(self):
        raise NotImplementedError()

    def _is_valid_side_index(self, side_index):
        if side_index >= self._number_of_sides or side_index < 0:
            raise ValueError("Invalid side index")
