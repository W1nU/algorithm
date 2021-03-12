N, limit = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * (limit + 1) for _ in range(N)]

for item_count in range(N):
    for weight_limit in range(1, limit + 1):
        c_weight, c_value = items[item_count]

        if item_count == 0 and c_weight <= weight_limit:
            dp[item_count][weight_limit] = c_value
        
        else:
            if c_weight > weight_limit:
                dp[item_count][weight_limit] = dp[item_count - 1][weight_limit]

            else:
                if weight_limit - c_weight >= 0:
                    dp[item_count][weight_limit] = max(dp[item_count - 1][weight_limit - c_weight] + c_value, dp[item_count - 1][weight_limit])

                else:
                    dp[item_count][weight_limit] = dp[item_count - 1][weight_limit]      

print(dp[-1][-1])