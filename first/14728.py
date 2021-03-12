N, T = map(int, input().split())
dp = [0] * (T + 1)

for count in range(N):
    time, score = map(int, input().split())

    for time_limit in range(T, 0, -1):
        if time <= time_limit:
            if count != 0:
                if time_limit - time >= 0:
                    dp[time_limit] = max(dp[time_limit - time] + score, dp[time_limit])
                else:
                    dp[time_limit] = score

            else:
                dp[time_limit] = score

print(dp[-1])