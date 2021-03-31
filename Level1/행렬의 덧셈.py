def solution(arr1, arr2):
    answer = []
    row = len(arr1)
    col = len(arr1[0])
    
    for i in range(row):
        ans = []
        for j in range(col):
            sum_ = arr1[i][j] + arr2[i][j]
            ans.append(sum_)
        answer.append(ans)
    return answer
