t = int(input())

for _ in range(t):
    n, m, s = tuple([int(i) for i in input().split()])

    s -= 1
    prisoner = (m +s) % n
    if prisoner == 0:
        prisoner = n
    print (prisoner)

