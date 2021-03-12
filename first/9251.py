import sys
input = sys.stdin.readline

A = input().strip()
B = input().strip()

len_a = len(A)
len_b = len(B)

# A는 col B는 row
dp = [[0] * (len_b + 1) for _ in range(len_a + 1)]

for i in range(len_b - 1, -1, -1):
    char = B[i]

    for j in range(len_a - 1, -1, -1):
        if char == A[j]:
            dp[j][i] += dp[j + 1][i + 1] + 1

        else:
            dp[j][i] = max(dp[j + 1][i], dp[j][i + 1])

print(max(max(dp)))