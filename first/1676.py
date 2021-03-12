N = int(input())
facto = [0] * (N + 1)

if N == 0:
    print(0)
else:
    facto[1] = '1'

    for n in range(2, N + 1):
        facto[n] = str(int(facto[n - 1]) * n)

    count = 0

    for char in facto[-1][::-1]:
        if char == "0":
            count += 1
        else:
            break

    print(count)