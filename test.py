import unittest
from Rover import Rover


class TestCornerCases(unittest.TestCase):
    def test_different_map(self):
        i = Rover()
        i.read_file("input.txt")
        # i.x_bounds = 3
        # i.y_bounds = 3
        self.assertEqual(str(i.initialise_rover()), '1 3 N \n 5 1 E')

if __name__ == '__main__':
    unittest.main()