N = int(input())

count = 1
number = 666

while True:
    if count == N:
        print(number)
        break
    
    else:
        number += 1

        if str(number).find("666") != -1:
            count += 1