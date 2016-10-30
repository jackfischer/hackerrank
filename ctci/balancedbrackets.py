def is_matched(expression):
    left = list()
    for i in expression:
        if i in brackets:
            left.append(i)
        else:
            if not left or brackets[left[-1]] != i:
                return False
            left.pop()
            
    if left:
        return False
    return True


t = int(input().strip())
brackets = {'{': '}', '[': ']', '(':')'}
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression) == True:
        print("YES")
    else:
        print("NO")
