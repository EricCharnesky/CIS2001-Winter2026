from platform import android_ver


class NQueens:

    QUEEN = 'Q'
    OPEN = ' '

    def __init__(self, n = 8):
        self.board = []
        for row in range(n):
            self.board.append([' '] * n)
        self.number_of_queens = 0

    def solve(self):
        if self.number_of_queens == len(self.board):
            print(self)
            print()
        for column_index in range(len(self.board)):
            if self._can_place_queen(self.number_of_queens, column_index):
                self.board[self.number_of_queens][column_index] = self.QUEEN
                self.number_of_queens += 1
                self.solve()
                # undo
                self.number_of_queens -= 1
                self.board[self.number_of_queens][column_index] = self.OPEN

    def __str__(self):
        return "\n".join(str(row) for row in self.board)

    def _can_place_queen(self, number_of_queens, column_index):
        return self._column_open(column_index) and \
            self._diagonal_backwards_open(number_of_queens, column_index) and \
            self._diagonal_forwards_open(number_of_queens, column_index)

    def _column_open(self, column_index):
        for row_index in range(self.number_of_queens):
            if self.board[row_index][column_index] == self.QUEEN:
                return False
        return True

    def _diagonal_backwards_open(self, number_of_queens, column_index):
        row_index_to_check = number_of_queens - 1
        column_index_to_check = column_index - 1

        while row_index_to_check >= 0 and column_index_to_check >= 0:
            if self.board[row_index_to_check][column_index_to_check] == self.QUEEN:
                return False
            row_index_to_check -= 1
            column_index_to_check -= 1
        return True

    def _diagonal_forwards_open(self, number_of_queens, column_index):
        row_index_to_check = number_of_queens - 1
        column_index_to_check = column_index + 1

        while row_index_to_check >= 0 and column_index_to_check < len(self.board):
            if self.board[row_index_to_check][column_index_to_check] == self.QUEEN:
                return False
            row_index_to_check -= 1
            column_index_to_check += 1
        return True


nqueens = NQueens()

nqueens.solve()