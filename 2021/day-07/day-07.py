#!/usr/bin/env python3
import sys

def parse_input(filename):
    data = list(map(str.strip, open(filename)))
    data = data[0].split(',')
    return list(map(int, data))

def find_delta_from_i_to_j(i, j):
    # find the difference from i to j
    return abs(j - i)

def fuel_cost_from_i_to_j(i, j):
    delta = abs(j - i)
    remainder = delta % 2
    if remainder == 1:
        pairsum = delta
        sumsums = ((delta // 2) * pairsum) + pairsum
        return sumsums
    else:
        pairsum = delta + 1
        sumsums = ((delta // 2) * pairsum)
        return sumsums

def brute_force(numlist, fuel_function):
    highest = 0
    for n in numlist:
        if n > highest:
            highest = n
    print('highest number found: ' + str(highest))
    totalCostToEachJ = []
    for j in range(0,highest):
        totalfuel = 0
        for n in numlist:
            totalfuel += fuel_function(n, j)
        totalCostToEachJ.append(totalfuel)
#    print(totalCostToEachJ)
    lowest = 99999999
    for cost in totalCostToEachJ:
        if cost < lowest:
            lowest = cost
    print(lowest)
    return lowest

def test_example_1(data):
    print(data)
    value = brute_force(data, find_delta_from_i_to_j)
    assert 37 == value

def part_a(data):
    result = brute_force(data, find_delta_from_i_to_j)
    print('part a: ' + str(result))

def test_example_2(data):
    value = brute_force(data, fuel_cost_from_i_to_j)
    assert 168 == value

def part_b(data):
    result = brute_force(data, fuel_cost_from_i_to_j)
    print('part b: ' + str(result))

def main():
    test_data = parse_input('day-07-example.txt')
    puzzle_data = parse_input('day-07-input.txt')

    test_example_1(test_data)
    part_a(puzzle_data)
    test_example_2(test_data)
    part_b(puzzle_data)

    print('done.')
    return 0

if __name__ == '__main__':
    sys.exit(main())
