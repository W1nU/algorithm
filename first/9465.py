from collections import deque
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    points = [list(map(int, input().split())) for _ in range(2)]

    dp = [[0] * N for _ in range(2)]
    dp[0][0] = points[0][0]
    dp[1][0] = points[1][0]
    dp[0][1] = dp[1][0] + points[0][1]
    dp[1][1] = dp[0][0] + points[1][1]

    for n in range(2, N):
        dp[0][n] = max(dp[1][n - 2], dp[1][n - 1]) + points[0][n]
        dp[1][n] = max(dp[0][n - 2], dp[0][n - 1]) + points[1][n]
    
    print(max(dp[0][-1], dp[1][-1]))
