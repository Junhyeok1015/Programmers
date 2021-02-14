def solution(n):
    result = ""
    
    while n >= 1:
        n, v = divmod(n, 3)
        
        result += str(v)
        
    answer = int(result, 3)
        
    return answer
