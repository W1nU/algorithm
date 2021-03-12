import sys
input = sys.stdin.readline

N, M = map(int, input().split())
mem = [0]
mem.extend(list(map(int, input().split())))
cost = [0] 
cost.extend(list(map(int, input().split())))

result = float('inf')
dp = [[0] * (sum(cost) + 1) for _ in range(N + 1)]

for n in range(1, N + 1):
    for cost_index in range(1, sum(cost) + 1):
        if cost[n] <= cost_index:
            dp[n][cost_index] = max(dp[n - 1][cost_index], dp[n - 1][cost_index - cost[n]] + mem[n])

        else:
            dp[n][cost_index] = dp[n - 1][cost_index]

        if dp[n][cost_index] >= M:
            result = min(result, cost_index)
            
print(result if result != float('inf') else 0)