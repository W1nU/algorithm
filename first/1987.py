import sys
input = sys.stdin.readline

MOVES = [(1, 0), (-1, 0), (0, 1), (0, -1)]
ret = 0

def DFS(x, y, count):
    global ret
    
    if count > ret:
        ret = count

    for add_x, add_y in MOVES:
        next_x, next_y = x + add_x, y + add_y

        if 0 <= next_x < C and 0 <= next_y < R and not alphabet[ord(maze[next_y][next_x])]:
            alphabet[ord(maze[next_y][next_x])] = True
            DFS(next_x, next_y, count + 1)
            alphabet[ord(maze[next_y][next_x])] = False


R, C = map(int, input().split())
maze = [input().rstrip() for _ in range(R)]
alphabet = {n: False for n in range(ord("A"), ord("Z") + 1)}

alphabet[ord(maze[0][0])] = True
DFS(0, 0, 1)
print(ret)