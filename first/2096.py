from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

for row in range(N):
    table_row = list(map(int, input().split()))

    if row == 0:
        dp_min = table_row
        dp_max = table_row

    else:
        temp_min = [0,0,0]
        temp_max = [0,0,0]

        for col in range(3):
            if col == 0:
                temp_max[0] = max(dp_max[0], dp_max[1]) + table_row[col]
                temp_min[0] = min(dp_min[0], dp_min[1]) + table_row[col]

            elif col == 1:
                temp_max[1] = max(dp_max[0], dp_max[1], dp_max[2]) + table_row[col]
                temp_min[1] = min(dp_min[0], dp_min[1], dp_min[2]) + table_row[col]

            else:
                temp_max[2] = max(dp_max[1], dp_max[2]) + table_row[col]
                temp_min[2] = min(dp_min[1], dp_min[2]) + table_row[col]

        dp_min = temp_min
        dp_max = temp_max

print(max(dp_max), min(dp_min)) 