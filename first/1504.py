import sys
input = sys.stdin.readline
import heapq

def find_min(s):
    distances = { n: float("inf") for n in range(1, N + 1) }
    distances[s] = 0

    queue = []
    heapq.heappush(queue, (distances[s], s))

    while queue:
        c_d, c_n = heapq.heappop(queue)

        if c_d > distances[c_n]:
            continue
        
        for n_n, n_d in G[c_n]:
            distance = c_d + n_d

            if distance < distances[n_n]:
                distances[n_n] = distance
                heapq.heappush(queue, (distance, n_n))
    
    return distances

N, E = map(int, input().split())
G = { n: [] for n in range(1, N + 1)}

for _ in range(E):
    s, e, w = map(int, input().split())
    G[s].append((e, w))
    G[e].append((s, w))

n1, n2 = map(int, input().split())

from_1 = find_min(1)
from_n1 = find_min(n1)
from_n2 = find_min(n2)

w_1 = from_1[n1] + from_n1[n2] + from_n2[N]
w_2 = from_1[n2] + from_n2[n1] + from_n1[N]
answer = min(w_1, w_2) 

print(answer if answer != float('inf') else -1)