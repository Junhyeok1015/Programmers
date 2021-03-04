import math

def solution(n):
    # answer = 0
    # if math.sqrt(n) == int(math.sqrt(n)):
    #     return
    
    return (math.sqrt(n) + 1) ** 2 if math.sqrt(n) == int(math.sqrt(n)) else -1
