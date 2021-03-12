import sys
input = sys.stdin.readline

N = int(input())
wines = [int(input()) for _ in range(N)]
dp = [0] * N

if N == 1:
    print(wines[0])
elif N == 2:
    print(wines[0] + wines[1])
else:
    dp[0] = wines[0]
    dp[1] = wines[0] + wines[1]

    for i in range(2, N):
        glass = wines[i]

        dp[i] = max(dp[i - 2] + glass, dp[i - 3] + wines[i - 1] + glass, dp[i - 1])

    print(dp[-1])