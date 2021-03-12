# 09 32
import sys
input = sys.stdin.readline
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

T = int(input())

for _ in range(T):
    N = int(input())
    sets = [n for n in range(N)]
    bases = [list(map(int, input().split())) for _ in range(N)]
    ret = 0

    for i in range(N):
        x, y, r = bases[i]

        for j in range(i, N):
            x2, y2, r2 = bases[j]

            distance = math.sqrt((x2 - x) ** 2 + (y2 - y) ** 2)

            if distance <= r + r2:
                union(i, j)
    
    for i in range(N):
        if i == sets[i]:
            ret += 1
    
    print(ret)
