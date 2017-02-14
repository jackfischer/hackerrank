#!/bin/python3

from collections import Counter
import sys

def legal(original: list, selected: tuple) -> bool:
    string = [c for c in original if c in selected]
    a = string[0]
    b = string[1]
    #Ensure alternation
    for i in range(2, len(string)):
        if i % 2 == 0:
            if string[i] != a:
                return False
        else:
            if string[i] != b:
                return False
    return True


s_len = int(input().strip())
s = input().strip()
ORIGINAL = list(s)

counter = Counter(s)
most_common = counter.most_common()
#print(most_common)
best_seen = 0
for outer in range(0, len(most_common) - 1):
    for inner in range(outer + 1, len(most_common)):
        potential_value = most_common[outer][1] + most_common[inner][1]
        #print(potential_value)

        if potential_value > best_seen:
            if legal(ORIGINAL, (most_common[outer][0], most_common[inner][0])):
                #print("updated to " + most_common[outer][0] + " " + most_common[inner][0])
                best_seen = potential_value
                
                
print(best_seen)
