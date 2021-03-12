from collections import deque

N, M = map(int, input().split())

queue = deque([str(n) for n in range(1, N + 1)])

while queue:
    current = queue.popleft()

    if len(current) == M:
        for char in current[:-1]:
            print(char, end=" ")
        
        print(current[-1])

    else:
        for number in range(int(current[-1]), N + 1):
            queue.append(current + str(number))
    
