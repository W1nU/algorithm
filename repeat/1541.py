import re
from collections import deque

expression = input()
stack = []
r = re.compile("(\+|\-)")
expression = deque(r.split(expression))

while expression:
    e = expression.popleft()

    if e == "-":
        continue

    elif e == "+":
        prev_number = stack.pop()
        next_number = int(expression.popleft())
        stack.append(prev_number + next_number)

    else:
        stack.append(int(e))

ans = stack[0]

for number in stack[1:]:
    ans -= number

print(ans)

