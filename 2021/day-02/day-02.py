#!/usr/bin/env python3
import sys

def parse_input(filename):
    inputLines = list(map(str, open(filename)))
    course = []
    for line in inputLines:
        direction, magnitude = line.split(' ')
        course.append((direction, int(magnitude)))
    return course

def plot_course(courseList):
    x = 0
    y = 0
    for i in range(len(courseList)):
        direction, magnitude = courseList[i]
        if(direction == 'forward'):
            x += magnitude
        elif(direction == 'down'):
            y += magnitude
        elif(direction == 'up'):
            y -= magnitude
        else:
            sys.exit(1)
    finalPosition = (x, y)
    print(finalPosition)
    return finalPosition

def test_example_1(data):
    finalX, finalY = plot_course(data)
    assert 150 == finalX * finalY

def part_a(data):
    finalX, finalY = plot_course(data)
    result = finalX * finalY
    print('part a: ' + str(result))

def plot_course_b(courseList):
    x = 0
    y = 0
    aim = 0
    for i in range(len(courseList)):
        #print('--- top of loop')
        #print('x: ' + str(x) + ' y: ' + str(y) + ' aim: ' + str(aim))
        direction, magnitude = courseList[i]
        if(direction == 'forward'):
            y += aim * magnitude
            x += magnitude
        elif(direction == 'down'):
            aim += magnitude
        elif(direction == 'up'):
            aim -= magnitude
        else:
            sys.exit(1)
        #print('x: ' + str(x) + ' y: ' + str(y) + ' aim: ' + str(aim))
    finalPosition = (x, y)
    print(finalPosition)
    return finalPosition

def test_example_2(data):
    finalX, finalY = plot_course_b(data)
    assert 900 == finalX * finalY

def part_b(data):
    finalX, finalY = plot_course_b(data)
    result = finalX * finalY
    print('part b: ' + str(result))

def main():
    test_data = parse_input('day-02-example.txt')
    puzzle_data = parse_input('day-02-input.txt')

    test_example_1(test_data)
    part_a(puzzle_data)
    test_example_2(test_data)
    part_b(puzzle_data)

    print('done.')
    return 0

if __name__ == '__main__':
    sys.exit(main())
