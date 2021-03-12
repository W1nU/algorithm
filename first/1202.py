import sys
input = sys.stdin.readline
import heapq
from collections import deque

N, K = map(int, input().split())
stones = [list(map(int, input().split())) for _ in range(N)]
bags = [int(input()) for _ in range(K)]
stones.sort()
bags.sort()

stones = deque(stones)
selected = []
ret = 0

for i in range(K):
    limit = bags[i]

    while stones:
        weight, value = stones.popleft()

        if weight <= limit:
            heapq.heappush(selected, (-value, weight))
        
        else:
            stones.appendleft((weight, value))
            break

    if selected:
        ret += heapq.heappop(selected)[0] * -1

print(ret)