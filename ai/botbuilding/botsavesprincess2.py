
def nextMove(n,r,c,grid):
    for i in range(n): #Find row
        if "p" in grid[i]:
            if r > i:
                return "UP"
            if r < i:
                return "DOWN"

            #Find column if necessary
            j = grid[i].index("p")
            if c > j:
                return "LEFT"
            if c < j:
                return "RIGHT"

n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = [input() for _ in range(0,n)]
print(nextMove(n,r,c,grid))

