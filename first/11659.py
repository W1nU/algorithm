# to_int = lambda x : int(x)

# N, M = list(map(to_int, input().split(" ")))
# numbers = list(map(to_int, input().split(" ")))
# ij = [list(map(to_int, input().split(" "))) for _ in range(M)]

# for i, j in ij:
#     print(sum(numbers[i - 1 : j]))

to_int = lambda x : int(x)

N, M = input().split(" ")
numbers = input().split(" ")
ij = [input().split(" ") for _ in range(int(M))] 

accumulate_sum = [] 

before_sum = 0

for number in numbers:
    before_sum += int(number)
    accumulate_sum.append(before_sum)

for i, j in ij:
    i = int(i)
    j = int(j)
    if i == 1:
        print(accumulate_sum[j - 1])

    else:
        print(accumulate_sum[j - 1] - accumulate_sum[i - 2])