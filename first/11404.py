import sys
input = sys.stdin.readline

def floyd():
    result = G

    for init in range(1, N + 1):
        result[init][init] = 0
    
    for stop_over in range(1, N + 1):
        for start in range(1, N + 1):
            for dest in range(1, N + 1):
                result[start][dest] = min(result[start][dest], result[start][stop_over] + result[stop_over][dest])
    
    for row in range(1, N + 1):
        print(" ".join(map(lambda x : "0" if x == float('inf') else str(x), result[row][1:])))

N = int(input())
M = int(input())
G = [[float('inf')] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    start, end, cost = map(int, input().split())
    G[start][end] = min(cost, G[start][end])

floyd()

