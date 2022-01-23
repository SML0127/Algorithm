# python 3.9.7
import copy
from collections import deque


n = int(input().split()[0]); # 1 <= n <= 20

init_board = [[int(val) for val in input().split()] for _ in range(n)]
 
q = deque()
q.append((init_board, 0)) # board & mv_num 


global_max_val = -1;
for line in init_board:
    for val in line:
        if val > global_max_val:
            global_max_val = val;
if n == 1:
    print(global_max_val)


def mv_right_to_left(board, max_val):
    prev_num = -1;
    cur_max_val = max_val

    for idx_origin, line in enumerate(board):
        val_array = []
        for idx in range(n):
            if line[idx] != 0:
                val_array.append(line[idx])
           
        for idx, val in enumerate(val_array):
            if idx < len(val_array) - 1:
                if val_array[idx] == val_array[idx + 1]:
                    val_array[idx] = val_array[idx] * 2
                    val_array[idx + 1] = 0
                    if cur_max_val < val_array[idx]:
                        cur_max_val = val_array[idx]
        
        board[idx_origin] = [0 for _ in range(len(board))]
        idx = 0
        for val in val_array:
            if val != 0:
                board[idx_origin][idx] = val
                idx = idx + 1  
    return board, cur_max_val

def mv_left_to_right(board, max_val):
    prev_num = -1;
    cur_max_val = max_val

    for idx_origin, line in enumerate(board):
        val_array = []
        for idx in range(n):
            if line[idx] != 0:
                val_array.append(line[idx])

     
        for i, val in enumerate(val_array):
            idx = len(val_array) - i - 1
            if idx > 0 :
                if val_array[idx - 1] == val_array[idx]:
                    val_array[idx] = val_array[idx - 1] * 2
                    val_array[idx - 1] = 0
                    if cur_max_val < val_array[idx]:
                        cur_max_val = val_array[idx]

        val_array.reverse() # 2 0 4

        board[idx_origin] = [0 for _ in range(len(board))]
        idx = len(board) - 1
        for val in val_array: # 2 0 4
            if val != 0:
                board[idx_origin][idx] = val
                idx = idx - 1

    return board, cur_max_val



def transpose(board):
    new_board = [[ 0 for _ in range(n)] for _ in range(n)]
    row = 0
    for line in board:
        for idx, val in enumerate(line):
            new_board[idx][row] = val
        row = row + 1
    return new_board


while q:
    
    cur_board, num_try = q.popleft()
 
    # 0 1 2 3 4
    if num_try > 5:
        print(global_max_val)
        break;
    for i in range(4):
        if i == 0: #right to left 
            input_board = copy.deepcopy(cur_board)
            res_board, new_max_val  = mv_right_to_left(input_board, global_max_val)
            if global_max_val < new_max_val:
                global_max_val = new_max_val
 
            q.append((res_board, num_try + 1))
        elif i == 1: #left to right
            input_board1 = copy.deepcopy(cur_board)
 
            res_board1, new_max_val  = mv_left_to_right(input_board1, global_max_val)
            if global_max_val < new_max_val:
                global_max_val = new_max_val
 
            q.append((res_board1, num_try + 1))
        elif i == 2: #b to t
            input_board2 = copy.deepcopy(cur_board)
            tmp_board2 = transpose(input_board2)
            tmp_board2, new_max_val  = mv_right_to_left(tmp_board2, global_max_val)
            res_board2 = transpose(tmp_board2)

            if global_max_val < new_max_val:
                global_max_val = new_max_val
 
            q.append((res_board2, num_try + 1))
        elif i == 3: #t to b
            input_board3 = copy.deepcopy(cur_board)
            tmp_board3 = transpose(input_board3)
            tmp_board3, new_max_val = mv_left_to_right(tmp_board3, global_max_val)
            res_board3 = transpose(tmp_board3)

            if global_max_val < new_max_val:
                global_max_val = new_max_val
 
            q.append((res_board3, num_try + 1))