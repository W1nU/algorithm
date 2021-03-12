K, N = list(map(int, input().split()))
lan_cables = [int(input()) for _ in range(K)]

min_length = 1
max_length = 2 ** 31

while True:
    current_length = (min_length + max_length) // 2
    devided_count = 0

    for cable in lan_cables:
        devided_count += cable // current_length
    
    if current_length == min_length:
        break
        
    if devided_count >= N:
        min_length = current_length
    
    else:
        max_length = current_length

devided_count = 0

for cable in lan_cables:
    devided_count += cable // max_length

if devided_count >= N:
    print(max_length)
else:
    print(min_length)