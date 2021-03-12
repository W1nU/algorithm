import heapq
import sys

input = sys.stdin.readline
INF = sys.maxsize

V, E = map(int, input().split())
start = int(input()) - 1
edges = { n: [] for n in range(V) }
visited = []

min_distance = [INF] * V
min_distance[start] = 0

for _ in range(E):
    s, e, w = map(int, input().split())
    edges[s - 1].append([w, e - 1])

# 힙에는 아직 방문하지 않은 노드가 도착지인 간선들만 들어가야 한다.
heap = [(min_distance[start], start)]

while heap:
    weight, end = heapq.heappop(heap)
    visited.append(end)

    for n_w, n_e in edges[end]:
        n_c = weight + n_w

        if n_c < min_distance[n_e]:
            min_distance[n_e] = n_c
            heapq.heappush(heap, (n_c, n_e))
      

for d in min_distance:
    print(d if d != INF else "INF")