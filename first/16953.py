from collections import deque

A, B = map(int, input().split())

queue = deque([[0, A]])
times = -1

while queue:
    current = queue.popleft()
    
    if current[1] == B:
        times = current[0]
        break

    elif current[1] < B:
        queue.append([current[0] + 1, current[1] * 2])
        queue.append([current[0] + 1, int(str(current[1]) + "1")])

if times == -1:
    print(-1)
else:
    print(times + 1)