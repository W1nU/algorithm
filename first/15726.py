import math 

numbers = list(map(int, input().split()))

print(math.floor(max(numbers[0] * numbers[1] / numbers[2], numbers[0] / numbers[1] * numbers[2])))