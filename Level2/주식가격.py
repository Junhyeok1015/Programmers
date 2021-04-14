def solution(prices):
    answer = []
    cnt = 0
    for i in range(0, len(prices)):
        stock = prices[i]
        ans = 0
        for j in range(cnt+1, len(prices)):
            if stock <= prices[j]:
                ans += 1
            elif stock > prices[j] and j != len(prices):
                ans += 1
                break
        answer.append(ans)
        cnt += 1
    return answer
