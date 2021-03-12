import sys
input = sys.stdin.readline
import heapq

N = int(input())
meetings = []
queue = []

for _ in range(N):
    start, end = map(int, input().split())
    heapq.heappush(queue, (end, start))

selected = []

while queue:
    end, start = heapq.heappop(queue)

    if not selected:
        selected.append((start, end))
    
    else:
        prev_end = selected[-1][1]
        
        if start >= prev_end:
            selected.append((start, end))

print(len(selected))