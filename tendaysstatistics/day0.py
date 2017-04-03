
n = int(input())
data = [int(x) for x in input().strip().split()]

mean = sum(data) / len(data)
data.sort()
if len(data) % 2 == 0:
    floor = len(data) // 2
    median = data[floor] + data[floor - 1]
    median /= 2
else:
    median = data[len(data) // 2]


mode = None
bestcount = 0
current = None
currentcount = 0
for i in data:
    if i == current:
        currentcount += 1
    else:
        current = i
        currentcount = 1
        
    if currentcount > bestcount:
        bestcount = currentcount
        mode = current

print("%.1f" % mean)
print("%.1f" % median)
print(mode)
