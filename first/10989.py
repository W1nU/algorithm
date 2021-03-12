# import sys 

# def merge(left, right):
#     reuslt = []
#     idx_L = 0
#     idx_R = 0

#     while idx_L < len(left) and idx_R < len(right):
#         if left[idx_L] < right[idx_R]:
#             reuslt.append(left[idx_L])
#             idx_L += 1
        
#         else:
#             reuslt.append(right[idx_R])
#             idx_R += 1
    
#     if idx_L < len(left):
#         for idx in range(idx_L, len(left)):
#             reuslt.append(left[idx])

#     if idx_R < len(right):
#         for idx in range(idx_R, len(right)):
#             reuslt.append(right[idx])
    
#     return reuslt

# def merge_sort(array):
#     if len(array) <= 1:
#         return array
    
#     mid = len(array) // 2

#     left = array[:mid]
#     right = array[mid:]

#     l = merge_sort(left)
#     r = merge_sort(right)
#     return merge(l, r)

# N = int(sys.stdin.readline())
# numbers = [int(sys.stdin.readline()) for _ in range(N)]
# numbers = merge_sort(numbers)

# for number in numbers:
#     print(number)

import sys 

N = int(input())
counter = [0 for _ in range(1, 10002)]

for _ in range(N):
    number = int(sys.stdin.readline())
    counter[number] += 1


for n, count in enumerate(counter):
    for _ in range(count):
        print(n)
