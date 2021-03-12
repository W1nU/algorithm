import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
# 선행 작업에 대한 정보
G = {n: [] for n in range(1, N + 1)}
# 후행 작업에 대한 정보
RG = {n: [] for n in range(1, N + 1)}
times = [0]
degree_matrix = [0] * (N + 1)
costs = [0] * (N + 1)
answer = 0

for n in range(1, N + 1):
    inp = list(map(int, input().split()))
    times.append(inp[0])

    for task in inp[2:]:
        G[n].append(task)
        RG[task].append(n)
        degree_matrix[n] += 1

# 인덱스, 이전까지 걸린 시간
queue = deque()

for index in range(1, N + 1):
    if degree_matrix[index] == 0:
        queue.append((index, times[index]))
        costs[index] = times[index]
        degree_matrix[index] = -1

while queue:
    task, cost = queue.popleft()
    next_node = RG[task]

    for node in next_node:
        degree_matrix[node] -= 1

    prev_node = G[task]
    max_cost = cost

    for node in prev_node:
        max_cost = max(max_cost, costs[node] + times[task])
    
    costs[task] = max_cost
    answer = max(answer, max_cost)

    for index in range(task, N + 1):
        if degree_matrix[index] == 0:
            queue.append((index, max_cost))
            degree_matrix[index] = -1

print(answer)