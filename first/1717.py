import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)

def union(v1, v2):
    v1 = find(v1)
    v2 = find(v2)

    if v1 == v2:
        return
    else:
        array[v2] = v1
        
def find(value):
    if value == array[value]:
        return value
    else:
        root = find(array[value])
        array[value] = root
        return root
    

N, M = list(map(int, input().split()))
array = [n for n in range(N + 1)]

# expressions = [list(map(int, input().split())) for _ in range(M)]

for i in range(M):
    op, v1, v2 = list(map(int, input().split()))
    
    if op == 0:
        union(v1, v2)
        
    if op == 1:
        if find(v1) == find(v2):
            print("YES")
        else:
            print("NO")
    