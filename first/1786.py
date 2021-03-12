import sys
input = sys.stdin.readline

def make_pi(P):
    length = len(P)
    j = 0
    pi = [0] * length

    for i in range(1, length):
        while j > 0 and P[i] != P[j]:
            j = pi[j - 1]

        if P[i] == P[j]:
            j += 1
            pi[i] = j
    
    return pi

def KMP(T, P):
    pi = make_pi(P)
    length_T = len(T)
    length_P = len(P)
    j = 0
    count = 0
    location = []

    for i in range(length_T):
        while j > 0 and P[j] != T[i]:
            j = pi[j - 1]

        if T[i] == P[j]:
            if j == length_P - 1:
                count += 1
                location.append(i - length_P + 2)
                j = pi[j]

            else:
                j += 1
    
    print(count)
    print(" ".join(map(str,location)))
    
T = input().rstrip()
P = input().rstrip()
KMP(T, P)