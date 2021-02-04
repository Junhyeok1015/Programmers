board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]	

def solution(board, moves):
    answer = 0
    
    basket = []
    
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                basket.append(board[j][i-1])
                board[j][i-1] = 0
                
                
                if len(basket) > 1:
                    if basket[-2] == basket[-1]:
                        for _ in range(2):
                            basket.pop(-1)
                        
                        answer += 2             
                break
    return answer


print(solution(board, moves))
