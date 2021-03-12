import sys
input = sys.stdin.readline

A = input().rstrip()
B = input().rstrip()
len_a = len(A)
len_b = len(B)
dp = [[0] * (len_a + 1) for _ in range(len_b + 1)]

for index_a in range(1, len_a + 1):
    char_a = A[index_a - 1]

    for index_b in range(1, len_b + 1):
        char_b = B[index_b - 1]
        
        if char_a == char_b:
            dp[index_b][index_a] = dp[index_b - 1][index_a - 1] + 1
        else:
            dp[index_b][index_a] = max(dp[index_b - 1][index_a], dp[index_b][index_a - 1])

string = []
x = len_a
y = len_b

while x > 0 and y > 0:
    if dp[y][x - 1] == dp[y][x]:
        x -= 1
    elif dp[y - 1][x] == dp[y][x]:
        y -= 1
    else:
        string.append(B[y - 1])
        x -= 1
        y -= 1

print(len(string))

if len(string) > 0:
    print("".join(string[::-1]))