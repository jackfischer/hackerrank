from collections import Counter

def can_valid(string: str) -> bool:
    #setup
    c1 = Counter(string)
    values = c1.values()
    c2 = Counter(c1.values())
    
    #Two short circuit cases
    if len(c2) <= 1:
        return True
    if len(c2) > 2:
        return False
    else:
        #c2 is len(2), check if values are one-off
        if min(c2.values()) == 1:
            return True
        else:
            return False


string = input().strip()

if can_valid(string):
    print("YES")
else:
    print("NO")

