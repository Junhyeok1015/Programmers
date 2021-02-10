def solution(a, b):
    date = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']

    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    day = sum(month[:a-1]) + b - 1
    answer = date[day % 7]
    print(answer)
    
    return answer
