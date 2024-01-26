import numpy as np

def read_input(input_file):
    with open("input") as f:
        data = f.read().splitlines()
    return data

initial_grid = np.array([list(row) for row in read_input('14')])

# rounded rock (O)
# olid rock (#)
# an empty space (.)

# from Part 1
def spin_cycle(grid):

    for _ in range(4):
        # Rotate the grid 90 degrees clockwise
        grid = np.rot90(grid)

    # rearrange the columns
    for col in range(grid.shape[1]):

        # find the locations of the tags '#'
        tag_loc = np.where(grid[:, col] == '#')[0]

        # split the column based on tag locations
        split_arrays = np.split(grid[:, col], tag_loc)

        for sub_array in split_arrays:

            # reorganize the sub_array
            count_o = np.where(sub_array == 'O')[0].shape[0]

            # only check the arrays with O's
            if count_o > 0:

                if sub_array[0] == '#':

                    # fill the first count_o elements with O
                    sub_array[1:(count_o+1)] = 'O'

                    # fill the remaining elements with .
                    sub_array[(count_o+1):] = '.'

                else:
                    # fill the first count_o elements with O
                    sub_array[:count_o] = 'O'

                    # fill the remaining elements with .
                    sub_array[count_o:] = '.'

        # concatenate the updated split_arrays
        grid[:, col] = np.concatenate(split_arrays)

        return grid


# from Part 1
def calculate_total_load(grid):
    
    total = 0

    # ranks is the list that is a reverse range of grid.shape[0]
    ranks = list(range(grid.shape[0], 0, -1))
    # print(ranks) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

    for row in range(grid.shape[0]):
        # assign rank based on row index
        rank = ranks[row]

        # count the number of O's in each row
        count_o = np.where(grid[row, :] == 'O')[0].shape[0]

        # multiply the ranks with the number of O's
        total += rank * count_o

    return total



def find_cycle_length(initial_grid):

    grid = initial_grid.copy()
    grid_configs = set()

    for cycle in range(1, 1000000001):  # limit the search to avoid infinite loop
        grid = spin_cycle(grid)

        # convert the grid array to a tuple to use it as a hashable key
        grid_tuple = tuple(map(tuple, grid))

        if grid_tuple in grid_configs:
            return cycle - 1  # cycle length is found
        else:
            grid_configs.add(grid_tuple)



cycle_length = find_cycle_length(initial_grid)

# Run the spin cycle for the remaining cycles
remaining_cycles = 1000000000 % cycle_length

for _ in range(remaining_cycles):
    initial_grid = spin_cycle(initial_grid)


final_total_load = calculate_total_load(initial_grid)
print("Part 2:", final_total_load)
