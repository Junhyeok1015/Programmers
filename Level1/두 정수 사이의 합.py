def solution(a, b):
    answer = 0
    
    if a == b:
        return a

    return sum(range(min(a, b), max(a, b) + 1))
