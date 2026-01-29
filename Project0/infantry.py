
from unit import Unit

class Infantry(Unit):

    def __init__(self, x, y, team):
        super().__init__(5, 5, x, y, team)

    def move(self, x, y):
        if x and y:
            raise ValueError("can't move both x and y")
        if abs(x) > 5 or abs(y) > 5:
            raise ValueError("Can't move more than 5 units")
        self._x_position += x
        self._y_position += y