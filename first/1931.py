import sys
input = sys.stdin.readline

def merge(left, right):
    result = []
    idx_L = 0
    idx_R = 0

    while idx_L < len(left) and idx_R < len(right):
        if left[idx_L][1] < right[idx_R][1]:
            result.append(left[idx_L])
            idx_L += 1
        
        elif left[idx_L][1] == right[idx_R][1]:
            if left[idx_L][0] < right[idx_R][0]:
                result.append(left[idx_L])
                idx_L += 1
            
            else:
                result.append(right[idx_R])
                idx_R += 1

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
meetings = [list(map(int, input().split())) for _ in range(N)]
sorted_meetings = merge_sort(meetings)
occupied_meetings = []

for meeting in sorted_meetings:
    if len(occupied_meetings) == 0 or occupied_meetings[-1][1] <= meeting[0]:
        occupied_meetings.append(meeting)

print(len(occupied_meetings))