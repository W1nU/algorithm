import math

T = int(input())

for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    stars = [list(map(int, input().split())) for _ in range(n)]
    inner_stars = 0

    for star in stars:
        start_point_inner = False
        end_point_inner = False

        cx, cy, r = star

        # 시작점과 행성의 중심 거리 
        start_distance = math.sqrt(((x1 - cx) ** 2 + (y1 - cy) ** 2))
        if start_distance <= r:
            start_point_inner = True
        
        end_distance = math.sqrt(((x2 - cx) ** 2 + (y2 - cy) ** 2))
        if end_distance <= r:
            end_point_inner = True
        
        if (not start_point_inner and end_point_inner) or (start_point_inner and not end_point_inner):
            inner_stars += 1

    print(inner_stars)


        
