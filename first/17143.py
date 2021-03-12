import sys
input = sys.stdin.readline
import heapq

def union(a, b):
    root_a = find(a)
    root_b = find(b)

    if root_a != root_b:
        sets[root_a] = root_b

def find(a):
    parent = sets[a]

    if parent == a:
        return parent
    else:
        root = find(parent)
        sets[parent] = root
        return root

N, M = map(int, input().split())
sets = [a for a in range(N)]
queue = []
selected_road = []
answer = 0

for _ in range(M):
    prev, dest, cost = map(int, input().split())
    heapq.heappush(queue, (cost, prev, dest))

while queue:
    cost, prev, dest = heapq.heappop(queue)
    prev, dest = prev - 1, dest - 1

    root_prev = find(prev)
    root_dest = find(dest)

    if root_prev != root_dest:
        union(root_prev, root_dest)
        answer += cost
        selected_road.append((cost, prev, dest))

print(answer - selected_road[-1][0])