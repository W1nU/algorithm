def find_parent(element):
    if sets[element] == element:
        return element
    else:
        root = find_parent(sets[element])
        return find_parent(root)

# def union(a, b):
#     if a < b:
#         sets[b] = find_parent(a)
    
#     else:
#         sets[a] = find_parent(b)

def union(v1, v2):
    v1 = find_parent(v1)
    v2 = find_parent(v2)

    if v1 == v2:
        return
    else:
        sets[v1] = v2

N = int(input())
sets = [n for n in range(N)]

while 1:

    unions = list(map(int, input().split()))

    if unions[0] == 1:
        print(find_parent(unions[1]) == find_parent(unions[2]))
    
    else:
        union(unions[1], unions[2])
    
    print(sets )
