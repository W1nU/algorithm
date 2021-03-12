import sys
input = sys.stdin.readline
import heapq

def find(a):
    parent = sets[a]

    if parent == a:
        return parent
    
    else:
        root = find(parent)
        sets[parent] = root
        return root

def union(a, b):
    root_a = find(a)
    root_b = find(b)

    if root_a != root_b:
        sets[root_a] = root_b

def is_mst():
    count = 0

    for n in range(N + 1):
        if n == sets[n]:
            count += 1

    return True if count == 1 else False

heap = []
N = int(input())

for v in range(1, N + 1):
    cost = int(input())
    heapq.heappush(heap, (cost, 0, v))

for v in range(1, N + 1):
    costs = list(map(int, input().split()))

    for v2, cost in enumerate(costs):
        if cost != 0:
            heapq.heappush(heap, (cost, v, v2 + 1))

sets = [n for n in range(N + 1)]
ret = 0

while not is_mst():
    cost, v1, v2 = heapq.heappop(heap)

    root_v1 = find(v1)
    root_v2 = find(v2)

    if root_v1 != root_v2:
        ret += cost
        union(root_v1, root_v2)

print(ret)





