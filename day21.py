import numpy as np
from collections import defaultdict

def read_input(input_file):
    with open("input") as f:
        data = f.read().splitlines()
    return data

# starting position (S)
# garden plots (.)
# rocks (#)

# initialize the grid as a numpy array
grid = np.array([list(row) for row in read_input('21')])


# find the starting position S
s_x, s_y = np.where(grid == 'S')

# initialize the dictionary to store the possible coordinates for each cycle
step_dict = defaultdict(list)

# initialize step_dict (step 0) with the location of S
step_dict[0].append((s_x[0], s_y[0])) 


# check each position to determine which are the next possible positions

def check_positions(x, y, step_list):
    # check the all 4 possible directions 

    if grid[x-1, y] != '#':
        step_list.append(((x-1), y))

    if grid[x+1, y] != '#':
        step_list.append(((x+1), y))

    if grid[x, y-1] != '#':
        step_list.append((x, (y-1)))

    if grid[x, y+1] != '#':
        step_list.append((x, (y+1)))

# it will store the results in the dictionary
        

reference = 64
current_step = 1

while current_step < (reference + 1):
    # loop over this process for the count of cycles specified in the problem
        
    previous_step = current_step - 1

    for i in step_dict[previous_step]:
        # check around each element in the previous step and update the dictionary step_dict for the current step
        check_positions(i[0], i[1], step_dict[current_step])
        
        # remove duplicates from it
        step_dict[current_step] = list(set(step_dict[current_step]))

    # update the current step
    current_step += 1


# the result is the length of the value of the last cycle in the dictionary
print("Part 1:", len(step_dict[reference]))