import unittest
from Rover import Rover
i = Rover()
i.read_file("input.txt")


class TestCornerCases(unittest.TestCase):
    def test_different_map(self):
        i.x_bounds = 3
        i.y_bounds = 3
        self.assertEqual(str(i.initialise_rover()), '1 3 N\n3 1 E\n')
        i.output = []
        i.x_bounds = 5
        i.y_bounds = 5
        self.assertEqual(str(i.initialise_rover()), '1 3 N\n5 1 E\n')

    def test_out_of_bounds(self):
        i.output = []
        i.x_bounds = 2
        i.y_bounds = 2
        self.assertEqual(str(i.initialise_rover()), '1 2 N\nInitial rover coordinates out of plateau bounds')

if __name__ == '__main__':
    unittest.main()