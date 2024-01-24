import numpy as np

def read_input(input_file):
    with open("input_in") as f:
        data = f.read().splitlines()
    return data

data = []
for line in read_input('9'):
    int_list = [int(i) for i in line.split()]
    data.append(int_list)

# Part 1

def sum_part_1(int_list):

    pattern = np.array(int_list, dtype=int).reshape(1, -1)
    final_number = 0

    # define a new array with differences

    #  if not all elements in the differences array are 0,
    while not np.all(np.diff(pattern) == 0):

        final_number += pattern[-1, -1] # take a record of the final element and replace the input array with the new array
        pattern = np.diff(pattern)
    # within the same loop, sum the final elements    
    else:
        final_number += pattern[-1, -1] # still add the last number

    return final_number


result = 0
for i in data:
    result += sum_part_1(i) # the sum of the resulting final numbers for each input line
print("Part 1:", result)



# Part 2
def sum_part_2(int_list):

    pattern = np.array(int_list, dtype=int).reshape(1, -1)
    final_number = 0 
    sign = 1 # this variable will be switched from 1 to -1, and also from -1 to 1, after each loop.

    # if not all elements in the differences array are 0,
    while not np.all(np.diff(pattern) == 0):

        final_number += pattern[0, 0] * sign #  take a record of the first element, and not the last one
        sign *= -1  
        pattern = np.diff(pattern)
    # within the same loop, sum the final elements
    else:
        # still add the first number
        final_number += pattern[0, 0] * sign
        sign *= -1

    return final_number


result = 0
for i in data:
    result += sum_part_2(i)
print("Part 2:", result)