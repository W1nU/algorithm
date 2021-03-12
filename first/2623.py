import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
degree_matrix = [0] * (N + 1)
G = {n: [] for n in range(N + 1)}

for _ in range(M):
    seq = list(map(int, input().split()))

    if seq[0] != 0:
        i = seq[1]
        for j in seq[2:]:
            degree_matrix[j] += 1
            G[i].append(j)
            i = j

queue = deque()
ret = []

for i in range(1, N + 1):
    if degree_matrix[i] == 0:
        queue.append(i)
        degree_matrix[i] = -1

while queue:
    singer = queue.popleft()
    next_singer = G[singer]

    for i in next_singer:
        degree_matrix[i] -= 1
    
    ret.append(singer)
    
    for i in range(1, N + 1):
        if degree_matrix[i] == 0:
            queue.append(i)
            degree_matrix[i] = -1

if len(ret) == N:
    for singer in ret:
        print(singer)

else:
    print(0)