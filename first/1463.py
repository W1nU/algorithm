def find_least_count_to_1(current_node):
    count = 0
    next_node = []

    while True:
        count += 1

        for number in current_node:
            if number == 1:
                return 0 

            if number % 2 == 0:
                if number // 2 == 1:
                    return count
                next_node.append(number // 2)
        
            if number % 3 == 0:
                if number // 3 == 1:
                    return count
                next_node.append(number // 3)

            if number - 1 == 1:
                return count
            next_node.append(number - 1)

        current_node = next_node
        next_node = []

N = int(input())
current_node = [N]
print(find_least_count_to_1(current_node))