strings = []

while True:
    string = input()

    if string == ".":
        break
    else:
        strings.append(string)

for string in strings:
    compare_stack = []
    is_fail = False

    for char in string:
        if char == "(":
            compare_stack.append("(")

        elif char == "[":
            compare_stack.append("[")

        elif char == ")":
            if len(compare_stack) != 0:
                compare_char = compare_stack.pop()
                if compare_char != "(":
                    print("no")
                    is_fail = True
                    break
            
            else:
                print("no")
                is_fail = True
                break
            

        elif char == "]":
            if len(compare_stack) != 0:
                compare_char = compare_stack.pop()
                if compare_char != "[":
                    print("no")
                    is_fail = True
                    break
            
            else:
                print("no")
                is_fail = True
                break
            
    if not is_fail:
        if len(compare_stack) == 0:
            print("yes")
        else:
            print("no")