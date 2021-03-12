import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
dp = [1 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if numbers[i] > numbers[j]:
            dp[i] = max(dp[j] + 1, dp[i])

print(max(dp))