import heapq

def dikstra(start):
    answer = [float('inf')] * (N + 1)
    visited = [False] * (N + 1)

    answer[start] = 0
    visited[start] = True 

    # 지금까지의 거리 합, 위치
    queue = [(0, start)]

    while queue:
        distance, node = heapq.heappop(queue)

        next_nodes = G[node]

        for next_node in next_nodes:
            next_distance = min(answer[next_node], distance + 1)
            answer[next_node] = next_distance

            if not visited[next_node]:
                heapq.heappush(queue, (next_distance, next_node))
                visited[next_node] = True
            
    return answer

N, M = map(int, input().split())
G = {n : set() for n in range(1, N + 1)}

for _ in range(M):
    a, b = map(int, input().split())
    G[a].add(b)
    G[b].add(a)

ret = 0
min_number = float('inf')

for stud in range(1, N + 1):
    number = sum(dikstra(stud)[1:])

    if min_number > number:
        ret = stud
        min_number = number
    
print(ret)
