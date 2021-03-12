A, B, C = list(map(int, input().split()))

def solution(number, times, devide):
    if times == 1:
        return number % devide
    
    else:
        if times % 2 == 0:
            return solution(number, times // 2, devide) * solution(number, times // 2, devide) % devide
        else:
            return solution(number, times // 2, devide) * solution(number, times // 2 + 1, devide) % devide

print(solution(A, B, C))