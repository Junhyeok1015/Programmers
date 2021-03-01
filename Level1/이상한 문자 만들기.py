def get_word(text):
    l = len(text)
    
    st = ""
    
    for i in range(l):
        if i % 2 == 0:
            st += text[i].upper()
        else:
            st += text[i].lower()
    return st

def solution(s):
    answer = ' '.join([get_word(t) for t in s.split(" ")])
    return answer
