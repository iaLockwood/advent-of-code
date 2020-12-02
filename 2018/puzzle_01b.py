
infile = "puzzle_01.input"
input_ints = []
frequency = 0

with open(infile) as f:
    for line in f:
        input_ints.append(int(line))

freq_dict = {}
count = 0
no_collision = True
while no_collision:
    for val in input_ints:
        count += 1
        frequency += val
        if frequency in freq_dict:
            print(frequency)
            no_collision = False
            break
        freq_dict[frequency] = count
#print('len(freq_dict):' + str(len(freq_dict)))
#print('frequency:' + frequency))
print('done')
