import sys
input = sys.stdin.readline
import heapq
import math 

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

def is_one_root():
    count = 0

    for n in range(N):
        if n == sets[n]:
            count += 1

    return True if count == 1 else False

N = int(input())
star = [list(map(float, input().split())) for _ in range(N)]
sets = [n for n in range(N)]
queue = []
ret = 0

for i in range(N):
    x, y = star[i]

    for j in range(i + 1, N):
        n_x, n_y = star[j]
        distance = math.sqrt((x - n_x) ** 2 + (y - n_y) ** 2)

        heapq.heappush(queue, (distance, i, j))

while not is_one_root():
    d, a, b = heapq.heappop(queue)

    root_a = find(a)
    root_b = find(b)

    if root_a != root_b:
        ret += d
        union(a, b)

print(round(ret, 2))