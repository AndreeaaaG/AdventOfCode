from collections import defaultdict

def read_input(input_file):
    with open("input_in") as f:
        data = f.read().splitlines()
    return data


# Part 1

def ascii_func(a_str):
    # the results per character are not calculated individually and then summed up
    # the current number is updated after looping over each character 
    current = 0
    for i in a_str:

        # first update the current with the ascii value of i
        current += ord(i)
        current = (current * 17) % 256 # the problem instructions

    return current


result = 0
# perform the function for every character in the input file, and then sum the results
for a in read_input('15')[0].split(','):
    result += ascii_func(a)

print("Part 1:", result) # 1320



# Part 2

boxes = defaultdict(dict) # initialize the dictionary with a dict as the default value

# when we loop over all the strings in the input file, we will get two types of instructions:
# update the focal length or remove the label from the box

for a in read_input('15')[0].split(','):

    if '=' in a:
        label = a.split('=')[0]
        focal_length = int(a.split('=')[1])
        box = ascii_func(label)

        # lookup the label in the corresponding box, and update the focal length
        boxes[box][label] = focal_length

    else:
        label = a.split('-')[0]
        box = ascii_func(label)

        # lookup the label in the corresponding box, and remove the label
        if label in boxes[box]:
            boxes[box].pop(label)


sum_all = 0

for box in boxes: 
    keys = list(boxes[box].keys())

    # we look at each label in each box

    for key, value in boxes[box].items():
        order = keys.index(key) + 1
        sum_all += (box+1) * order * value
        # the corresponding number is the value variable, that is multiplied by the number of the box + 1 and by its order in the box

print("Part 2:", sum_all) # 145