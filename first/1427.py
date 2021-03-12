string = input()
arr = []

for char in string:
    arr.append(char)

arr.sort(reverse=True)
print("".join(arr))