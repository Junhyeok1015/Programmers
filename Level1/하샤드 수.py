def solution(x):
    answer = True
    num = sum(map(int,str(x)))
    return x % num == 0
