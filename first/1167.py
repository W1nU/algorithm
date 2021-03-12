import sys
input = sys.stdin.readline

def dfs(start):
    stack = [(start, 0)]
    visited = [False] * (len(trees) + 1)
    visited[start] = True
    max_node = None
    max_weight = 0

    while stack:
        current_node, current_weight = stack.pop()
        next_node = trees[current_node].items()

        for node, weight in next_node:
            if not visited[node]:
                new_weight = weight + current_weight

                if new_weight > max_weight:
                    max_weight = new_weight
                    max_node = node
                
                stack.append((node, new_weight))
                visited[node] = True
    
    return max_node, max_weight

V = int(input())
trees = { n: {} for n in range(1, V + 1)}

for _ in range(V):
    inpt = list(map(int, input().split()))
    
    for index in range(1, len(inpt) - 1, 2):
        trees[inpt[0]][inpt[index]] = inpt[index + 1]

node, weight = dfs(1)
node, result = dfs(node)

print(result)