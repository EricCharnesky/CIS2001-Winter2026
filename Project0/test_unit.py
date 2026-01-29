from unittest import TestCase
from unit import Unit

class TestUnit(TestCase):
    def test_init(self):
        # arrange
        expected_attack_power = 5
        expected_max_hit_points = 5
        expected_hit_points = 5
        expected_range = 5
        expected_x_position = 5
        expected_y_position = 5
        expected_team = "team"

        # act
        unit = Unit(expected_attack_power, expected_max_hit_points, expected_x_position, expected_y_position, expected_team, expected_range)
        actual_attack_power = unit.get_attack_power()
        actual_max_hit_points = unit.get_max_hit_points()
        actual_hit_points = unit.get_hit_points()
        actual_range = unit.get_range()
        actual_x_position = unit.get_x_position()
        actual_y_position = unit.get_y_position()
        actual_team = unit.get_team()

        # assert
        self.assertEqual(actual_attack_power, actual_attack_power)
        self.assertEqual(expected_max_hit_points, actual_max_hit_points)
        self.assertEqual(expected_hit_points, actual_hit_points)
        self.assertEqual(expected_range, actual_range)
        self.assertEqual(expected_x_position, actual_x_position)
        self.assertEqual(expected_y_position, actual_y_position)
        self.assertEqual(expected_team, actual_team)


    def test_attack_not_within_range(self):
        # arrange
        unit = Unit(5, 10, 0, 0, Unit.US)
        target_unit = Unit(5, 10, 5, 5, Unit.THEM)
        expected_hit_points = 10

        # act
        unit.attack(target_unit)
        actual_hit_points = target_unit.get_hit_points()

        # assert
        self.assertEqual(expected_hit_points, actual_hit_points)

    def test_attack(self):
        # arrange
        unit = Unit(5, 10, 0, 0, Unit.US, 5)
        target_unit = Unit(5, 10, 1, 1, Unit.THEM)
        expected_hit_points = 5

        # act
        unit.attack(target_unit)
        actual_hit_points = target_unit.get_hit_points()

        # assert
        self.assertEqual(expected_hit_points, actual_hit_points)