def union(v1, v2):
    v1 = find(v1)
    v2 = find(v2)

    if v1 == v2:
        return
    else:
        sets[v2] = v1
        
def find(value):
    if value == sets[value]:
        return value
    else:
        root = find(sets[value])
        sets[value] = root
        return root

N, M = map(int, input().split())
known = list(map(int, input().split()))[1:]
parties = [list(map(int, input().split()[1:])) for _ in range(M)]
sets = [n for n in range(N + 1)]
count = 0

for party in parties:
    selected = party[0]

    for person in party[1:]:
        union(selected, person) 

for party in parties:
    available = True

    for person in party:
        if not available:
            break

        for known_person in known:
            if person == known_person:
                available = False
                break 

            else:
                if find_parent(person) == find_parent(known_person):
                    available = False

    if available:
        count += 1

print(count)
