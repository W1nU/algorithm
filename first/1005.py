import sys
input = sys.stdin.readline
from collections import deque

T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    times = list(map(int, input().split()))
    G = { n: [] for n in range(1, N + 1) }
    RG = { n: [] for n in range(1, N + 1) }
    degree_matrix = [0] * N
    dp = [0] * N

    for _ in range(K):
        current, dest = map(int, input().split())
        G[current].append(dest)
        RG[dest].append(current)
        degree_matrix[dest - 1] += 1
    
    win_node = int(input())
    queue = deque([])   

    for index in range(N):
        if degree_matrix[index] == 0:
            degree_matrix[index] = -1
            queue.append(index + 1)

    
    while queue:
        current_node = queue.popleft()
        current_node_edge = G[current_node]
        current_node_prev = RG[current_node]

        if len(current_node_prev) == 0:
            dp[current_node - 1] = times[current_node - 1]
        
        else:
            max_time = 0

            for node in current_node_prev:
                if dp[node - 1] > max_time:
                    max_time = dp[node - 1]
            
            dp[current_node - 1] = times[current_node - 1] + max_time

        for node in current_node_edge:
            degree_matrix[node - 1] -= 1
        
        for index in range(N):
            if degree_matrix[index] == 0:
                degree_matrix[index] -= 1
                queue.append(index + 1)

    print(dp[win_node - 1])
    