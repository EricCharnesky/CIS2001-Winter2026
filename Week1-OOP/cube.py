from square import Square

class Cube:

    def __init__(self, size):
        self._face = Square()
        self._face.set_length(size)

    def get_volume(self):
        return self._face.get_width() ** 3

    def get_surface_area(self):
        return self._face.get_area() * 6