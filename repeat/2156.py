# import sys
# input = sys.stdin.readline

# N = int(input())
# wines = [int(input()) for _ in range(N)]

# if N == 1:
#     print(max(wines))
# else:  
#     # 전전 화인을 마신 값, 직전 와인을 마신 값, 마시지 않은 값
#     dp = [[0, 0, 0] for _ in range(N)]
#     dp[0] = [wines[0], wines[0], wines[0]]
#     dp[1] = [wines[1], wines[1] + wines[0], wines[1]]

#     for i in range(2, N):
#         dp[i][0] = max(dp[i - 3]) + wines[i]
#         dp[i][1] = max(dp[i - 1][0], dp[i - 1][2]) + wines[i]
#         dp[i][2] = max(dp[i - 2]) + wines[i]

#     print(max(max(dp[-2]), max(dp[-1])))
    
import sys

I=sys.stdin.readline
a=[int(I())for i in range(int(I()))]
d=[0,a[0],0]

for i in a[1:]:
    d=[max(d),d[0]+i,d[1]+i]  
    print(f"{i}번째 와인의 {d}")

print(max(d))