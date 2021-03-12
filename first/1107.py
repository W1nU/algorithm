def calc_gep(a, b):
    return abs(int(a) - int(b))

target_channel = input()
broken_count = int(input())

if broken_count != 0:
    broken_number = list(map(int, input().split()))
    available_number = []

    for number in range(10):
        if number not in broken_number:
            available_number.append(number)

else:
    available_number = [number for number in range(0, 10)]

if abs(int(target_channel) - 100) <= len(target_channel) or len(available_number) == 0:
    print(abs(int(target_channel) - 100))    

else:
    all_channel = [str(number) for number in available_number]
    before_boundary = 0
    count = 1
    close_channel = all_channel[0]
    push_count = 0
    max_gap = 10000000001

    while count < len(target_channel) + 1:
        next_node = []
        
        for current_element in all_channel[before_boundary:]:
            for number in available_number:
                gen_number = current_element + str(number)
                if calc_gep(gen_number, target_channel) < max_gap:
                    max_gap = calc_gep(gen_number, target_channel)
                    next_node.append(current_element + str(number))

        before_boundary = len(all_channel)

        for channel in next_node:
            if channel[0] != "0":
                all_channel.append(channel)

        count += 1

    for number in all_channel:
        if calc_gep(number, target_channel) < calc_gep(close_channel, target_channel):
            close_channel = number

    push_count = len(str(int(close_channel)))

    if calc_gep(close_channel, target_channel) + push_count > calc_gep(target_channel, 100):
        print(calc_gep(target_channel, 100))

    else:
        print(push_count + calc_gep(close_channel, target_channel))
