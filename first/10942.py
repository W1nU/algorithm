import sys
input = sys.stdin.readline

N = int(input())
string = input().split()
M = int(input())
Q = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(M)]

dp = [[0] * N for _ in range(N)]

for end in range(N):
    for start in range(end + 1):
        if start == end:
            dp[start][end] = 1
        
        else:
            if end - start > 1:
                if string[start] == string[end] and dp[start + 1][end - 1]:
                    dp[start][end] = 1

            else:
                if string[start] == string[end]:
                    dp[start][end] = 1

for q in Q:
    start, end = q
    print(dp[start][end])