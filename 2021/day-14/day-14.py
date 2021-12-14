#!/usr/bin/env python3
import sys

def parse_input(filename):
    rawdata = list(map(str.strip, open(filename)))
    polymerTemplate = rawdata[0]
    insertionRules = []
    for line in rawdata[2:]:
        insertionRules.append(line.split(' -> '))
    return (polymerTemplate, insertionRules)

def apply_step(s, rules):
    pairs = get_pairs_from_string(s)
#    print(pairs)
    pairsAfterInsertion = []
    for pair in pairs:
        for rule in rules:
            if(pair == rule[0]):
                pairsAfterInsertion.append(pair[:1] + rule[1] + pair[1:])
                break
            # DOESN'T HANDLE NO MATCHING RULE
    return merge_pairs_into_string(pairsAfterInsertion)

def get_pairs_from_string(s):
    pairs = []
    for x in range(len(s) - 1):
        pairs.append(s[x:x+2])
    return pairs

def merge_pairs_into_string(pairList):
    newstring = pairList[0]
    for i in range(1, len(pairList)):
        pair = pairList[i]
        newstring += pair[1:]
    return newstring

def get_most_and_least_common_element(s):
    countmap = {}
    for i in range(len(s)):
        if(s[i] in countmap):
            countmap[s[i]] = countmap[s[i]] + 1
        else:
            countmap[s[i]] = 1
    high = 0
    highchar = ""
    low = 999999
    lowchar = ""
    for key in countmap:
        if(countmap[key] > high):
            high = countmap[key]
            highchar = key
        if(countmap[key] < low):
            low = countmap[key]
            lowchar = key
#    print(countmap)
    return ((highchar, countmap[highchar]), (lowchar, countmap[lowchar]))

def test_example_1(data):
    template, rules = data
#    print(template, end='\n\n')
#    print(rules, end='\n\n')
    afterOneStep = apply_step(template, rules)
    assert afterOneStep == "NCNBCHB"
    i = 0
    s = template
    while i < 4:
        s = apply_step(s, rules)
        i += 1
    assert s == "NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB"
    while i < 10:
        s = apply_step(s, rules)
        i += 1
    hightuple, lowtuple = get_most_and_least_common_element(s)
#    print(hightuple)
#    print(lowtuple)
    # difference between most and least common elements should be 1588
    assert 1588 == (hightuple[1] - lowtuple[1])

def part_a(data):
    print('part a...')
    template, rules = data
    i = 0
    s = template
    while i < 10:
        print('applying step ' + str(i))
        s = apply_step(s, rules)
        i += 1
    hightuple, lowtuple = get_most_and_least_common_element(s)
    result = hightuple[1] - lowtuple[1]
    print('...result part a: ' + str(result))

def part_b(data):
    print('part b...')
    template, rules = data
    i = 0
    s = template
    while i < 40:
        print('applying step ' + str(i))
        s = apply_step(s, rules)
        i += 1
    hightuple, lowtuple = get_most_and_least_common_element(s)
    result = hightuple[1] - lowtuple[1]
    print('...result part b: ' + str(result))

def main():
    test_data = parse_input('day-14-example.txt')
    puzzle_data = parse_input('day-14-input.txt')

    test_example_1(test_data)
    part_a(puzzle_data)
    part_b(puzzle_data)

    print('done.')
    return 0

if __name__ == '__main__':
    sys.exit(main())
