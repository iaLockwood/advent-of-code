#!/usr/bin/env python3
import sys

def parse_input(filename):
    data = list(map(str, open(filename)))
    print(data)
    map_idx_count0 = {}
    map_idx_count1 = {}
#    print(map_idx_count0)
#    print(map_idx_count1)
    for s in data:
        #print(s)
        for idx in range(len(s)):
            if s[idx] == "0":
                #print('match 0')
                if idx in map_idx_count0:
                    map_idx_count0[idx] += 1
                else:
                    map_idx_count0[idx] = 1
            elif s[idx] == "1":
                #print('match 1')
                if idx in map_idx_count1:
                    map_idx_count1[idx] += 1
                else:
                    map_idx_count1[idx] = 1
            elif s[idx == "\n"]:
                #print('newline character')
                continue
            else:
                print('ERROR')
                sys.exit(1)
    print(map_idx_count0)
    print(map_idx_count1)
    # walk maps and build binary numbers
    gamma = ""
    epsilon = ""
    for i in range(len(data[0]) - 1):
        if(map_idx_count0[i] > map_idx_count1[i]):
            #print("more zeros")
            gamma += "0"
            epsilon += "1"
        elif(map_idx_count0[i] < map_idx_count1[i]):
            #print("more ones")
            gamma += "1"
            epsilon += "0"
        else:
            print('ERROR')
            sys.exit(1)
    print(gamma)
    print(epsilon)
    #convert binary to decimal
    return (int(gamma, 2), int(epsilon, 2))

def test_example_1(data):
    g, e = data
    # found from most common bit
    gammaBinary = '10110'
    gammaDecimal = 22
    # found from lease common bit
    epsilonBinary = '01001'
    epsilonDecimal = 9
    # product of gamma and epsilon
    powerConsumption = 198
    assert g * e == 198

def part_a(data):
    g, e = data
    result = g * e
    print('part a: ' + str(result))

def part_b(data):
    result = 0
    print('part b: ' + str(result))

def main():
    test_data = parse_input('day-03-example.txt')
    test_example_1(test_data)

    puzzle_data = parse_input('day-03-input.txt')
    part_a(puzzle_data)
    part_b(puzzle_data)

    print('done.')
    return 0

if __name__ == '__main__':
    sys.exit(main())
