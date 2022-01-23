import sys

sys.stdin = open("1211/input.txt", "r")

T = 10
def go(i, j, board, prev_mv, cnt):
    if i == 99:
        return cnt
    if j > 0 and prev_mv != 2: 
        if board[i][j-1] == 1:
            return go(i, j-1, board, 3, cnt + 1)
        else:
            if j <99 and prev_mv != 3: 
                if board[i][j+1] == 1:
                    return go(i, j+1, board, 2, cnt + 1)
                elif board[i+1][j] == 1:
                    return go(i+1, j, board, 1, cnt + 1)   
            elif board[i+1][j] == 1:
                return go(i+1, j, board, 1, cnt + 1)
    elif j <99 and prev_mv != 3: 
        if board[i][j+1] == 1:
            return go(i, j+1, board, 2, cnt + 1)
        else:
            if j > 1 and prev_mv != 2:  
                if board[i][j-1] == 1:
                    return go(i, j-1, board, 2, cnt + 1)
                elif board[i+1][j] == 1:
                    return go(i+1, j, board, 1, cnt + 1)   
            elif board[i+1][j] == 1:
                return go(i+1, j, board, 1, cnt + 1)
    else:
        if board[i+1][j] == 1:
            return go(i+1, j, board, 1, cnt + 1)   

for _ in range(1, T + 1):
    test_case = int(input())
    board = [list(map(int, input().split())) for _ in range(100)]
    min_distance = 999999
    result = 0
    for i in range(100):
        if board[0][i] == 1:
            distance = go(0, i, board, 1, 1)
            if min_distance > distance:
                result = i
                min_distance = distance
 
    print('#{} {}'.format(test_case, result))
