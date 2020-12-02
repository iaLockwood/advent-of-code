# Given a list of passwords (according to the corrupted database)
# and the corporate policy when that password was set
testdata = ['1-3 a: abcde\n','1-2 b: cdefg\n','2-9 c: ccccccccc\n']
# how many passwords are valid according to their policies?

data = list(map(str, open("input-p2.txt")))


import re
p = re.compile('(\d+)-(\d+) ([a-z]): ([a-z]*)\n')

# where
# <min c occur>-<max c occur> <c>: <string>
def part_a(data):
    num_valid = 0
    for s in data:
        #print("...debug... top of loop")
        m = p.match(s)
        lo = int(m.group(1))
        hi = int(m.group(2))
        target = m.group(3)
        password = m.group(4)
        occurences = password.count(target)
        if occurences <= hi:
            if occurences >= lo:
                num_valid += 1
    return num_valid

# where
# exactly one of two given position contains the target letter c
# <position 1 of c>-<position 2 of c> <c>: <string ostensibly containing c>
# note, position is 1-indexed
def part_b(data):
    num_valid = 0
    for s in data:
        m = p.match(s)
        pos1 = int(m.group(1)) - 1
        pos2 = int(m.group(2)) - 1
        target = m.group(3)
        password = m.group(4)
        if (password[pos1] == target) ^ (password[pos2] == target):
            #print("...debug VALID")
            num_valid += 1
        #else:
        #    print("...debug INVALID")
    return num_valid

print("num_valid_a: " + str(part_a(data)))
print("num_valid_b: " + str(part_b(data)))

print("\n\ndone")
