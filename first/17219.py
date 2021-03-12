import sys
input = sys.stdin.readline

N, M = list(map(int, input().split()))
password_dict = { }

for _ in range(N):
    site, password = input().split()
    password_dict[site] = password

for _ in range(M):
    site = input()[:-1]
    print(password_dict[site])