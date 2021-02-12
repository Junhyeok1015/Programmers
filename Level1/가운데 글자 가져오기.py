def solution(s):
    answer = ''
    if len(s) % 2 == 0: # 짝수일때
        num = len(s) // 2
        answer = s[num-1:num+1]
    else:
        answer = s[len(s)//2]
    return answer
