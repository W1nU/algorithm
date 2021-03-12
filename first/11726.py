import sys
input = sys.stdin.readline

dp = {}
dp[1] = 1
dp[2] = 2

for n in range(3, 1001):
    dp[n] = dp[n - 1] + dp[n - 2]

n = int(input())
print(dp[n] % 10007)