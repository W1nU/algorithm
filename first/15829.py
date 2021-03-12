L = int(input())
string = input()
number_mapped_string = [ord(char) - 96 for char in string]
sigma = 0

for n, number in enumerate(number_mapped_string):
    sigma += number * (31 ** n)

print(sigma % 1234567891)