import collections

def solution(participant, completion):
    answer = ''
    
    temp = collections.Counter(participant) - collections.Counter(completion)
    
    return list(temp.keys())[0]