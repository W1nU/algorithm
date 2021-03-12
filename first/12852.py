from collections import deque

N = int(input())
# 최소 횟수, 부모 
counts = [[float("inf"), ""] for _ in range(N + 1)]

# 지금 위치, 시간
queue = deque([(N, 0)])
counts[N] = [0, N]

while queue:
    current, times = queue.popleft()
    new_time = times + 1

    if current % 3 == 0:
        next_loc = current // 3

        if 1 <= next_loc <= 1000000 and new_time < counts[next_loc][0]:
            counts[next_loc] = [new_time, current]
            queue.append((next_loc, new_time))
    
    if current % 2 == 0:
        next_loc = current // 2

        if 1 <= next_loc <= 1000000 and new_time < counts[next_loc][0]:
            counts[next_loc] = [new_time, current]
            queue.append((next_loc, new_time))

    
    next_loc = current - 1

    if 1 <= next_loc <= 1000000 and new_time < counts[next_loc][0]:
        counts[next_loc] = [new_time, current]
        queue.append((next_loc, new_time))

current = 1
numbers = [str(current)]

while current != N:
    parent = counts[current][1]
    numbers.append(str(parent))
    current = parent

print(counts[1][0])
numbers.reverse()
print(" ".join(numbers))