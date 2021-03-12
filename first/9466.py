import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def dfs(start):
    global no_team

    visited[start] = True
    cycle.append(start)

    next_node = selects[start - 1]

    if not visited[next_node]:
        dfs(next_node)
    
    else:
        cycle_start = False

        for stud in cycle:
            if stud == next_node:
                cycle_start = True
            
            if cycle_start:
                has_team[stud] = True
                no_team -= 1
            
T = int(input())

for _ in range(T):
    N = int(input())
    selects = list(map(int, input().split()))
    visited = [False] * (N + 1)
    has_team = [False] * (N + 1)
    no_team = N

    for stud in range(1, N + 1):
        if not visited[stud]:
            cycle = []
            dfs(stud)
    
    print(no_team)

