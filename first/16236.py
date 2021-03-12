import sys
from collections import deque
input = sys.stdin.readline

def find_eatable(space, x, y):
    MOVE_X = [0, 0,1,-1]
    MOVE_Y = [1,-1,0,0]

    visited = [[False] * N for _ in range(N)]
    visited[y][x] = True
    current_node = deque([[x, y]])
    eatable_fish = []
    count = 0
    
    while 1: 
        count += 1
        next_node = deque([])

        while current_node:
            current_location = current_node.popleft()
            
            for i in range(4):
                new_x = current_location[0] + MOVE_X[i]
                new_y = current_location[1] + MOVE_Y[i]

                if (0 <= new_x < N and 0 <= new_y < N) and visited[new_y][new_x] == False:
                    if space[new_y][new_x] <= shark_size:
                        visited[new_y][new_x] = True
                        next_node.append([new_x, new_y])
                        
                        if 0 < space[new_y][new_x] < shark_size:
                            eatable_fish.append([new_x, new_y, space[new_y][new_x], count])
        
        if len(next_node) != 0:
            current_node = next_node
        else:
            break

    return eatable_fish

N = int(input())
space = [list(map(int, input().split())) for _ in range(N)]
shark_location = []
shark_size = 2
time = 0
eat_counter = 0

for y in range(N):
    for x in range(N):
        if space[y][x] == 9:
            shark_location = [x, y]

while True:
    eatable_fish = find_eatable(space, shark_location[0], shark_location[1])
    min_length = float("inf")
    close_fish = []

    if len(eatable_fish) == 0:
        break

    for fish in eatable_fish:
        if fish[3] < min_length:
            close_fish = [fish]
            min_length = fish[3]
        
        elif fish[3] == min_length:
            close_fish.append(fish)

    target_fish = close_fish[0]

    for fish in close_fish[1:]:
        if fish[1] < target_fish[1]:
            target_fish = fish
        
        elif fish[1] == target_fish[1]:
            if fish[0] < target_fish[0]:
                target_fish = fish

    time += target_fish[3]
    space[shark_location[1]][shark_location[0]] = 0
    shark_location = [target_fish[0], target_fish[1]]
    eat_counter += 1

 
    if eat_counter == shark_size:
        shark_size += 1
        eat_counter = 0
    
    space[target_fish[1]][target_fish[0]] = 9

print(time)
# 1. 움직일 수 있는 모든 점 파악
# 2. 먹을 수 있는 물고기만 선별
# 3. 규칙에 맞게 처리 