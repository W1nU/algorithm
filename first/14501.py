import sys
input = sys.stdin.readline

N = int(input())
meetings = [list(map(int, input().split())) for _ in range(N)]
dp = [0] * (N)

for start in range(N - 1, -1, -1):
    duration, cost = meetings[start]
    end = start + duration - 1
    
    if end >= N:
        dp[start] = 0
    
    else:
        if end == N - 1:
            dp[start] = cost
        else:
            dp[start] = cost + max(dp[end + 1:])
    
print(max(dp))