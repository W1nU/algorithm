import sys
input = sys.stdin.readline
import heapq

def dijkstra(start):
    distance = [float('inf') for _ in range(N + 1)]
    distance[start] = 0
    heap = []
    heapq.heappush(heap, (0, start))

    while heap:
        current_weight, current_node = heapq.heappop(heap)

        if current_weight > distance[current_node]:
            continue
        
        else:
            current_roads = roads[current_node]
        
            for road in current_roads:
                new_weight = current_weight + road[0]

                if distance[road[1]] > new_weight:
                    distance[road[1]] = new_weight
                    heapq.heappush(heap, (new_weight, road[1]))

    return distance

N, M, X = map(int, input().split())
roads = {n : [] for n in range(1, N + 1)}
max_time = 0

for _ in range(M):
    start, end, weight = map(int, input().split())
    roads[start].append((weight, end))

return_time = dijkstra(X)

for stud in range(1, N + 1):
    go_time = dijkstra(stud)

    time = go_time[X] + return_time[stud]

    if time > max_time:
        max_time = time

print(max_time)