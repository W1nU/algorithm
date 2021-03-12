import sys
input = sys.stdin.readline
from collections import deque

MOVE = [[1,0], [-1,0], [0, 1], [0, -1]]

N, M = map(int, input().split())
maze = [input().rstrip() for _ in range(N)]

# 부수지 않고 방문, 부수고 방문
visited = [[[False, False] for _ in range(M)] for _ in range(N)]
# X, Y, count, 부순 벽의 수
queue = deque([(0, 0, 1, 0)])
visited[0][0][0] = True
answer = float('inf')

if N == 1 and M == 1:
    answer = 1

else:
    while queue:
        X, Y, count, wall = queue.popleft()

        for move_x, move_y in MOVE:
            new_x = X + move_x
            new_y = Y + move_y

            if 0 <= new_x < M and 0 <= new_y < N:
                if new_x == M - 1 and new_y == N - 1 and count + 1 < answer:
                    answer = count + 1

                if wall == 0:
                    if maze[new_y][new_x] == "1" and not visited[new_y][new_x][1]:
                        queue.append((new_x, new_y, count + 1, wall + 1))
                        visited[new_y][new_x][1] = True

                    elif maze[new_y][new_x] == "0" and not visited[new_y][new_x][0]:
                        queue.append((new_x, new_y, count + 1, wall))
                        visited[new_y][new_x][0] = True

                else:
                    if maze[new_y][new_x] == "0" and not visited[new_y][new_x][1]:
                        queue.append((new_x, new_y, count + 1, wall))
                        visited[new_y][new_x][1] = True
                
print(answer if answer != float("inf") else -1)
