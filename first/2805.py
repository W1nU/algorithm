
import sys 

def merge(left, right):
    l = 0
    r = 0
    result = []

    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        
        else:
            result.append(right[r])
            r += 1

    if l < len(left):
        for idx in range(l, len(left)):
            result.append(left[idx])

    if r < len(right):
        for idx in range(r, len(right)):
            result.append(right[idx])

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

N, M = list(map(int, sys.stdin.readline().split()))
trees = list(map(int, sys.stdin.readline().split()))
trees = merge_sort(trees)

start = 0
end = trees[len(trees) - 1]

while start <= end:
    cutted_length = 0
    heigth = (start + end) // 2

    for i in trees:
        if heigth >= i:
            continue
        
        else:
            cutted_length += (i - heigth)

    if cutted_length >= M:
        start = heigth + 1
    
    else: 
        end = heigth - 1

if cutted_length >= M:
    print(heigth)
else:
    print(heigth - 1)