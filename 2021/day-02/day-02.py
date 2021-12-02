#!/usr/bin/env python3
import sys

def parse_input(filename):
    data = list(map(str, open(filename)))
    return data

def test_example_1(data):
    print(data)
    assert 0 == 1

def part_a(data):
    result = 0
    print('part a: ' + str(result))

def part_b(data):
    result = 0
    print('part b: ' + str(result))

def main():
    test_data = parse_input('day--example.txt')
    puzzle_data = parse_input('day--input.txt')

    test_example_1(test_data)
    part_a(puzzle_data)
    part_b(puzzle_data)

    print('done.')
    return 0

if __name__ == '__main__':
    sys.exit(main())
