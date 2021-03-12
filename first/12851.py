from collections import deque

N, K = map(int, input().split())

min_time = [float("inf")] * 100001
count = 0

# 내 위치, 걸린 시간
queue = deque([(N, 0)])
min_time[N] = 0

if N == K:
    count += 1
    min_time[K] = 0

else:    
    while queue:
        current, time = queue.popleft()
        next_time = time + 1

        for i in range(3):
            if i == 0:
                next_loc = current - 1
            elif i == 1:
                next_loc = current + 1
            else:
                next_loc = current * 2
            
            if 0 <= next_loc <= 100000 and min_time[next_loc] >= next_time:
                if next_loc == K:
                    if min_time[next_loc] == next_time:
                        count += 1
                    else:
                        count = 1
                        min_time[next_loc] = next_time
                
                else:
                    if min_time[next_loc] >= next_time:
                        min_time[next_loc] = next_time
                        queue.append((next_loc, next_time))

print(min_time[K])
print(count)
