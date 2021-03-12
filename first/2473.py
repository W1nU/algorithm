import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
numbers.sort()
min_gap = (float('inf'), [])

for index in range(N - 2):
    a = numbers[index]
    s, e = index + 1, N - 1

    while s < e:
        b, c = numbers[s], numbers[e]
        ph = a + b + c
        
        if ph < 0:
            s += 1

        else:
            e -= 1
        
        gap = abs(ph)

        if gap == 0:
            print(*[a,b,c])
            sys.exit()

        elif gap < min_gap[0]:
            min_gap = (gap, [a, b, c])

print(*min_gap[1])