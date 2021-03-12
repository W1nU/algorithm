import sys
input = sys.stdin.readline
import heapq

def dijkstra(start):
    distance = [float('inf') for _ in range(N + 1)]
    distance[start] = 0
    queue = []
    heapq.heappush(queue, (distance[start], start))

    while queue:
        current_weight, current_dest = heapq.heappop(queue)

        if current_weight > distance[current_dest]:
            continue

        current_roads = roads[current_dest]
        
        for road_weight, road_dest in current_roads:
            new_weight = current_weight + road_weight

            if distance[road_dest] > new_weight:
                distance[road_dest] = new_weight
                heapq.heappush(queue, (new_weight, road_dest))
        
    return distance

N, M, R = map(int, input().split())
items = list(map(int, input().split()))
roads = {n: [] for n in range(1, N + 1)}

for _ in range(R):
    start, end, weight = map(int, input().split())
    roads[start].append((weight, end))
    roads[end].append((weight, start))

max_item = 0

for point in range(1, N + 1):
    lengths = dijkstra(point)
    item_count = 0

    for node in range(1, N + 1):
        if lengths[node] <= M:
            item_count += items[node - 1]
    
    if max_item < item_count:
        max_item = item_count

print(max_item)