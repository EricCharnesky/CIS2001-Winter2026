def count_down(number):
    print(number)
    if number > 0:
        count_down(number-1)

def bad_fib(nth):
    if nth <= 2:
        return 1
    return bad_fib(nth-1) + bad_fib(nth-2)

def better_recursive_fib(nth):
    if nth <= 1:
        return 1
    return _better_recursive_fib(nth, 1, 1, 1)

def _better_recursive_fib(nth, current_nth, previous, current):
    if current_nth == nth:
        return current
    return _better_recursive_fib(nth, current_nth+1, current, previous+current)

def iterative_fib(nth):
    current_nth = 0
    previous = 0
    current = 1

    while current_nth != nth:
        next = previous + current
        previous = current
        current = next
        current_nth += 1

    return current


#for nth in range(50):
#   print(f'{nth}: {better_recursive_fib(nth)}')


class MazeSolver:

    START = 'S'
    END = 'E'
    OPEN = ' '
    VISITED = '.'

    def __init__(self, maze):
        self.maze = maze
        self.solved = False

    def solve(self):
        start_row = 0
        start_column = 0

        for row_index in range(len(self.maze)):
            for column_index in range(len(self.maze[row_index])):
                if self.maze[row_index][column_index] == self.START:
                    start_row = row_index
                    start_column = column_index
        self._solve(start_row, start_column)

    def _solve(self, row_index, column_index):


        if self.maze[row_index][column_index] == self.END:
            #print(self)
            self.solved = True

        if self.maze[row_index][column_index] != self.START:
            self.maze[row_index][column_index] = self.VISITED
        # try up
        self._try_move_to(row_index-1, column_index)

        # try down
        self._try_move_to(row_index + 1, column_index)

        # try left
        self._try_move_to(row_index, column_index - 1)

        # try right
        self._try_move_to(row_index, column_index + 1)

    def _try_move_to(self, target_row_index, target_column_index):
        if 0 <= target_row_index < len(self.maze) and 0 <= target_column_index < len(self.maze[target_row_index]) and \
                ( self.maze[target_row_index][target_column_index] == self.OPEN or \
                    self.maze[target_row_index][target_column_index] == self.END ):

                self._solve(target_row_index, target_column_index)


    def __str__(self):
        return "\n".join(str(row) for row in self.maze)


maze = [
    ['S', 'X', 'X', 'X', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', 'X', 'X', 'X', 'X'],
    [' ', 'X', ' ', ' ', ' '],
    [' ', 'X', 'X', ' ', 'E'],
]

solver = MazeSolver(maze)

solver.solve()
if solver.solved:
    print(solver)
else:
    print("unsolvable")