import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
G = {n: [] for n in range(1, N + 1)}
degree_matrix = [0 for _ in range(N + 1)]

for _ in range(M):
    frond, back = map(int, input().split())
    G[frond].append(back)
    degree_matrix[back] += 1

queue = deque()
answer = ""

for i in range(1, N + 1):
    if degree_matrix[i] == 0:
        queue.append(i)
        degree_matrix[i] -= 1

while queue:
    front_stud = queue.popleft()
    back_stud = G[front_stud]

    for stud in back_stud:
        degree_matrix[stud] -= 1
        
        if degree_matrix[stud] == 0:
            queue.append(stud)
            degree_matrix[stud] -= 1
    
    answer += str(front_stud) + " "

print(answer.rstrip())