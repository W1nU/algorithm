import sys
input = sys.stdin.readline
from collections import Counter

def find_highest():
    start = 0
    end = max(heights)

    while start <= end:
        mid = (start + end) // 2
        cut = 0

        for height, count in heights.items():
            if height > mid:
                cut += (height - mid) * count

        if cut >= M:
            start = mid + 1

        else:
            end = mid - 1
    
    print(end)
    
N, M = map(int, input().split())
heights = Counter(list(map(int, input().split())))
find_highest()