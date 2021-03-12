N = int(input())

dp = { n: 1 for n in range(10) }
dp[0] = 0

for _ in range(1, N):
    new_dp = { n: 0 for n in range(10) }

    for n in range(10):
        if n == 0:
            new_dp[n] = dp[n + 1] % 1000000000
        
        elif n == 9:
            new_dp[n] = dp[n - 1] % 1000000000
        
        else:
            new_dp[n] = (dp[n - 1] + dp[n + 1]) % 1000000000

    dp = new_dp

sum_value = 0

for key in dp:
    sum_value += dp[key]

print(sum_value % 1000000000)