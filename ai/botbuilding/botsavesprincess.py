
def displayPathtoPrincess(n: int, grid: list):
    p = None
    m = None
    
    #Discover p and m in matrix
    for i in range(n):
        if M in grid[i]:
            m = (i, grid[i].index(M))
        if P in grid[i]:
            p = (i, grid[i].index(P))
        if p and m:
            break
    
    #Travel in vertical direction
    vertical = m[0] - p[0]
    command = "UP" if vertical > 0 else "DOWN"
    for i in range(abs(vertical)):
        print(command)

    #Travel in horizontal direction
    horizontal = m[1] - p[1]
    command = "LEFT" if horizontal > 0 else "RIGHT"
    for j in range(abs(horizontal)):
        print(command)

        
M = "m"
P = "p"
N = int(input())
grid = [input().strip() for _ in range(0, N)]
displayPathtoPrincess(N,grid)

