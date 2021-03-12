import sys
input = sys.stdin.readline

def merge(left, right):
    result = []
    idx_L = 0
    idx_R = 0

    while idx_L < len(left) and idx_R < len(right):
        if left[idx_L] < right[idx_R]:
            result.append(left[idx_L])
            idx_L += 1

        else:
            result.append(right[idx_R])
            idx_R += 1
        
    while idx_L < len(left):
        result.append(left[idx_L])
        idx_L += 1
    
    while idx_R < len(right):
        result.append(right[idx_R])
        idx_R += 1
    
    return result

def merge_sort(array):
    if len(array) <= 1:
        return array
    
    mid = len(array) // 2

    left = array[:mid]
    right = array[mid:]

    l = merge_sort(left)
    r = merge_sort(right)

    return merge(l, r)

N = int(input())
numbers = list(map(int, input().split()))
numbers_set = set(numbers)
sorted_numbers = merge_sort(list(numbers_set))
answer_dict = { N: 0 for N in sorted_numbers }

prev_number = sorted_numbers[0]
count = 0

for number in sorted_numbers[1:]:
    if number != prev_number:
        count += 1
        answer_dict[number] = count
        prev_number = number

answer = ""

for number in numbers:
    answer += str(answer_dict[number])
    answer += " "

print(answer.strip())