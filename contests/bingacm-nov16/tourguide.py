
line = [int(i) for i in input().split()]

"""
paths = dict()
for a, b in zip(range(1,len(line)+1), line):
    paths[a] = b
"""
paths = line

current = 1
path = list()
touched = set()
while current not in touched and len(path) != len(paths):
    touched.add(current)
    path.append(current)
    current = paths[current-1]
    
    
if len(path) == len(paths):
    path = [str(i) for i in path]
    print(" ".join(path))
else:
    print("NO")