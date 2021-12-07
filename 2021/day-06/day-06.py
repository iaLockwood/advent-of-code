#!/usr/bin/env python3
import sys

def parse_input(filename):
    data = list(map(str.strip, open(filename)))
    data = data[0].split(',')
    data = list(map(int, data))
    return data

def simulate_n_days(fishlist, n):
    population = list(fishlist)
    for day in range(0,n):
        #print('...day: ' + str(day))
        #print(population)
        newpop = []
        for fish in population:
            #print(fish)
            aged_fish = fish_ages(fish)
            #print(aged_fish)
            newpop += aged_fish
        population = newpop
    print(len(population))
    return len(population)

def fish_ages(fish):
    if(fish == 0):
        return [6, 8]
    elif(fish < 9):
        return [fish - 1]
    else:
        return []

def fish_ages_fast(fish):
    if(fish == 8):
        return [0]
    elif(fish == 7):
        return [6, 8]
    elif(fish == 6):
        return [5, 7]
    elif(fish == 5):
        return [4, 6]
    elif(fish == 4):
        return [3, 5]
    elif(fish == 3):
        return [2, 4]
    elif(fish == 2):
        return [1, 3]
    elif(fish == 1):
        return [0, 2]
    else: # fish == 0
        return [0, 6, 1, 3]

def simulate_8n_days(fishlist, n):
    population = list(fishlist)
    for day in range(0,n // 8):
        print('...day: ' + str(day))
        #print(population)
        newpop = []
        for fish in population:
            #print(fish)
            aged_fish = fish_ages_fast(fish)
            #print(aged_fish)
            newpop += aged_fish
        population = newpop
    print(len(population))
    return len(population)
    count = 0
    return count

def test_example_1(data):
    print(data)
    assert 26 == simulate_n_days(data, 18)
    assert 5934 == simulate_n_days(data, 80)

def part_a(data):
    result = simulate_n_days(data, 80)
    print('part a: ' + str(result))

def test_example_2(data):
    print(data)
    assert 26984457539  == simulate_8n_days(data, 256)

def part_b(data):
    result = simulate_n_days(data, 256)
    print('part b: ' + str(result))

def main():
    test_data = parse_input('day-06-example.txt')
    puzzle_data = parse_input('day-06-input.txt')

    test_example_1(test_data)
    part_a(puzzle_data)

    test_example_2(test_data)
    #part_b(puzzle_data)

    print('done.')
    return 0

if __name__ == '__main__':
    sys.exit(main())
