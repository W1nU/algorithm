import sys
input = sys.stdin.readline

N = int(input())
scores = [int(input()) for _ in range(N)]
dp = [[0, 0] for _ in range(N)]

if N == 1:
    print(scores[0])

else:
    dp[0] = [scores[0], scores[0]]
    dp[1] = [scores[0] + scores[1], scores[1]]

    for n in range(2, N):
        dp[n][0] = dp[n - 1][1] + scores[n]
        dp[n][1] = max(dp[n - 2]) + scores[n]

    print(max(dp[N - 1]))