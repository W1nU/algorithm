import sys
import heapq
input = sys.stdin.readline

def dijkstra(graph, start):
    # start로 부터의 거리 값을 저장하기 위함.
    distances = { node: float('inf') for node in graph } 

    # 시작 노드의 거리는 항상 0.
    distances[start] = 0

    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue:
        # 탐색할 노드와 해당 노드까지의 거리
        current_distance, current_destination = heapq.heappop(queue)

        # 기존 거리보다 길면 무시
        if distances[current_destination] < current_distance:
            continue

        for next_destination, next_distance in graph[current_destination]:
            distance = current_distance + next_distance

            if distance < distances[next_destination]:
                distances[next_destination] = distance
                heapq.heappush(queue, [distance, next_destination])
    
    return distances

N = int(input())
M = int(input())
bus = { town: [] for town in range(1, N + 1)}

for _ in range(M):
    start, end, value = map(int, input().split())
    bus[start].append((end, value))

start, end = map(int, input().split())
print(dijkstra(bus, start)[end])