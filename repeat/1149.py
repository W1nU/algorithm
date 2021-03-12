import sys
input = sys.stdin.readline

N = int(input())

prev_costs = list(map(int, input().split()))

for _ in range(1, N):
    current_costs = list(map(int, input().split()))

    for color in range(3):
        if color == 0:
            current_costs[color] = min(prev_costs[1], prev_costs[2]) + current_costs[color]

        elif color == 1:
            current_costs[color] = min(prev_costs[0], prev_costs[2]) + current_costs[color]

        else:
            current_costs[color] = min(prev_costs[0], prev_costs[1]) + current_costs[color]

    prev_costs = current_costs

print(min(prev_costs)) 