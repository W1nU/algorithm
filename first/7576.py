from collections import deque 

MOVES = [
    [1,0],
    [0,1],
    [-1,0],
    [0, -1]
]

M, N = list(map(int, input().split()))
box = [list(input().split()) for _ in range(N)]
day_count = 0

current_node = []
queue = deque([])

for y in range(N):
    for x in range(M):
        if box[y][x] == "1":
            current_node.append([x,y])


while current_node:
    next_node = []
    
    queue.extend(current_node)

    while queue:
        temp_node = queue.popleft()

        for move in MOVES:
            moved_node = [temp_node[0] + move[0], temp_node[1] + move[1]]

            if 0 <= moved_node[0] < M and 0 <= moved_node[1] < N:
                if box[moved_node[1]][moved_node[0]] == "0":
                    box[moved_node[1]][moved_node[0]] = "1"
                    next_node.append(moved_node)
    
    current_node = next_node
    day_count += 1

is_all_changed = True

for y in range(N):
    for x in range(M):
        if box[y][x] == "0":
            is_all_changed = False

if is_all_changed:
    print(day_count - 1)
else:
    print(-1)