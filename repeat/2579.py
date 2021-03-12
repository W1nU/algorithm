import sys
input = sys.stdin.readline

N = int(input())
# 이전 계단을 밟은 경우, 이전 계단을 밟지 않은 경우
stairs = [int(input()) for _ in range(N)]

if N == 1:
    print(stairs[0])
    
else:
    dp = [[0,0] for _ in range(N)]

    dp[0][0] = stairs[0]
    dp[0][1] = stairs[0]
    dp[1][0] = stairs[1] + stairs[0]
    dp[1][1] = stairs[1]

    for step in range(2, N):
        dp[step][0] = dp[step - 1][1] + stairs[step]
        dp[step][1] = max(dp[step - 2]) + stairs[step]

    print(max(dp[-1]))