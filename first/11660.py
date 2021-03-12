N, M = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]
scopes = [list(map(int, input().split())) for _ in range(M)]

added_table = [[0] * N for _ in range(N)]

for row in range(N):
    for col in range(N):
        if row == 0:
            if col == 0:
                added_table[row][col] = table[row][col]
            else:
                added_table[row][col] = added_table[row][col - 1] + table[row][col]
        
        elif col == 0:
            if row == 0:
                added_table[row][col] = table[row][col]
            else:
                added_table[row][col] = added_table[row - 1][col] + table[row][col]

        else:
            added_table[row][col] = (added_table[row - 1][col] + added_table[row][col - 1] - added_table[row - 1][col - 1]) + table[row][col]

for scope in scopes:
    y1, x1, y2, x2  = map(lambda x : x - 1, scope)
    result = -1

    if x1 == 0 and y1 == 0:
        result = added_table[y2][x2]

    elif x1 == 0:
        result = added_table[y2][x2] - added_table[y1 - 1][x2]

    elif y1 == 0:
        result = added_table[y2][x2] - added_table[y2][x1 - 1]

    else:
        result = added_table[y2][x2] - added_table[y2][x1 - 1] - added_table[y1 - 1][x2] + added_table[y1 - 1][x1 - 1]
    
    print(result)