N, M = map(int, input().split())
factorial = [0] * (N + 1)
factorial[1] = 1

for n in range(2, N + 1):
    factorial[n] = factorial[n - 1] * n

if N == M:
    print5(1)
else:
    print(factorial[N] // (factorial[M] * factorial[N - M]))