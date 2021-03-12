import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
# 직전 숫자가 포함된 결과, 직전 숫자를 포함하지 않는 결과
dp = [0] * N
dp[0] = numbers[0]
ret = numbers[0]

for n in range(1, N):
    dp[n] = max(numbers[n], dp[n - 1] + numbers[n])
    
    if dp[n] > ret:
        ret = dp[n]

print(ret)