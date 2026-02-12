class CheckersSolver:

    WHITE = 'W'
    BLACK = 'B'
    EMPTY = ' '

    def __init__(self, board):
        if len(board) != 8:
            raise ValueError("not 8x8")
        for row in board:
            if len(row) != 8:
                raise ValueError("not 8x8")

        found_on_even = False
        found_on_odd = False
        for row_index in range(len(board)):
            for column_index in range(len(board[row_index])):
                if board[row_index][column_index] != self.EMPTY:
                    if board[row_index][column_index] not in ( self.WHITE, self.BLACK):
                        raise ValueError("invalid piece found, white and black checkers only")

                    if (row_index + column_index) % 2:
                        found_on_odd = True
                    else:
                        found_on_even = True

        if found_on_odd == found_on_even:
            raise ValueError("invalid piece setup")

        self._board = board
        self._max_jumps = 0

    def get_max_jumps(self):
        for row_index in range(len(self._board)):
            for column_index in range(len(self._board[row_index])):
                if self._board[row_index][column_index] == self.WHITE:
                    self._get_max_jumps(row_index, column_index, 0)


        return self._max_jumps

    def _try_move_to(self, current_row_index, current_column_index, target_row_index, target_column_index, current_jumps):
        row_of_jumped_piece = current_row_index + (target_row_index - current_row_index) // 2
        column_of_jumped_piece = current_column_index + (target_column_index - current_column_index) // 2
        if 0 <= target_row_index < 8 and 0 <= target_column_index < 8 and \
            self._board[target_row_index][target_column_index] == self.EMPTY and \
            self._board[row_of_jumped_piece][column_of_jumped_piece] == self.BLACK:
                self._board[current_row_index][current_column_index] = self.EMPTY
                self._board[row_of_jumped_piece][column_of_jumped_piece] = self.EMPTY
                self._board[target_row_index][target_column_index] = self.WHITE

                self._get_max_jumps(target_row_index, target_column_index, current_jumps+1)

                self._board[target_row_index][target_column_index] = self.EMPTY
                self._board[row_of_jumped_piece][column_of_jumped_piece] = self.BLACK
                self._board[current_row_index][current_column_index] = self.WHITE



    def _get_max_jumps(self, row_index, column_index, current_jumps):
        if current_jumps > self._max_jumps:
            self._max_jumps = current_jumps

        moves = [(row_index-2, column_index-2), (row_index-2, column_index+2),
            (row_index+2, column_index+2), (row_index+2, column_index-2)]

        for move in moves:
            self._try_move_to(row_index, column_index, move[0], move[1], current_jumps)


board = [
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', 'B', ' ', 'B', ' ', 'B', ' ', ' '],
    [' ', ' ', 'W', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', 'B', ' ', 'B', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', 'B', ' ', 'B', ' ', ' '],
    [' ', ' ', 'W', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', 'B']
]

solver = CheckersSolver(board)
print(solver.get_max_jumps())