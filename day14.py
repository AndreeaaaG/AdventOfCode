import numpy as np

def read_input(input_file):
    with open("input_in") as f:
        data = f.read().splitlines()
    return data

grid = np.array([list(row) for row in read_input('14')])

# rounded rock (O)
# olid rock (#)
# an empty space (.)

# Part 1

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


print("Part 1:", total) # 136