class SudokuSolver:

    BLANK = " "

    def __init__(self, grid):
        self.grid = grid
        self.not_solved = True

    # TODO - Optimize later
    def solve(self):
        row_index, column_index = self._find_first_open_space()
        if row_index == -1 and column_index == -1:
            print(self)
            print()
            self.not_solved = False
            return
        for number in range(1, 10):
            number = str(number)
            # stop more recursion from happening once it is solved
            if self.not_solved and self._can_place_number(number, row_index, column_index):
                self.grid[row_index][column_index] = number
                self.solve()
                if self.not_solved:
                    self.grid[row_index][column_index] = self.BLANK


    def __str__(self):
        return "\n".join(str(row) for row in self.grid)

    def _find_first_open_space(self):
        for row_index in range(len(self.grid)):
            for column_index in range(len(self.grid[row_index])):
                if self.grid[row_index][column_index] == self.BLANK:
                    return row_index, column_index
        return -1, -1

    def _can_place_number(self, number, row_index, column_index):
        return self._can_place_number_in_row(number, row_index) \
            and self._can_place_number_in_column(number, column_index) \
            and self._can_place_number_in_grid(number, row_index, column_index )

    def _can_place_number_in_row(self, number, row_index):
        return number not in self.grid[row_index]

    def _can_place_number_in_column(self, number, column_index):
        for row_index in range(len(self.grid)):
            if number == self.grid[row_index][column_index]:
                return False
        return True

    def _can_place_number_in_grid(self, number, row_index, column_index):
        start_row_index = row_index // 3 * 3
        start_column_index = column_index // 3 * 3

        for row_index in range(start_row_index, start_row_index+3):
            for column_index in range(start_column_index, start_column_index+3):
                if self.grid[row_index][column_index] == number:
                    return False
        return True

grid = [
    ['3', '2', '7', '5', '1', '6', '4', '9', '8'],
    ['4', ' ', ' ', '2', '8', '7', ' ', ' ', '5'],
    [' ', ' ', ' ', ' ', '4', ' ', ' ', ' ', ' '],
    [' ', ' ', '6', ' ', ' ', ' ', '5', ' ', ' '],
    [' ', ' ', ' ', ' ', '5', ' ', ' ', ' ', ' '],
    ['7', ' ', ' ', ' ', '3', ' ', ' ', ' ', '1'],
    ['8', ' ', '2', ' ', ' ', ' ', '9', ' ', '3'],
    [' ', '1', '3', ' ', ' ', ' ', '8', '4', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
]

solver = SudokuSolver(grid)
solver.solve()