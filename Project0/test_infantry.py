from unittest import TestCase
from infantry import Infantry

class TestInfantry(TestCase):
    def test_move_fails_both_x_and_y(self):
        # arrange
        infantry = Infantry(0, 0, "")

        # act

        # assert
        with self.assertRaises(ValueError):
            infantry.move(1, 1)

    def test_move_fails_too_far(self):
        # arrange
        infantry = Infantry(0, 0, "")

        # act

        # assert
        with self.assertRaises(ValueError):
            infantry.move(10, 0)

    def test_move(self):
        # arrange
        infantry = Infantry(0, 0, "")
        expected_x = 5

        # act
        infantry.move(5, 0)
        actual_x = infantry.get_x_position()

        # assert
        self.assertEqual(expected_x, actual_x)
