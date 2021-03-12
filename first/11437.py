import sys
input = sys.stdin.readline

N = int(input())
G = {n: [] for n in range(1, N + 1)}

for _ in range(N - 1):
    v1, v2 = map(int, input().split())
    G[v1].append(v2)
    G[v2].append(v1)

M = int(input())
Q = []

for _ in range(M):
    v1, v2 = map(int, input().split())
    Q.append((v1, v2))

# 부모, 깊이
table = [[None, None] for _ in range(N + 1)]
table[1] = [None, 1]
stack = [(1, 1)]

while stack:
    parent, depth = stack.pop()
    next_nodes = G[parent]

    for next_node in next_nodes:
        if table[next_node][1] == None:
            table[next_node] = [parent, depth + 1]
            stack.append((next_node, depth + 1))

for v1, v2 in Q:
    v1_parent, v1_depth = table[v1]
    v2_parent, v2_depth = table[v2]

    if v1_depth > v2_depth:
        while v1_depth != v2_depth:
            v1 = v1_parent
            v1_parent, v1_depth = table[v1_parent]
        
    elif v1_depth < v2_depth:
        while v1_depth != v2_depth:
            v2 = v2_parent
            v2_parent, v2_depth = table[v2_parent]
    
    while v1 != v2:
        v1 = v1_parent
        v2 = v2_parent
        v1_parent, v1_depth = table[v1_parent]    
        v2_parent, v2_depth = table[v2_parent]
    
    print(v1)
