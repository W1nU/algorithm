import sys
input = sys.stdin.readline

def merge(left, right):
    result = []
    idx_L = 0
    idx_R = 0

    while len(left) > idx_L and len(right) > idx_R:
        if left[idx_L] < right[idx_R]:
            result.append(left[idx_L])
            idx_L += 1
        
        else:
            result.append(right[idx_R])
            idx_R += 1
    
    if len(left) > idx_L:
        for idx in range(idx_L, len(left)):
            result.append(left[idx])

    if len(right) > idx_R:
        for idx in range(idx_R, len(right)):
            result.append(right[idx])

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
y_dixt = {y: [] for y in range(-100000, 100001)}

for _ in range(N):
    x, y = list(map(int, input().split()))

    y_dixt[y].append(x)
    
for y in y_dixt:
    if len(y_dixt[y]) != 0:
        sorted_y = merge_sort(y_dixt[y])
        for x in sorted_y:
            print(x, y)
        