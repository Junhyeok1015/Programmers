answer = 0

def colaz(num):
    global answer
    
    if num == 1 or answer >= 500:
        return answer
    
    num = int(num / 2) if num % 2 == 0 else num*3 + 1
    answer += 1
    colaz(num)

def solution(num):
    global answer
    colaz(num)
    if answer >= 500:
        return -1
    else:
        return answer
