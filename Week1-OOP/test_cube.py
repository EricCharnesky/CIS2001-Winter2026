from unittest import TestCase
from cube import Cube

class TestCube(TestCase):
    def test_get_volume(self):
        # AAA

        # Arrange - setup the code we need to test
        expected_volume = 125
        cube = Cube(5)

        # Act - call the code we're testing
        actual_volume = cube.get_volume()

        # Assert - did we get what we expected
        self.assertEqual(expected_volume, actual_volume)

    def test_get_surface_area(self):
        # Arrange - setup the code we need to test
        expected_surface_area = 150
        cube = Cube(5)

        # Act - call the code we're testing
        actual_surface_area = cube.get_surface_area()

        # Assert - did we get what we expected
        self.assertEqual(expected_surface_area, actual_surface_area)
