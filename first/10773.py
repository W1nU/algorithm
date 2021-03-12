import sys
input = sys.stdin.readline

K = int(input())
numbers = []

for _ in range(K):
    number = int(input())
    if number == 0:
        numbers.pop()

    else:
        numbers.append(number)

print(sum(numbers))
