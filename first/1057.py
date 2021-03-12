N, kim, im = list(map(int, input().split()))
round_count = 0

while True:
    round_count += 1

    kim = kim // 2 + kim % 2
    im = im // 2 + im % 2

    if kim == im:
        print(round_count)
        break