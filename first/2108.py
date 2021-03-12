import math
import sys

def merge(left, right):
    result = []
    idx_i = 0
    idx_r = 0

    while idx_i < len(left) and idx_r < len(right):
        if left[idx_i] <= right[idx_r]:
            result.append(left[idx_i])
            idx_i += 1
        
        else:
            result.append(right[idx_r])
            idx_r += 1
    
    if idx_i < len(left):
        for index in range(idx_i, len(left)):
            result.append(left[index])
    
    if idx_r < len(right):
        for index in range(idx_r, len(right)):
            result.append(right[index])
    
    return result

def merge_sort(array):
    if len(array) == 1:
        return array
    
    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]

    l = merge_sort(left)
    r = merge_sort(right)
    return merge(l, r)

def find_second_small(array):
    if len(array) == 1:
        return array[0]
    
    else:
        return array[1]

N = int(sys.stdin.readline())
sum_value = 0
numbers = []
numbers_seen = { x: 0 for x in range(-4000, 4001) }
max_seen_count = 0
max_seen_numbers = []

for _ in range(N):
    number = int(sys.stdin.readline())

    sum_value += number
    numbers_seen[number] += 1

    if numbers_seen[number] > max_seen_count:
        max_seen_count = numbers_seen[number]
        max_seen_numbers = [number]
    
    elif numbers_seen[number] == max_seen_count:
        max_seen_numbers.append(number)
    
    numbers.append(number)

max_seen_numbers = merge_sort(max_seen_numbers)

numbers = merge_sort(numbers)
print(round(sum_value / N))
print(numbers[len(numbers) // 2])
print(find_second_small(max_seen_numbers))
print(numbers[len(numbers) - 1] - numbers[0])