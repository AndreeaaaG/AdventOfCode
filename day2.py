import re
from collections import defaultdict
import math

with open("input") as f:
    data = f.read().strip().split("\n")

sum_of_ids = 0
sum_of_power = 0

for line in data: 
    parts = re.sub("[:,;]", "", line).split()
    colorMax = defaultdict(int)
    
    # print(parts)
    # print(parts[1]) # takes the id
    # print(parts[2::2]) # takes only nr 
    # print(parts[3::2]) # takes only color names
    
    # for i in zip(parts[2::2], parts[3::2]):
    #     print(i)

    for nr, color in zip(parts[2::2], parts[3::2]):
        # print("max( ", colorMax[color], " , ", int(nr), " )")
        colorMax[color] = max(colorMax[color], int(nr))
        # print(colorMax[color])
    
    # print(colorMax["red"], colorMax["green"], colorMax["blue"])
    # print("\n")

    if colorMax["red"] <= 12 and colorMax["green"] <= 13 and colorMax["blue"] <= 14:
        sum_of_ids += int(parts[1])
        # print("Take ID: ", int(parts[1]), "\n")

    # print(colorMax.values())
    sum_of_power += math.prod(colorMax.values())

print(sum_of_ids) # part 1
print(sum_of_power) # part 2