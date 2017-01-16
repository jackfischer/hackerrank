import heapq

N, K = map(lambda x: int(x), input().split())
cookies = [int(x) for x in input().split()]
heapq.heapify(cookies)

operations = 0
while len(cookies) >= 2 and cookies[0] < K:
    special = heapq.heappop(cookies)
    special += heapq.heappop(cookies) * 2
    heapq.heappush(cookies, special)
    operations += 1
    
if cookies[0] >= K:
    print(operations)
else:
    print(-1)
    