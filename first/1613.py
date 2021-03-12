import sys
input = sys.stdin.readline

N, K = map(int, input().split())
distance = [[float('inf')] * (N + 1) for _ in range(N +1)]
distance_reverse = [[float('inf')] * (N + 1) for _ in range(N +1)]

for i in range(1, N + 1):
    distance[i][i] = 0
    distance_reverse[i][i] = 0

for _ in range(K):
    front, back = map(int,  input().split())
    distance[front][back] = 1
    distance_reverse[back][front] = -1

S = int(input())
Q = [list(map(int, input().split())) for _ in range(S)]

for stop_over in range(1, N + 1):
    for start in range(1, N + 1):
        for end in range(1, N + 1):
            distance[start][end] = min(distance[start][end], distance[start][stop_over] + distance[stop_over][end])
            distance_reverse[start][end] = min(distance_reverse[start][end], distance_reverse[start][stop_over] + distance_reverse[stop_over][end])

print(distance)

for query in Q:
    front, end = query

    d = distance[front][end]
    d_r = distance_reverse[front][end]

    if d == float('inf') and d_r == float('inf'):
        print(0)

    elif d == float('inf') and d_r < 0:
        print(1)
        
    else:
        print(-1)

