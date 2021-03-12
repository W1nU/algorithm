import sys
input = sys.stdin.readline

def isOneColor(paper):
    color = paper[0][0]

    for row in paper:
        for cell in row:
            if cell != color:
                return False
    
    return True

N = int(input())
paper = [input().split() for _ in range(N)]

one = 0
minus_one = 0
zero = 0

stack = [paper]

while stack:
    temp_paper = stack.pop()

    if isOneColor(temp_paper):
        if temp_paper[0][0] == "1":
            one += 1
        elif temp_paper[0][0] == "0":
            zero += 1
        else:
            minus_one += 1
    
    else:
        slice_length = len(temp_paper) // 3
        
        stack.append([row[:slice_length] for row in temp_paper[:slice_length]])
        stack.append([row[slice_length:slice_length * 2] for row in temp_paper[:slice_length]])
        stack.append([row[slice_length * 2:] for row in temp_paper[:slice_length]])

        stack.append([row[:slice_length] for row in temp_paper[slice_length:slice_length * 2]])
        stack.append([row[slice_length:slice_length * 2] for row in temp_paper[slice_length:slice_length * 2]])
        stack.append([row[slice_length * 2:] for row in temp_paper[slice_length:slice_length * 2]])

        stack.append([row[:slice_length] for row in temp_paper[slice_length * 2:]])
        stack.append([row[slice_length:slice_length * 2] for row in temp_paper[slice_length * 2:]])
        stack.append([row[slice_length * 2:] for row in temp_paper[slice_length * 2:]])

print(minus_one)
print(zero)
print(one)
