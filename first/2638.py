import sys
input = sys.stdin.readline

sides = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def check_closed_air():
    stack = [(0,0)]

    while stack:
        row, col = stack.pop()
        temp_cheese[row][col] = "air"

        for side in sides:
            next_row, next_col = row + side[0], col + side[1]
            
            if 0 <= next_row < N and 0 <= next_col < M and temp_cheese[next_row][next_col] == "0":
                stack.append((next_row, next_col))
    
def is_melt(row, col):
    count = 0

    for side in sides:
        new_row = row + side[0]
        new_col = col + side[1]

        if 0 <= new_row < N and 0 <= new_col < M and temp_cheese[new_row][new_col] == "air":
            count += 1
    
    if count >= 2:
        return True

    return False

N, M = map(int, input().split())
cheese = [input().split() for _ in range(N)]
time_count = 0

while True:
    is_clear = True
    will_melt = []
    temp_cheese = []

    for row in cheese:
        temp_cheese.append(row[:])

    check_closed_air()

    for row in range(N):
        for col in range(M):
            if cheese[row][col] == "1":
                is_clear = False
                if is_melt(row, col):
                    will_melt.append((row, col))

    for melt_row, melt_col in will_melt:
        cheese[melt_row][melt_col] = "0"

    if is_clear:
        print(time_count)
        break 
    else:
        time_count += 1

# 8 9 
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 1 1 0 0 0 1 1 0
# 0 1 0 1 1 1 0 1 0
# 0 1 0 0 1 0 0 1 0
# 0 1 0 1 1 1 0 1 0
# 0 1 1 0 0 0 1 1 0
# 0 0 0 0 0 0 0 0 0
