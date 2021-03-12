import sys
input = sys.stdin.readline

def union(a, b):
    root_a = find(a)
    root_b = find(b)

    if root_a == root_b:
        return
    else:
        sets[root_a] = root_b

def find(a):
    parent = sets[a]

    if parent == a:
        return parent
    
    else:
        root = find(parent)
        sets[parent] = root
        return root

N, M = map(int, input().split())
maze = [input().rstrip() for _ in range(N)]
sets = [n for n in range(0, N * M)]

for row in range(N):
    for col in range(M):
        current_node = (M * row) + col

        direction = maze[row][col]

        if direction == "D":
            next_node = (M * (row + 1)) + col

        elif direction == "L":
            next_node = (M * row) + col - 1

        elif direction == "R":
            next_node = (M * row) + col + 1

        else:
            next_node = (M * (row - 1)) + col
        
        union(current_node, next_node)

answer = 0

for i in range(N * M):
    if i == sets[i]:
        answer += 1

print(answer)