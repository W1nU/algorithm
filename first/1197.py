import sys
input = sys.stdin.readline
from collections import deque

def union(v1, v2):
    v1 = find(v1)
    v2 = find(v2)

    if v1 == v2:
        return
    else:
        sets[v2] = v1
        
def find(value):
    if value == sets[value]:
        return value
    else:
        root = find(sets[value])
        sets[value] = root
        return root

V, E = map(int, input().split())
sets = [n for n in range(V + 1)]
G = []

for _ in range(E):
    start, end, cost = map(int, input().split())
    G.append((cost, start, end))

G.sort()
queue = deque(G)
total_cost = 0

while queue:
    cost, start, end = queue.popleft()
    
    s_root = find(start)
    e_root = find(end)

    if e_root == s_root:
        continue

    else:
        union(start, end)
        total_cost += cost

print(total_cost)
