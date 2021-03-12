import sys
input = sys.stdin.readline

N, S = map(int, input().split())
numbers = list(map(int, input().split()))

start, end = 0, 1
temp = numbers[start] + numbers[end]
min_length = float('inf')

while start <= N - 1:
    if temp >= S:
        if end - start + 1 < min_length:
            min_length = end - start + 1
        
        else:
            temp -= numbers[start]
            start += 1
    
    else:
        if end < N - 1:
            end += 1
            temp += numbers[end]
        
        else:
            break

print(min_length if min_length != float('inf') else 0)
