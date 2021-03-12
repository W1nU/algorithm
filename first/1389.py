import sys
input = sys.stdin.readline

N, M = list(map(int, input().split()))
friends = [list(map(int, input().split())) for _ in range(M)]

distance_matrix = [[float("inf")] * N for _ in range(N)]

for y in range(N):
    for x in range(N):
        if y == x:
            distance_matrix[y][x] = 0

# distance_matrix[1][1] = 1
for friend in friends:
    distance_matrix[friend[0] - 1][friend[1] - 1] = 1
    distance_matrix[friend[1] - 1][friend[0] - 1] = 1

# 거쳐가는 점
for i in range(N):
    # 출발점
    for j in range(N):
        # 도착점
        for k in range(N):
            distance_matrix[j][k] = min(distance_matrix[j][k], distance_matrix[j][i] + distance_matrix[i][k])

min_distance = [1, sum(distance_matrix[0])]

for n, distance in enumerate(distance_matrix):
    temp_distance = sum(distance)

    if temp_distance < min_distance[1]:
        min_distance = [n + 1, temp_distance]

print(min_distance[0])