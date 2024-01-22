def read_input(input_file):
    with open("input_in") as f:
        data = f.read().splitlines()
    return data

data = read_input('6')


times = [int(x) for x in data[0].split(': ')[1].split(' ') if x != '']
# print(times) # [7, 15, 30]

distances = [int(x) for x in data[1].split(': ')[1].split(' ') if x != '']
# print(distances) # [9, 40, 200]

# create tuples of (time, distance)
pairs = [(times[i], distances[i]) for i in range(len(times))]
# print(pairs) # [(7, 9), (15, 40), (30, 200)]

# Part 1
def get_distance_travelled(pair):
    # exclude 0 and max value as it never makes sense
    # start the counter
    counter = 0

    for i in range(1, pair[0]):
        # distance travelled with the current power
        distance = (pair[0] - i) * i

        if distance > pair[1]:
            counter += 1
    
        # print(counter, i)
    return counter


result = 1
for pair in pairs:
    result *= get_distance_travelled(pair)

print("part 1: ", result) # 288

# Part 2

# get the new time
new_time = data[0].split(': ')[1].split(' ')
# print(new_time) # ['', '', '', '', '', '7', '', '15', '', '', '30']

final_time = ""
for i in new_time:
    final_time += i
    
final_time = int(final_time)
# print(final_time) # 71530

# get the new distance
new_distance = data[1].split(': ')[1].split(' ')
# print(new_distance) # ['', '9', '', '40', '', '200']

final_distance = ""
for i in new_distance:
    final_distance += i

final_distance = int(final_distance)
# print(final_distance) # 940200

print("part 2: ", get_distance_travelled((final_time, final_distance))) # 71530