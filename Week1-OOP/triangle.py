import math
from polygon import Polygon

class Triangle(Polygon):

    def __init__(self):
        super().__init__(3)

    def get_area(self):
        semi_perimeter = self.get_perimeter() / 2
        return math.sqrt(semi_perimeter
                         * ( semi_perimeter-self.get_side_length(0))
                         * ( semi_perimeter-self.get_side_length(1) )
                         * ( semi_perimeter-self.get_side_length(2)) )

    # this is a silly example of a unique to triangle function, you can't use it on polygons
    def get_base(self):
        return 10
