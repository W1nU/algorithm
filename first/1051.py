N, M = list(map(int, input().split()))
numbers = [input() for _ in range(N)]
max_size = 0

for y in range(N - 1):
    for x in range(M - 1):
        current_index = numbers[y][x]
        
        for size in range(M-x):
            if y + size >= N:
                break
            
            if numbers[y][x + size] == current_index and numbers[y + size][x] == current_index and numbers[y + size][x + size] == current_index:
                if max_size < (size + 1) ** 2:
                    max_size = (size + 1) ** 2

if max_size == 0:
    max_size = 1
    
print(max_size)