import sys
input = sys.stdin.readline
from collections import deque

def BFS(start):
    visited = [False] * (N + 1)
    max_node = start
    max_weight = 0

    queue = deque([(start, 0)])
    visited[start] = True

    while queue:
        current_node, current_weight = queue.popleft()
        next_node = edges[current_node].items()

        for node, weight in next_node:
            new_weight = weight + current_weight

            if not visited[node]:
                if new_weight > max_weight:
                    max_weight = new_weight
                    max_node = node
                
                queue.append((node, new_weight))
                visited[node] = True

    return max_node, max_weight

N = int(input())
edges = {n: {} for n in range(1, N + 1)}

for _ in range(N - 1):
    start, end, weight = map(int, input().split())
    edges[start][end] = weight
    edges[end][start] = weight

node, weight = BFS(1)
max_node, max_weight = BFS(node)
print(max_weight)