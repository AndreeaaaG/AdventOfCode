import re

def read_input(input_file):
    with open("input_in") as f:
        data = f.read().splitlines()
    return data

data = read_input('5')


def get_maps():
    # get the maps as the list of lists
    maps = []
    current_map = []
    
    for line in data[1:]:
        if line == '':
            if current_map:
                maps.append(current_map)
                current_map = []
        else:
            current_map.append(line)

    if current_map:
        maps.append(current_map)

    return maps



maps = get_maps()
# print(maps)
# [['seed-to-soil map:', '50 98 2', '52 50 48'], ['soil-to-fertilizer map:', '0 15 37', '37 52 2', '39 0 15'], 
# ['fertilizer-to-water map:', '49 53 8', '0 11 42', '42 0 7', '57 7 4'], ['water-to-light map:', '88 18 7', '18 25 70'], 
# ['light-to-temperature map:', '45 77 23', '81 45 19', '68 64 13'], ['temperature-to-humidity map:', '0 69 1', '1 0 69'], ['humidity-to-location map:', '60 56 37', '56 93 4']]


seeds = [int(x) for x in data[0].split(': ')[1].split(' ')] 
# print(seeds) 
# for input : seeds: 79 14 55 13
#it prints: [79, 14, 55, 13]


def get_value_based_on_source_seed(source):

    source_value = source

    for m in maps:
        values = m[1:]

        for i in values:
            i = [int(x) for x in i.split(' ')]

            source_interval = range(i[1], i[1] + i[2])
            # print("source_interval", source_interval)

            # update source value for the next map
            if source_value in source_interval:

                # find the distance from the start of the interval
                distance = source_value - i[1]

                # new source value is the destination start + the distance
                source_value = i[0] + distance

                # source found, move to the next map
                break
            else:
                # keep the source value, move to the next map
                pass
            

    return source_value



# Part 1

final_values = [get_value_based_on_source_seed(seed) for seed in seeds]
# print(final_values)
# [82, 43, 86, 35]

print( "Part 1: ", min(final_values) ) # 35


# Part 2

def get_seed_ranges():
    #  generate all individual seed numbers within the specified ranges
    # before iterating over them to find their corresponding values

    seed_line = data[0].split(': ')[1]

    seed_ranges = [int(x) for x in re.findall(r'\b\d+\b', seed_line)] 
    # find all occurrences of one or more digits (\d+) that are surrounded by word boundaries (\b)

    return [(seed_ranges[i], seed_ranges[i+1]) for i in range(0, len(seed_ranges), 2)]



seed_ranges = get_seed_ranges()
# print(seed_ranges) 
# for input : seeds: 79 14 55 13
#it prints: [(79, 14), (55, 13)]


def generate_all_seeds(seed_ranges):
    # generate all seed numbers within those ranges
    all_seeds = []

    for start, length in seed_ranges:
        all_seeds.extend(range(start, start + length))
        
    return all_seeds


all_seeds = generate_all_seeds(seed_ranges)
# print(all_seeds)
# [79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67]

final_values = [get_value_based_on_source_seed(seed) for seed in all_seeds]
# print(final_values)
# [82, 83, 84, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 60, 86, 87, 88, 89, 94, 95, 96, 56, 57, 58, 59, 97, 98]

print("Part 2: ", min(final_values)) # 46
