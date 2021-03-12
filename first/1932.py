import sys
input = sys.stdin.readline

N = int(input())
tri = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]

dp[0][0] = tri[0][0]
# 선택할 수 있는 것, 아래 층의 n과 n+1 

for floor in range(1, N):
    row = tri[floor]

    for col in range(len(row)):
        if col == 0:
            dp[floor][col] = dp[floor - 1][col] + row[col]

        elif col == len(row) - 1:
            dp[floor][col] = dp[floor - 1][col - 1] + row[col]
        
        else:
            dp[floor][col] = max(dp[floor - 1][col], dp[floor - 1][col - 1]) + row[col]

print(max(dp[-1]))