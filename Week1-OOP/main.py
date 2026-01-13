# from module_name import class_name
from polygon import Polygon
from triangle import Triangle
from rectangle import Rectangle
from square import Square
from cube import Cube


def print_polygon_details(polygon : Polygon):
    print(f'perimeter: {polygon.get_perimeter()}')
    print(f'area: {polygon.get_area()}')
    # can't use a triangle only function
    # polygon.get_base()

cube = Cube(5)
print(f'volume {cube.get_volume()}')
print(f'surface area {cube.get_surface_area()}')

small_triangle = Triangle()
small_triangle.set_side_length(0, 3)
small_triangle.set_side_length(1, 4)
small_triangle.set_side_length(2, 5)
print_polygon_details(small_triangle)

big_rectangle = Rectangle()
big_rectangle.set_side_length(0, 10)
big_rectangle.set_side_length(1, 5)
big_rectangle.set_side_length(2, 10)
big_rectangle.set_side_length(3, 20)
print_polygon_details(big_rectangle)
big_rectangle.set_length(10)
big_rectangle.set_width(5)
print_polygon_details(big_rectangle)


small_square = Square()
small_square.set_side_length(27, 10)
print_polygon_details(small_square)



four_sided_shape = Polygon(4)
#four_sided_shape.set_number_of_sides(4)
# bad form
# four_sided_shape._number_of_sides = 4
four_sided_shape.set_side_length(0, 5)
four_sided_shape.set_side_length(1, 7)
four_sided_shape.set_side_length(2, 3)
four_sided_shape.set_side_length(3, 5)
print_polygon_details(four_sided_shape)


# crashes because polygon doesn't know how to calculate area
print(four_sided_shape.get_number_of_sides())

# shouldn't access protected attributes directly
five_sided_shape = Polygon()
five_sided_shape._number_of_sides = -1
print(five_sided_shape._number_of_sides)

