N = int(input())
people = [list(map(int, input().split())) for _ in range(N)]

for N, person in enumerate(people):
    bigger_count = 0

    for N2, compare_person in enumerate(people):
        if N == N2:
            continue
        
        if person[0] < compare_person[0] and person[1] < compare_person[1]:
            bigger_count += 1
        
    print(bigger_count + 1 )
