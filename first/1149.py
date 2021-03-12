import sys
input = sys.stdin.readline

N = int(input())
price = [list(map(int, input().split())) for _ in range(N)]
dp = [[0,0,0] for _ in range(N)]
dp[0] = price[0]

for n in range(1, N):
    temp_cost = [0,0,0]

    temp_cost[0] = min(dp[n - 1][1] + price[n][0], dp[n - 1][2] + price[n][0])
    temp_cost[1] = min(dp[n - 1][0] + price[n][1], dp[n - 1][2] + price[n][1])
    temp_cost[2] = min(dp[n - 1][0] + price[n][2], dp[n - 1][1] + price[n][2])

    dp[n] = temp_cost

print(min(dp[n]))