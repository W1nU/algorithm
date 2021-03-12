import sys
input = sys.stdin.readline

def check_paper_color(paper):
    color = None 

    for row in paper:
        for col in row:
            if color == None:
                color = col
            else:
                if color != col:
                    return False
    
    return True

N = int(input())
paper = [input().split() for _ in range(N)]
sliced_paper = []

blue = 0
white = 0

if check_paper_color(paper):
    if paper[0][0] == "1":
        blue += 1
    
    else:
        white += 1

else:
    N = len(paper) // 2

    first = [row[:N] for row in paper[:N]]
    second = [row[N:] for row in paper[:N]]
    third = [row[:N] for row in paper[N:]]
    fourth = [row[N:] for row in paper[N:]]

    sliced_paper.extend([first, second, third, fourth])

    while sliced_paper:
        temp_paper = sliced_paper.pop()

        if check_paper_color(temp_paper):
            if temp_paper[0][0] == "1":
                blue += 1
            else:
                white += 1
        
        else:
            N = len(temp_paper) // 2

            first = [row[:N] for row in temp_paper[:N]]
            second = [row[N:] for row in temp_paper[:N]]
            third = [row[:N] for row in temp_paper[N:]]
            fourth = [row[N:] for row in temp_paper[N:]]

            sliced_paper.extend([first, second, third, fourth])

print(white)
print(blue)
