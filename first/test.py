# 소마 피시방
# P, N, H = map(int, input().split())
# pc_req = {n: [] for n in range(1, P + 1)}

# for _ in range(N):
#     pc, hour = map(int, input().split())

#     if hour <= H:
#         pc_req[pc].append(hour)

# for pc in pc_req:
#     req = pc_req[pc]
#     dp = [0] * (H + 1)

#     for i in range(len(req)):
#         hour, cost = req[i], req[i] * 1000
#         for j in range(hour, H + 1):
#             dp[j] = max(dp[j], dp[j - hour] + cost)

#     print(f"{pc} {max(dp)}")

# =================================================================
# from collections import deque

# N, M, E = map(int, input().split())
# nuts = list(map(int, input().split()))
# nuts_zero = []

# for nut in nuts:
#     nuts_zero.append(nut - E)

# nuts_zero.append(0)
# nuts_zero.sort()
# start = nuts_zero.index(0)
# eat = 0

# while eat <




# =================================================================
# from collections import deque

# N = int(input())
# costs = list(map(int, input().split()))

# # 남은 시작점, 끝점, 현재까지 가치
# queue = deque([(costs, 0)])
# ret = 0

# while queue:
#     arr, cost = queue.popleft()

#     if cost > ret:
#         ret = cost

#     if len(arr) > 1:
#         mid = len(arr) // 2
        
#         left = arr[:mid]
#         right = arr[mid:]

#         queue.append((left, cost + max(right)))
#         queue.append((right, cost + max(left)))
  
# print(ret)
# =================================================================
# from collections import deque

# skilles = input().split()
# N = int(input())
# G = {n: [] for n in skilles}
# degree_matrix = {n: 0 for n in skilles}
# ret = []

# for _ in range(N):
#     front, back = input().split()
#     G[front].append(back)
#     degree_matrix[back] += 1

# queue = deque()

# for skill in degree_matrix:
#     if degree_matrix[skill] == 0:
#         queue.append((skill, ""))
#         degree_matrix[skill] = -1

# while queue:
#     current_skill, combination = queue.popleft()
#     combination += current_skill
#     next_skill = G[current_skill]

#     if len(next_skill) == 0:
#         ret.append(combination)

#     for skill in next_skill:
#         degree_matrix[skill] -= 1
    

#     for skill in degree_matrix:
#         if degree_matrix[skill] == 0:
#             queue.append((skill, combination))
#             degree_matrix[skill] = -1

# length = len(ret)

# for _ in range(length):
#     print(" ".join(ret.pop()))