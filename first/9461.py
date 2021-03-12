import sys
input = sys.stdin.readline

T = int(input())
case = [int(input()) - 1 for _ in range(T)]

dp = [1,1,1,2,2]

for i in range(5, 100):
    dp.append(dp[i - 5] + dp[i - 1])

for number in case:
    print(dp[number])
