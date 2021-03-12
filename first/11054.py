import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
dp_inc = [1] * N

dp_dec = [1] * N

for i in range(N):
    for j in range(i):
        if numbers[i] > numbers[j]:
            dp_inc[i] = max(dp_inc[i], dp_inc[j] + 1)

for i in range(N - 1, -1, -1):
    for j in range(N - 1, i - 1, -1):
        if numbers[i] > numbers[j]:
            dp_dec[i] = max(dp_dec[i], dp_dec[j] + 1)

max_length = 0
for i in range(N):
    max_length = max(max_length, dp_inc[i] + dp_dec[i] - 1)

print(max_length)
