N = int(input())
room = [input().split() for _ in range(N)]

# 가로인 상태로 도달할 수 있는 경우의 수, 세로의 상태로 도달할 수 있는 경우의 수, 대각선인 상태로 도달할 수 있는 경우의 수
dp = [[[0,0,0] for _ in range(N)] for _ in range(N)]
dp[0][1] = [1,0,0]

for row in range(N):
    for col in range(2,N):
        if room[row][col] != "1":
            dp[row][col][0] = dp[row][col - 1][0] + dp[row][col - 1][2]
            dp[row][col][1] = dp[row - 1][col][1] + dp[row - 1][col][2]

            if room[row][col - 1] != "1" and room[row - 1][col] != "1":
                dp[row][col][2] += dp[row - 1][col - 1][0] + dp[row - 1][col - 1][1] + dp[row - 1][col - 1][2] 

print(sum(dp[-1][-1]))