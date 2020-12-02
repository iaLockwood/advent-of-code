# given a list of numbers, find the two entries that sum to 2020
# answer is the product of those two numbers
import timeit
from aocd import data

#datalist = ['1721', '979', '366', '299', '675', '1456']
#print("...debug ", end='')
#print(datalist)

visited_entries = {}
datalist = [int(x) for x in data.split()]

start = timeit.default_timer()

for idx, entry in enumerate(datalist):
    if entry in visited_entries:
#        print("...debug ", end='')
#        print("found entry in visited entries")
        retrieved_entry = datalist[visited_entries[entry]]
#        assert(int(entry) + int(retrieved_entry) == 2020)
#        print("entries which sum to 2020: " + entry + "," + retrieved_entry)
#        print("product is " + str(int(entry)*int(retrieved_entry)))
        break
#    print("...debug ", end='')
#    print(str(idx) + " " + entry)
    visited_entries[2020 - entry] = idx

stop = timeit.default_timer()
#print("...debug ", end='')
#print(visited_entries)
print('Time: ', stop - start)
print("done")
