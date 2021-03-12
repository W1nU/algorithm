from collections import deque

def find_maze_min(maze):
    current_node = deque([[0,0]])
    next_node = deque([])
    count = 0

    while len(current_node) != 0:
        current_location = current_node.popleft()

        for move in MOVE:
            next_location = [current_location[0] + move[0], current_location[1] + move[1]]

            if next_location[0] == N - 1 and next_location[1] == M - 1:
                return count + 2

            if 0 <= next_location[0] < N and 0 <= next_location[1] < M:
                if maze[next_location[0]][next_location[1]] == "1" and visit[next_location[0]][next_location[1]] == False:
                    visit[next_location[0]][next_location[1]] = True
                    next_node.append(next_location)

        if len(current_node) == 0 and len(next_node) > 0:
            current_node = next_node
            next_node = deque([])
            count += 1 

MOVE = [[1,0],[-1,0],[0, -1],[0, 1]]
N, M = list(map(int, input().split()))
maze = [input() for _ in range(N)]
visit = [[False] * M for _ in range(N)]

print(find_maze_min(maze))
