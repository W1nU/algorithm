import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
times = [0] * N
results = [-1] * N
G = {n: [] for n in range(N)}
RG = {n: [] for n in range(N)}
degree_matrix = [0] * N

for n in range(N):
    intp = list(map(int, input().split()))

    times[n] = intp[0]

    for to in intp[1:len(intp) - 1]:
        degree_matrix[n] += 1
        G[n].append(to - 1)
        RG[to - 1].append(n)

queue = deque([])

for index in range(N):
    if degree_matrix[index] == 0:
        # 차수가 0인 건물, 지금까지의 시간
        queue.append((index, times[index]))
        results[index] = max(results[index], times[index])
        degree_matrix[index] = -1

while queue:
    building, time = queue.popleft()
    next_buildings = RG[building]

    for building in next_buildings:
        degree_matrix[building] -= 1

    for index in range(N):
        if degree_matrix[index] == 0:
            max_time = time
            prev_nodes = G[index]

            for node in prev_nodes:
                if max_time < results[node]:
                    max_time = results[node]
            
            new_time = max_time + times[index]
            queue.append((index, new_time))
            results[index] = max(results[index], new_time)
            degree_matrix[index] -= 1

for time in results:
    print(time)
