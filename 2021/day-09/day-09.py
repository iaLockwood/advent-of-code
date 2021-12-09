#!/usr/bin/env python3
import sys

def parse_input(filename):
    rawdata = list(map(str.strip, open(filename)))
    data = []
    ninepad = [9]*(2 + len(rawdata[0]))
    data.append(ninepad)
    for n in rawdata:
        pointvals = [int(i) for i in n]
        padded = [9]
        padded += pointvals
        padded += [9]
        data.append(padded)
    data.append(ninepad)
    return data

def find_low_points(paddedgrid):
    lowvals = []
    lowpoints = []
    for y in range(1, len(paddedgrid) - 1):
        for x in range(1, len(paddedgrid[y]) - 1):
            pointval = paddedgrid[y][x]
            if pointval < paddedgrid[y][x+1] \
               and pointval < paddedgrid[y][x-1] \
               and pointval < paddedgrid[y+1][x] \
               and pointval < paddedgrid[y-1][x]:
                lowvals.append(pointval)
                lowpoints.append((y, x))
#            print(paddedgrid[y][x], end='')
#        print('\n', end='')
#    print(lowvals)
    return (lowvals, lowpoints)

def get_risk(lowvals):
    risk = 0
    for n in lowvals:
        risk += (n + 1)
    return risk

def test_example_1(data):
    print('...test_example_1')
#    print(data)
    lowvals, lowpoints = find_low_points(data)
    print(lowvals)
#    print(lowpoints)
    assert 15 == get_risk(lowvals)

def part_a(data):
    lowvals, lowpoints = find_low_points(data)
    result = get_risk(lowvals)
#    print(lowpoints)
    print('...part a: ' + str(result))

def get_points_in_basin_from_lowpoint(lowpoint, paddedgrid):
    tovisit = [lowpoint]
    inbasin = []
    visited = []
    while len(tovisit) > 0:
        point = tovisit.pop()
        y, x = point
        if point not in visited and paddedgrid[y][x] < 9:
            inbasin.append(point)
        if (y,x+1) not in visited and paddedgrid[y][x+1] < 9:
            tovisit.append((y,x+1))
        if (y,x-1) not in visited and paddedgrid[y][x-1] < 9:
            tovisit.append((y,x-1))
        if (y+1,x) not in visited and paddedgrid[y+1][x] < 9:
            tovisit.append((y+1,x))
        if (y-1,x) not in visited and paddedgrid[y-1][x] < 9:
            tovisit.append((y-1,x))
        visited.append(point)
    return inbasin

def get_num_locations_in_each_basin(lowpoints, paddedgrid):
    counts = []
    for lowpoint in lowpoints:
        points_in_basin = get_points_in_basin_from_lowpoint(lowpoint, paddedgrid)
        counts.append(len(points_in_basin))
    return counts

def product_of_three_largest(intlist):
    intlist.sort()
    bigthree = intlist[-3:]
    print(bigthree)
    product = 1
    for n in bigthree:
        product = product * n
    return product

def test_example_2(data):
# The size of a basin is the number of locations within the basin,
# including the low point. The example above has four basins.
# Find the three largest basins and multiply their sizes together.
# In the above example, this is 9 * 14 * 9 = 1134.
    print('...test_example_2')
#    print(data)
    lowvals, lowpoints = find_low_points(data)
    print(lowvals)
    print(lowpoints)
    sizes = get_num_locations_in_each_basin(lowpoints, data)
    print(sizes)
    assert 1134 == product_of_three_largest(sizes)

def part_b(data):
    lowvals, lowpoints = find_low_points(data)
    sizes = get_num_locations_in_each_basin(lowpoints, data)
    result = product_of_three_largest(sizes)
    print('...part b: ' + str(result))

def main():
    test_data = parse_input('day-09-example.txt')
    puzzle_data = parse_input('day-09-input.txt')

    test_example_1(test_data)
    part_a(puzzle_data)
    test_example_2(test_data)
    part_b(puzzle_data)

    print('done.')
    return 0

if __name__ == '__main__':
    sys.exit(main())
