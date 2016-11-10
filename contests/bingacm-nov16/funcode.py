
def funcode(line: list) -> list:
    z = zip(line, range(len(line)))
    li = sorted(list(z))
    result = []
    for val, i in li:
        total = 0
        for j in range(i):
            if line[j] > val:
                total += 1
        result.append(total)
    return result




Q = int(input())

for q in range(Q):
    line = [int(i) for i in input().split()]
    line = line[1:]
    result = funcode(line)
    result = [str(i) for i in result]
    print(' '.join(result))
    