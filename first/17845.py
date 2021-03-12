import sys
input = sys.stdin.readline

N, K = map(int, input().split())
lecture = [list(map(int, input().split())) for _ in range(K)]

dp = [[0] * (N + 1) for _ in range(K + 1)]

for n in range(1, K + 1):
    score, time = lecture[n - 1]

    for limit_time in range(1, N + 1):
        if time <= limit_time:
            dp[n][limit_time] = max(dp[n - 1][limit_time], dp[n - 1][limit_time - time] + score)
        else:
            dp[n][limit_time] = dp[n - 1][limit_time]

print(dp[-1][-1])

