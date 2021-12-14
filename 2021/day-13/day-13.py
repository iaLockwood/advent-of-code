#!/usr/bin/env python3
import sys

def parse_input(filename, numfolds):
    rawdata = list(map(str.strip, open(filename)))
    folds = []
    for s in rawdata[-numfolds:]:
        foldins = s[11:].split('=')
        folds.append((foldins[0], int(foldins[1])))
    points = []
    xmax = 0
    ymax = 0
    for line in range(len(rawdata) - numfolds - 1):
        pointlist = rawdata[line].split(',')
        #points.append((int(pointlist[0]), int(pointlist[1])))
        pointtuple = (int(pointlist[0]), int(pointlist[1]))
        points.append(pointtuple)
        if(pointtuple[0] > xmax):
            xmax = pointtuple[0]
        if(pointtuple[1] > ymax):
            ymax = pointtuple[1]
#    print('xmax: ' + str(xmax))
#    print('ymax: ' + str(ymax))
    return (points, folds)

def init_2d_grid(lenx, leny):
    grid = []
    for row in range(leny):
        grid.append([])
        for col in range(lenx):
            grid[row].append('.')
    return grid

def sum_2d_grid(grid):
    print('\n')
    numdots = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
#            print(grid[row][col], end='')
            if(grid[row][col] == "#"):
                numdots += 1
#        print('\n')
#    print('total number of dots in above grid: ' + str(numdots))
    print('\n')
    return numdots

def print_2d_grid(grid):
    print('\n')
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            print(grid[row][col], end='')
        print('')
    print('\n')

def load_grid(grid, points):
    for point in points:
        x, y = point
        # note reversal
        grid[y][x] = '#'

def fold_grid_horizontal_along_y(grid, y):
#    print('fold_grid_horizontal_along_y ' + str(y))
    oldlastrow = len(grid) - 1
    lower = oldlastrow - y
#    print('oldlastrow: ' + str(oldlastrow))
    if(lower <= y):
#        print('oldlastrow - y <= y, fold will not go above top')
        for yoffset in range(1, len(grid) - y):
            for column in range(len(grid[y + yoffset])):
                if(grid[y + yoffset][column] == "#"):
                    grid[y - yoffset][column] = "#"
        return grid[:y]
    else:
        print('oldlastrow - y >= y, below fold is larger than above')
        print("NOT IMPLEMENTED")
        return []


def fold_grid_vertical_along_x(grid, x):
#    print('fold_grid_vertical_along_x ' + str(x))
    leftstart = 0
    leftend = x
    rightstart = x + 1
    rightend = len(grid[0])
    if((rightend - rightstart) <= (leftend - leftstart)):
#        print('rightend - rightstart < leftend - leftstart')
        for rownum in range(len(grid)):
#            print('rownum: ' + str(rownum))
            for xoffset in range(1, rightend - x):
                if(grid[rownum][x + xoffset] == "#"):
                    grid[rownum][x - xoffset] = "#"
            totrim = grid[rownum]
            grid[rownum] = totrim[:x]
    else:
        print('rightend - rightstart > leftend - leftstart')
        print('NOT IMPLEMENTED')
    return grid

def do_folds(grid, folds):
#    print(folds)
    newgrid = grid
    count = 0
    for fold in folds:
        axis, value = fold
#        print(axis)
        if axis == "y":
            newgrid = fold_grid_horizontal_along_y(newgrid, value)
        else:
            newgrid = fold_grid_vertical_along_x(newgrid, value)
#        count = sum_2d_grid(newgrid)
#    print_2d_grid(newgrid)
#    return count
    return newgrid

def test_example_1(data):
    print('test_example_1...')
#    print(data)
    points, folds = data
    grid = init_2d_grid(11, 15)
#    print(grid)
#    print_2d_grid(grid)
    load_grid(grid, points)
#    print_2d_grid(grid)
    result = do_folds(grid, folds[:1])
    print_2d_grid(result)
    result2 = do_folds(grid, folds[1:])

def part_a(data):
    points, folds = data
    grid = init_2d_grid(1311, 895)
    load_grid(grid, points)
    newgrid = do_folds(grid, folds[:1])
    result = sum_2d_grid(newgrid)
    print('...result part a: ' + str(result))

def part_b(data):
    points, folds = data
    grid = init_2d_grid(1311, 895)
    load_grid(grid, points)
    print('...result part b: ')
    newgrid = do_folds(grid, folds)
    print_2d_grid(newgrid)

def main():
    test_data = parse_input('day-13-example.txt', 2)
    puzzle_data = parse_input('day-13-input.txt', 12)

    test_example_1(test_data)
    part_a(puzzle_data)
    part_b(puzzle_data)

    print('done.')
    return 0

if __name__ == '__main__':
    sys.exit(main())
