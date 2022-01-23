
import sys

 
sys.stdin = open("1861/input.txt", "r")

T = int(input())

def find(N, i, j, board, res, depth, start):
    depth = depth + 1
    if i < N - 1:
        if board[i][j] + 1 == board[i+1][j]:
            find(N, i+1, j, board, res, depth, start) 
    if i > 0:
        if board[i][j] + 1 == board[i-1][j]:
            find(N, i-1, j, board, res, depth, start) 
    if j < N - 1:
        if board[i][j] + 1 == board[i][j+1]:
            find(N, i, j+1, board, res, depth, start) 
    if j > 0:
        if board[i][j] + 1 == board[i][j-1]:
            find(N, i, j-1, board, res, depth, start) 

    if res[1] == depth:
        if res[0] > start:
            res[1] = depth
            res[0] = start 
    elif res[1] < depth:
        res[1] = depth
        res[0] = start 
    return
    

     

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    N = int(input())
    board = [list(int(val) for val in input().split()) for _ in range(N)]
    #print(board)

    result = 0
    
    res = [9999999999999, 0]
    depth = 0
    for i in range(N):
        for j in range(N):
            start = board[i][j]
            find(N, i, j, board, res, depth, start)

    
    print('#{} {} {}'.format(test_case, res[0], res[1]))
    # ///////////////////////////////////////////////////////////////////////////////////
