import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
nodes = { n: [] for n in range(1, N + 1)}
parents = [0 for _ in range(N + 1)]

for _ in range(N - 1):
    n1, n2 = map(int, input().split())
    nodes[n1].append(n2)
    nodes[n2].append(n1)

parent = 1
queue = deque([[parent, nodes[parent]]])

while queue:
    parent, next_nodes = queue.popleft()

    for node in next_nodes:
        if parents[node] == 0:
            parents[node] = parent
            queue.append([node, nodes[node]])
    

for parent in parents[2:]:
    print(parent)