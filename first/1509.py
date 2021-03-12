string = input()
N = len(string)

dp = [[False] * N for _ in range(N)]
min_dp = [float("inf")] * N
cycle = [n for n in range(N)]

for end in range(N):
    for start in range(end + 1):
        if start == end:
            dp[start][end] = True
        
        else:
            if end - start != 1:
                if string[start] == string[end] and dp[start + 1][end - 1]:
                    dp[start][end] = True

                    if cycle[start] < end:
                        cycle[start] = end

            else:
                if string[start] == string[end]:
                    dp[start][end] = True

                    if cycle[start] < end:
                        cycle[start] = end

for end in range(N):
    if dp[0][end]:
        min_dp[end] = 1

    else:
        for start in range(end + 1):
            if dp[start][end]:
                min_dp[end] = min(min_dp[end], min_dp[start - 1] + 1)

print(min_dp[-1])