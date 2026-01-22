from unittest import TestCase
from main import binary_search

class Test(TestCase):
    def test_binary_search_found_lower(self):
        # arrange
        numbers = [3, 4, 5, 6, 7, 8, 10, 20, 50, 100]
        expected_index = 0

        # act
        actual_index = binary_search(3, numbers)

        # assert
        self.assertEqual(expected_index, actual_index)

    def test_binary_search_found(self):
        # arrange
        numbers = [3, 4, 5, 6, 7, 8, 10, 20, 50, 100]
        expected_index = 7

        # act
        actual_index = binary_search(20, numbers)

        # assert
        self.assertEqual(expected_index, actual_index)

    def test_binary_search_not_found(self):
        # arrange
        numbers = [3, 4, 5, 6, 7, 8, 10, 20, 50, 100]
        expected_index = -1

        # act
        actual_index = binary_search(21, numbers)

        # assert
        self.assertEqual(expected_index, actual_index)
