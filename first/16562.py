import sys
input = sys.stdin.readline
import heapq
sys.setrecursionlimit(10000)

def union(a, b):
    root_a = find(a)
    root_b = find(b)

    if root_a != root_b:
        sets[root_a] = root_b

def find(a):
    parent = sets[a]

    if parent == a:
        return a
    
    else:
        root = find(parent)
        sets[a] = root
        return root

def is_one():
    root_count = 0

    for n in range(N + 1):
        if sets[n] == n:
            root_count += 1
    
    return True if root_count == 1 else False

N, M, K = map(int, input().split())
costs = list(map(int, input().split()))
# 0번은 나 자신
sets = [n for n in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    union(a, b)

queue = []

for n in range(N):
    heapq.heappush(queue, (costs[n], n + 1))

used_cost = 0
available = True

while not is_one():
    cost, student = heapq.heappop(queue)

    root_me = find(0)
    root_stud = find(student)

    if root_stud != root_me:
        used_cost += cost
        
        if used_cost > K:
            available = False
            break

        else:
            union(0, student)
    
print(used_cost if available else "Oh no")