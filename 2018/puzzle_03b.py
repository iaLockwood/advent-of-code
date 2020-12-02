def show(array, width, height):
    for i in range(0, width):
        for j in range(0, height):
            print(array[i][j], end='')
        print('')
    print('')
    pass

def claim(array, x, y, width, height):
    for i in range(x, x + width):
        for j in range(y, y + height):
            array[i][j] = array[i][j] + 1
    pass

#grid = [[0 for i in range(10)] for j in range(10)]
#show(grid, 10, 10)
#claim(grid, 1, 3, 4, 4)
#claim(grid, 3, 1, 4, 4)
#claim(grid, 5, 5, 2, 2)
#show(grid, 10, 10)

#  parse lines of the form
#  #16 @ 320,546: 10x28
grid = [[0 for i in range(1000)] for j in range(1000)]
import re
with open('puzzle_03.input') as f:
    for line in f:
        a = [int(s) for s in re.findall(r'\d+', line)]
        claim(grid, a[1], a[2], a[3], a[4])

overlap = 0
for i in range(0, 1000):
    for j in range(0, 1000):
        if grid[i][j] > 1:
            overlap += 1
print(overlap)
