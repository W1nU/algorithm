import sys
input = sys.stdin.readline

N = int(input())
triangle = [list(map(int, input().split())) for _ in range(N)]

for level in range(1, N):
    for index in range(len(triangle[level])):
        l, r = index - 1, index

        if 0 <= l and r < level:
            triangle[level][index] = max(triangle[level - 1][l], triangle[level - 1][r]) + triangle[level][index]
        
        elif 0 > l:
            triangle[level][index] = triangle[level - 1][0] + triangle[level][index]
    
        else:
            triangle[level][index] = triangle[level - 1][-1] + triangle[level][index]

print(max(triangle[-1]))