def return_k(array, i, j, k):
    cut = array[i-1:j]
    cut = sorted(cut)
    return cut[k-1]
    
    
def solution(array, commands):    
    answer = [return_k(array, i, j, k) for i, j, k in commands]
    
    return answer
