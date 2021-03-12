import sys
input = sys.stdin.readline

N = int(input())
packs = [0]
packs.extend(list(map(int, input().split())))

dp = [0] * (N + 1)
dp[1] = packs[1]

for i in range(2, N + 1):
    for j in range(1, i + 1):
        dp[i] = max(dp[i], dp[i - j] + packs[j])


print(dp[-1])