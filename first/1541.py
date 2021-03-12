from collections import deque

expression = input()
disassembled = deque([])

number = ""

for char in expression:
    if char == "+" or char == "-":
        disassembled.append(int(number))
        number = ""
        disassembled.append(char)
    
    else:
        number += char

disassembled.append(int(number))
new_expression = []

while disassembled:
    exp = disassembled.popleft()

    if exp == "+":
        prev_number = new_expression.pop()
        new_expression.append(prev_number + disassembled.popleft())

    elif exp == "-":
        continue

    else:
        new_expression.append(exp)

min_number = new_expression[0]

for number in new_expression[1:]:
    min_number -= number

print(min_number)