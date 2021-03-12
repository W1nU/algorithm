import sys
input = sys.stdin.readline

strings = []

while 1:
    string = input().rstrip()

    if string == ".":
        break

    strings.append(string)

for string in strings:
    stack = []
    ret = True

    for char in string:
        if char == "[":
            stack.append("[")

        elif char == "(":
            stack.append("(")

        elif char == ")":
            if stack:
                compare = stack.pop()
                
                if compare != "(":
                    ret = False
                    break
            
            else:
                ret = False
                break

        elif char == "]":
            if stack:
                compare = stack.pop()

                if compare != "[":
                    ret = False
                    break
            
            else:
                ret = False
                break

    if ret and not stack:
        print("yes")
    
    else:
        print("no")