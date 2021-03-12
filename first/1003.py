T = int(input())
N = [int(input()) for _ in range(T)]
fib_cache = {}

for n in range(0, 41):
    if (n == 0):
        fib_cache[n] = {
            0 : 1,
            1 : 0
        }

    elif (n == 1):
        fib_cache[n] = {
            0: 0,
            1: 1
        }
    
    else:
        n_minus_1 = fib_cache[n - 1]
        n_minus_2 = fib_cache[n - 2]

        fib_cache[n] = {
            0 : n_minus_1[0] + n_minus_2[0],
            1: n_minus_1[1] + n_minus_2[1]
        }

for n in N:
    print(fib_cache[n][0], fib_cache[n][1])