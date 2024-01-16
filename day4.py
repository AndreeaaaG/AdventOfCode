import re
import numpy as np

with open("input") as f:
    data = f.read().strip().split("\n")

ns = [list(map(int, re.findall(r"\d+", x))) for x in data]
# print("ns", ns)
# extract in lists all the numbers for each row, searching with regex for digits in input file

# for n in ns:
#     print(n[1:])
#     print(set(n)) # transform in set to have no dublicated numbers 
#     print(set(n[1:11])) # select all elemnts except the last 3
#     print(set(n[11:])) # select just the last 3 elements
#     print('\n')


winning_nr_list = [ set(n[11:]) & set(n[1:11]) for n in ns]
# print("winning_nr_list", winning_nr_list)
# it shows the list with only the dublicated numbers
# [{48}, {32}, {1, 21}, set(), set(), set()]


winning_nr = [len( set(n[11:]) & set(n[1:11]) ) for n in ns]
# print("winning_nr", winning_nr)
# it counts the length for those dublicated numbers list
# [1, 1, 2, 0, 0, 0]

# Part 1
final_sum = sum(2 ** (w - 1) for w in winning_nr if w > 0)
print("final_sum", final_sum, '\n') # 4
# calculate the final result for the above list with the lengths



# Part 2
cards = np.ones(len(ns)) # for each row (meaning one card), it makes a new array with value one (1.)
# print("cards", cards)
# [1. 1. 1. 1. 1. 1.]

for i in range(len(ns)):
#     print("i = ", i)
#     print("cards = ", cards)
#     print("winning_nr = ", winning_nr)

#     print("winning_nr[",i,"] =", winning_nr[i])
#     print("cards[",i,"] =", cards[i])

#     print("before -> cards[",i," + 1 : ",i," + winning_nr[",i,"] + 1] = ", cards[i + 1 : i + winning_nr[i] + 1] )
    
    # we want to extract just one single element between that possitions, and then to modify correctly the array cards
    # for example, when we have 2 winning numbers, it will count correctly the possitions and extract two elements: [1. 1.]
    # and we add +1 in the formula because we have to look up always for the next element
    # after that, it will add the previous element (cards[i]) in the cards array

    # for example i = 2, and winning_nr =  [1, 1, 2, 0, 0, 0]
    # then we have cards = [1. 2. 3. 1. 1. 1.], (calculated and updated at steps i=0 and i=1)
    # winning_nr[2] = 2, cards[2] = 3.0, 
    # before -> cards[ 2  + 1 :  2  + winning_nr[ 2 ] + 1] =  [1. 1.]
    # after -> cards[i + 1 : i + winning_nr[i] + 1] =  [4. 4.]
    
    cards[i + 1 : i + winning_nr[i] + 1] += cards[i]
    
    # print("after -> cards[i + 1 : i + winning_nr[i] + 1] = ", cards[i + 1 : i + winning_nr[i] + 1] )
    # print("\n")

# print("cards", cards) # the final array
# [1. 2. 3. 4. 4. 1.]

scratchcards  = cards.sum() # sum up all the elements for the result
print("scratchcards", scratchcards ) 
# 15.0