#!/bin/python3

import sys

n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
x = [int(x_temp) for x_temp in input().strip().split(' ')]


def search_for_house(index: int) -> int:
    """
    Find furthest possible house from index from which index is reachable
    """
    most_recent_good = index
    for i in range(index, len(x)):
        delta = x[i] - x[index]
        if delta <= k:
            most_recent_good = i
        else:
            return most_recent_good

    return most_recent_good


#Initialization
x.sort()
radio_indexes = [search_for_house(0)]
index = radio_indexes[0]

while index < len(x):
    delta = x[index] - x[radio_indexes[-1]]
    if delta > k: #house not reached by current radio
        index = search_for_house(index)
        radio_indexes.append(index)
    else:
        index += 1 #check next house


print(len(radio_indexes))
