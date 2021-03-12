import sys
input = sys.stdin.readline

N, M = list(map(int, input().split()))
graph = { str(n): [] for n in range(1, N + 1) }

for _ in range(M):
    v1, v2 = input().split()
    graph[v1].append(v2)
    graph[v2].append(v1)

visited = []
component_count = 0

for vertex in graph:
    if vertex not in visited:
        start_vertex = vertex
        stack = graph[start_vertex]
        component_count += 1

        while stack:
            next_vertex = stack.pop()

            if next_vertex not in visited:
                visited.append(next_vertex)
                stack.extend(graph[next_vertex])

print(component_count)