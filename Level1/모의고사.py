def solution(answers):
    answer = []
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    dic = {x : 0 for x in range(1, 4)}
    
    for i, ans in enumerate(answers):
        if ans == p1[i % len(p1)]:
            dic[1] += 1
        if ans == p2[i % len(p2)]:
            dic[2] += 1
        if ans == p3[i % len(p3)]:
            dic[3] += 1
            
    answer = [k for k, v in dic.items() if v == max(dic.values())]
    
    return sorted(answer)
