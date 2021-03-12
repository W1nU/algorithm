from collections import deque

def merge(a, b):
    result = []
    idx_a = 0
    idx_b = 0

    while idx_a < len(a) and idx_b < len(b):
        if a[idx_a] > b[idx_b]:
            result.append(b[idx_b])
            idx_b += 1
        
        else:
            result.append(a[idx_a])
            idx_a += 1
    
    while idx_a < len(a):
        result.append(a[idx_a])
        idx_a += 1

    while idx_b < len(b):
        result.append(b[idx_b])
        idx_b += 1
    
    return result

def merge_sort(array):
    if len(array) <= 1:
        return array
    
    else:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]

        l = merge_sort(left)
        r = merge_sort(right)

        return merge(l, r)

N, M = map(int, input().split())
numbers = list(set(map(int, input().split())))
sorted_numbers = merge_sort(numbers)
parsed_numbers = []

for n, number in enumerate(sorted_numbers):
    parsed_numbers.append([number])

queue = deque(parsed_numbers)

while queue:
    current = queue.popleft()

    if len(current) == M:
        for number in current[:-1]:
            print(number, end=" ")
        
        print(current[-1])

    else:
        for number in sorted_numbers:
            temp = current[:]
            temp.append(number)
            queue.append(temp)