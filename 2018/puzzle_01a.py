
infile = "puzzle_01.input"
frequency = 0

with open(infile) as f:
    array = []
    for line in f:
        #array.append(line)
        frequency += int(line)

print(frequency)
