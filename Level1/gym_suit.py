import copy

def solution(n, lost, reserve):
    answer = 0

    new_reserve = list(set(reserve) - set(lost))
    new_lost_f = list(set(lost) - set(reserve))
    new_lost_b = copy.deepcopy(new_lost_f)
    
    # forward first
    for l in new_reserve:
        f = l + 1
        b = l - 1
        
        if f in new_lost_f:
            new_lost_f.remove(f)
        elif b in new_lost_f:
            new_lost_f.remove(b)
    
    # backward first
    for l in new_reserve:
        f = l + 1
        b = l - 1
        
        if b in new_lost_b:
            new_lost_b.remove(b)
        elif f in new_lost_b:
            new_lost_b.remove(f)
    
    if len(new_lost_f) > len(new_lost_b):
        answer = n - len(new_lost_b)
    else:
        answer = n - len(new_lost_f)
    
    return answer
