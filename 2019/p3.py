import unittest
from aocd.models import Puzzle

def find_nearest_collision(wire_paths):
    print(wire_paths)
    return 0

class TestClass(unittest.TestCase):

    def test_example_1(self):
        wire_paths = "R8,U5,L5,D3\nU7,R6,D4,L4"
        output = find_nearest_collision(wire_paths)
        self.assertEqual(output, 6)

    def test_part_a(self):
        puzzle = Puzzle(year=2019, day=3)
        #wire_paths = [int(x) for x in puzzle.input_data.split(',')]
        wire_paths = puzzle.input_data
        output = find_nearest_collision(wire_paths)

if __name__ == '__main__':
    unittest.main()
