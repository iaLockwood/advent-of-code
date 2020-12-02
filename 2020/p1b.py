# given a list of numbers, find the THREE entries that sum to 2020
# answer is the product of those THREE numbers
import timeit

testdata = [1721, 979, 366, 299, 675, 1456]
data = list(map(int, open('input-p1.txt')))

#print("...debug ", end='')
#print(testdata)
#print(data)
start = timeit.default_timer()

def brute_force(entries):
    for i in entries:
        for j in entries:
            for k in entries:
                if i + j + k == 2020:
                    return (i, j, k)
    return (0, 0, 0)

answer = brute_force(data)
print(answer)
print("product: " + str(answer[0] * answer[1] * answer[2]))

stop = timeit.default_timer()
print('Time: ', stop - start)
print("done")
