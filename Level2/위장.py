'''from collections import defaultdict
def solution(clothes):
    answer = 1
    dress=defaultdict(list)
    for a,b in clothes:   
        dress[b].append(a)
    for i in dress.keys():
        answer *= (len(dress[i])+1)
    
    return answer-1'''
def solution(clothes):
    count = {}
    for i in clothes:
        if i[1] in count:
            count[i[1]] += 1
        else:
            count[i[1]] = 1
    
    temp = 1
    for j in count.values():
        temp *= j
        if len(count.values()) == 1:
            return len(clothes) + 1

        
    return len(clothes)+temp

''' 각 카테고리 별로 아이템이 꼭포함되지 않아도 되는 경우의수가 한개가 더있으니 -1하고,

전체에서 카테고리별로 아무것도 포함하지 않는 경우의 수 +1를 하면 점화식은 다음과 같다.

(모자의갯수 + 1) * (바지의갯수 + 1) * (안경의갯수 + 1)-1 로 계산해야 한다.

점화식 : answer *= (len(dress[i])+1)'''
