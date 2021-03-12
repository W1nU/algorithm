import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

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
sets = [n for n in range(N + 1)]
for _ in range(M):
    op, a, b = map(int, input().split())

    if op == 0:
        union(a, b)
    
    else:
        root_a = find(a)
        root_b = find(b)

        if root_a != root_b:
            print("NO")
        else:
            print("YES")