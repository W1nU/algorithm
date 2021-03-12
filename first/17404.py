import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
costs = [list(map(int, input().split())) for _ in range(N)]

# R, G, B로 각각 시작했을때
dp = [[0] * 3 for _ in range(3)]

for start_color in range(3):
    for row in range(1, N):
        print(dp)
        temp_cost = []

        if row == 1:
            if start_color == 0:
                temp_cost.append(float('inf'))
                temp_cost.append(costs[0][0] + costs[1][1])
                temp_cost.append(costs[0][0] + costs[1][2])

            elif start_color == 1:
                temp_cost.append(costs[0][1] + costs[1][0])
                temp_cost.append(float('inf'))
                temp_cost.append(costs[0][1] + costs[1][2])
            
            else:
                temp_cost.append(costs[0][2] + costs[1][0])
                temp_cost.append(costs[0][2] + costs[1][1])
                temp_cost.append(float('inf'))

        else:
            for color in range(3):
                if color == 0:
                    cost = min(dp[start_color][1], dp[start_color][2]) + costs[row][color]

                elif color == 1:
                    cost = min(dp[start_color][0], dp[start_color][2]) + costs[row][color]

                else:
                    cost = min(dp[start_color][0], dp[start_color][1]) + costs[row][color]

                temp_cost.append(cost)   

        dp[start_color] = temp_cost
            
min_price = float('inf')

for start_color in range(3):
    for color in range(3):
        if start_color != color:
            min_price = min(min_price, dp[start_color][color])
    
print(min_price)

