import heapq 
import sys
input = sys.stdin.readline

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

    for index in range(1, N + 1):
        if sets[index] == index:
            count += 1

    return True if count == 1 else False

N = int(input())
M = int(input()) 
PQ = []
sets = [n for n in range(N + 1)]
ret = 0

for _ in range(M):
    a, b, cost = map(int, input().split())

    if a != b:
        heapq.heappush(PQ, (cost, a, b))    

while not is_one_root():
    cost, a, b = heapq.heappop(PQ)

    root_a = find(a)
    root_b = find(b)

    if root_a != root_b:
        union(a, b)
        ret += cost
    
print(ret)