def merge_two_array(left, right):
    i = 0
    j = 0
    result = []

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
            j += 1
    
    if i < len(left):
        for idx in range(i, len(left)):
            result.append(left[idx])
    
    if j < len(right):
        for idx in range(j, len(right)):
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
    return merge_two_array(l, r)

array = [1,3,33,3321,2,4,5]
sortedArr = merge_sort(array)
print(sortedArr)
    
