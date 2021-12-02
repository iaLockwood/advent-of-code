#!/usr/bin/env python3
import sys

def count_increases(numList):
    count = 0
    curr = 1
    prev = 0
    limit = len(numList)
    while curr < limit:
        if numList[curr] > numList[prev]:
            count += 1
        curr += 1
        prev += 1
    return count

def test_example_1(data):
    #print(data)
    assert count_increases(data) == 7

def part_a(data):
    result = count_increases(data)
    print('part a: ' + str(result))

def count_triplet_increases(numList):
    count = 0
    w1 = 0
    w2 = 1
    w3 = 2
    w4 = 3
    limit = len(numList)
    while w4 < limit:
        windowSum1 = numList[w1] + numList[w2] + numList[w3]
        windowSum2 = numList[w2] + numList[w3] + numList[w4]
        if windowSum2 > windowSum1:
            count +=1
        w1 += 1
        w2 += 1
        w3 += 1
        w4 += 1
    return count

def part_b(data):
    result = count_triplet_increases(data)
    print('part b: ' + str(result))

def test_example_2(data):
    assert count_triplet_increases(data) == 5

def main():
    test_data = list(map(int, open('day-01-example.txt')))
    test_example_1(test_data)

    puzzle_data = list(map(int, open('day-01-input.txt')))
    part_a(puzzle_data)

    test_example_2(test_data)
    part_b(puzzle_data)

    print('done.')
    return 0

if __name__ == '__main__':
    sys.exit(main())
