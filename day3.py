import re
import itertools
import math

with open("input") as f:
    data = f.read().strip().split("\n")

square = list(itertools.product((-1, 0, 1), (-1, 0, 1))) # for checking the adjacent number possitions to a symbol

symbol_list = {
    (i, j): (x, [])
    for i, line in enumerate(data)
    for j, x in enumerate(line)
    if x != "." and not x.isdigit()
}

final_sum = 0

for i, line in enumerate(data):
    for match in re.finditer(r"\d+", line):

        nr = int(match.group(0)) # takes only the numbers

        boundary = {
            (i + di, j + dj)
            for di, dj in square
            for j in range(match.start(), match.end())
        }
       
        if symbol_list.keys() & boundary:
            final_sum += nr # add the number to the final sum

        for symbol in symbol_list.keys() & boundary:
            symbol_list[symbol][1].append(nr) # add also the number to the symbol list that is associate with

# Part 1
print(final_sum)

# Part 2
sum_rations = sum(
    math.prod(number_list)
    for symbol, number_list in symbol_list.values() # search in the dict values for the two possible gears
    if len(number_list) == 2 and symbol == "*" # check if theare are correct two gears
    )

print(sum_rations)