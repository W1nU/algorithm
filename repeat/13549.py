from collections import deque

N, K = map(int, input().split())

# 위치, 시간
queue = deque([(N, 0)])
distance = [float('inf')] * 100001
distance[N] = 0

while queue:
    current, time = queue.popleft()

    for i in range(3):
        next_time = time

        if i == 0:
            next_loc = current * 2

        elif i == 1:
            next_loc = current + 1
            next_time = time + 1

        else:
            next_loc = current - 1
            next_time = time + 1

        if 0 <= next_loc < 100001 and distance[next_loc] > next_time:
            queue.append((next_loc, next_time))
            distance[next_loc] = next_time

print(distance[K])