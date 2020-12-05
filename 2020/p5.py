""""
--- Day 5: Binary Boarding ---

You board your plane only to discover a new problem: you dropped your boarding pass! You aren't sure which seat is yours, and all of the flight attendants are busy with the flood of people that suddenly made it through passport control.

You write a quick program to use your phone's camera to scan all of the nearby boarding passes (your puzzle input); perhaps you can find your seat through process of elimination.

Instead of zones or groups, this airline uses binary space partitioning to seat people. A seat might be specified like FBFBBFFRLR, where F means "front", B means "back", L means "left", and R means "right".

The first 7 characters will either be F or B; these specify exactly one of the 128 rows on the plane (numbered 0 through 127). Each letter tells you which half of a region the given seat is in. Start with the whole list of rows; the first letter indicates whether the seat is in the
front (0 through 63) or the back (64 through 127). The next letter indicates which half of that region the seat is in, and so on until you're left with exactly one row.

For example, consider just the first seven characters of FBFBBFFRLR:

* Start by considering the whole range, rows 0 through 127.
* F means to take the lower half, keeping rows 0 through 63.
* B means to take the upper half, keeping rows 32 through 63.
* F means to take the lower half, keeping rows 32 through 47.
* B means to take the upper half, keeping rows 40 through 47.
* B keeps rows 44 through 47.
* F keeps rows 44 through 45.
* The final F keeps the lower of the two, row 44.

The last three characters will be either L or R; these specify exactly one of the 8 columns of seats on the plane (numbered 0 through 7). The same process as above proceeds again, this time with only three steps. L means to keep the lower half, while R means to keep the
upper half.

For example, consider just the last 3 characters of FBFBBFFRLR:

* Start by considering the whole range, columns 0 through 7.
* R means to take the upper half, keeping columns 4 through 7.
* L means to take the lower half, keeping columns 4 through 5.
* The final R keeps the upper of the two, column 5.

So, decoding FBFBBFFRLR reveals that it is the seat at row 44, column 5.

Every seat also has a unique seat ID: multiply the row by 8, then add the column. In this example, the seat has ID 44 * 8 + 5 = 357.

Here are some other boarding passes:

* BFFFBBFRRR: row 70, column 7, seat ID 567.
* FFFBBBFRRR: row 14, column 7, seat ID 119.
* BBFFBBFRLL: row 102, column 4, seat ID 820.

As a sanity check, look through your list of boarding passes. What is the highest seat ID on a boarding pass?
"""
def parse_seat_string(s):
    #seat_number = [0] * 10
    seat_number = ''
    for idx, c in enumerate(s):
        #print(c)
        if c == 'B' or c == 'R':
            #seat_number[idx] = 1
            seat_number += '1'
        elif c == 'F' or c == 'L':
            seat_number += '0'
    return seat_number
#print(parse_seat_string('BFFFBBFRRR'))

rawdata = list(map(str , open("input-p5.txt")))
cleandata = [None] * len(rawdata)
for idx, s in enumerate(rawdata):
    cleandata[idx] = parse_seat_string(s)
cleandata.sort()
#print(cleandata)

def seat_id(string_binary):
    row_2 = string_binary[0:7]
    col_2 = string_binary[7:]
    row_10 = int(row_2, 2)
    col_10 = int(col_2, 2)
    #print("row_2 " + row_2 + " row_10 " + str(row_10) + " col " + col_2 + " col_10 " + str(col_10))
    seat_id_10 = row_10 * 8 + col_10
    return seat_id_10

def part_a(data):
    highest_seat_bin = data[len(data) - 1]
    #print(highest_seat_bin)
    return str(seat_id(highest_seat_bin))


print("part_a " + part_a(cleandata))


print("\npart_b")
seat_ids = [None] * len(cleandata)
sum_of_seat_ids = 0
for idx, bin_seat in enumerate(cleandata):
    id_10 = seat_id(bin_seat)
    seat_ids[idx] = id_10
    sum_of_seat_ids += id_10
print("...sum of seat ids " + str(sum_of_seat_ids))

lowest_seat_id_10 = int(seat_ids[0])
print("...lowest seat id " + str(lowest_seat_id_10))
sum_of_missing_seats = lowest_seat_id_10 * ((lowest_seat_id_10 - 1) / 2)
print("...sum of missing seats " + str(sum_of_missing_seats))

#print(str(seat_ids[0]))
highest_seat_10 = seat_ids[len(seat_ids) - 1]
sum_of_possible_seat_ids = (highest_seat_10 + 1) * (highest_seat_10 / 2)
print("...sum of possible seat ids " + str(sum_of_possible_seat_ids))

my_seat_id = sum_of_possible_seat_ids - (sum_of_seat_ids + sum_of_missing_seats)
print("my seat id " + str(my_seat_id))

print("\n\ndone")
