import sys
input = sys.stdin.readline

T = int(input())

dp = [[0] * 31 for _ in range(31)]

for west in range(1, 31):
    for east in range(west, 31):
        if west == 1:
            dp[west][east] = east

        else:    
            if west == east:
                dp[west][east] = 1
            
            else:
                dp[west][east] = sum(dp[west - 1][west - 1: east])

for _ in range(T):
    west, east = map(int, input().split())
    print(dp[west][east])

# from sys import stdin
# from itertools import combinations
# input = stdin.readline

# dp=[0 for _ in range(31)]

# dp[0] = 1
# dp[1] = 1

# for i in range(2, 31):
#     dp[i] = i*dp[i-1]

# print(dp)

# for tc in range(int(input())):
#     w, e = map(int, input().split())
#     print((dp[e])//(dp[e-w]*dp[w]))