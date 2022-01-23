from copy import deepcopy

N = int(input())
Board = [list(map(int, input().split())) for _ in range(N)]


def rotate_clockwise(N, board):
    new_board = deepcopy(board)
    for i in range(N):
        for j in range(N):
            new_board[j][N-i-1] = board[i][j]
    return new_board
#2 2 4 = > 4 0 4
def compact(N, board):
    new_board = []
    for line in board:
        val_array = [i for i in line if i != 0];
        for idx, val in enumerate(val_array):
            if idx > 0:
                if val_array[idx - 1] == val_array[idx]:
                    val_array[idx - 1] = val_array[idx] * 2
                    val_array[idx] = 0
        new_val_array = [i for i in val_array if i != 0];
        new_board.append(new_val_array + [0] * (N - len(new_val_array)))
    return new_board

def DFS(N, board, count):
    result = max([max(line) for line in board]) # get max value in current board(2d array)
    if count == 5:
        return result;
    
    for _ in range(4):
        compacted_board = compact(N, board); # compact
        result = max( result, DFS(N, compacted_board, count + 1)) # compare max val in next board and max val in current board
        board = rotate_clockwise(N, board); # rotate for next
    return result



print(DFS(N, Board, 0))