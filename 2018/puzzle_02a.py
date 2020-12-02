
infile = "puzzle_02.input"
box_ids = []

with open(infile) as f:
    for line in f:
        box_ids.append(line.rstrip())

num_pairs = 0
num_triplets = 0
for box_id in box_ids:
    char_dict = {}
    for letter in box_id:
        if letter in char_dict:
            char_dict[letter] = char_dict[letter] + 1
        else:
            char_dict[letter] = 1
    #print(box_id)
    for key in char_dict:
        #print(' ' + key + ' ' + str(char_dict[key]))
        if char_dict[key] == 2:
            num_pairs += 1
            break
    for key in char_dict:
        if char_dict[key] == 3:
            num_triplets += 1
            break
print('num_pairs:' + str(num_pairs))
print('num_triplets:' + str(num_triplets))
print('product:' + str(num_pairs * num_triplets))
print('done')
