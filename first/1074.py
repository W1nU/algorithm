N, y, x = list(map(int, input().split()))

def find_visit_number(x, y, N, prev_count):
    if N == 0:
        return prev_count
    
    benchmark = ((2 ** N) // 2) - 1
    new_prev_count = prev_count

    if x > benchmark and y > benchmark:
        new_prev_count += (2 ** (2 * N - 2)) * 3
        new_x = x - (2 ** (N - 1))
        new_y = y - (2 ** (N - 1))

    elif x > benchmark and y <= benchmark:
        new_prev_count += (2 ** (2 * N - 2)) * 1
        new_x = x - (2 ** (N - 1))
        new_y = y

    elif x <= benchmark and y > benchmark:
        new_prev_count += (2 ** (2 * N - 2)) * 2
        new_x = x
        new_y = y - (2 ** (N - 1))

    elif x <= benchmark and y <= benchmark:
        new_x = x
        new_y = y

    return find_visit_number(new_x, new_y, N - 1, new_prev_count)

print(find_visit_number(x, y, N, 0))