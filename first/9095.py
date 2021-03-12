T = int(input())
numbers = [int(input()) for _ in range(T)]
cache = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
    9: 0,
    10: 0
}

current_node = [0]
next_node = []

while len(current_node) != 0:
    for number in current_node:
        if number + 1 < 11:
            next_node.append(number + 1)
            cache[number + 1] += 1

        if number + 2 < 11:
            next_node.append(number + 2)
            cache[number + 2] += 1
        
        if number + 3 < 11:
            next_node.append(number + 3)
            cache[number + 3] += 1

    current_node = next_node
    next_node = []

for number in numbers:
    print(cache[number])

