import math
from aocd.models import Puzzle
year = 2019
day = 1
puzzle = Puzzle(year, day)
#print(puzzle.input_data)

# 1969 is 654 + 216 + 70 + 21 + 5 = 966
def calculate_fuel(fuel):
    additional_fuel = math.floor(int(fuel) / 3) - 2
    ret_val = 0
    if additional_fuel<= 0:
        retval = fuel
    else:
        ret_val = additional_fuel + calculate_fuel(additional_fuel)
    print(ret_val)
    return ret_val

#print(" 1969 is 654 + 216 + 70 + 21 + 5 = 966")
#calculated_fuel = calculate_fuel(1969)
#print("calculated_fuel=" + str(calculated_fuel))

a = puzzle.input_data.split()
b = []
for x in a:
    b.append(calculate_fuel(x))

my_answer = 0
for x in b:
    my_answer += x

from aocd import submit
print("my_answer=" + str(my_answer))
submit(my_answer, part="b", day=1, year=2019)
