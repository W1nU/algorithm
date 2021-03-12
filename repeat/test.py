string = input()

attack = 0
defence = 0

for char in string:
    if char == "(":
        attack += 1
    
    else:
        defence += 1

if attack == defence:
    print("YES")
else:
    print("NO")