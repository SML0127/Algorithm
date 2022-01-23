from copy import deepcopy


def move_to_right(cur_pt, cur_str, board):
    new_str = deepcopy(cur_str)
    if cur_pt[1] + 1 < 4:
        value = board[cur_pt[0]][cur_pt[1] + 1]
        return str(new_str) + str(value), (cur_pt[0], cur_pt[1] + 1)
    else:
        return '', (0,0)

def move_to_left(cur_pt, cur_str, board):
    new_str = deepcopy(cur_str)
    if cur_pt[1] -1 >= 0:
        value = board[cur_pt[0]][cur_pt[1] -1]
        return str(new_str) + str(value), (cur_pt[0], cur_pt[1] - 1)
    else:
        return '', (0,0)


def move_to_top(cur_pt, cur_str, board):
    new_str = deepcopy(cur_str)
    if cur_pt[0] - 1 >= 0:
        value = board[cur_pt[0] - 1][cur_pt[1]]
        return str(new_str) + str(value), (cur_pt[0] - 1, cur_pt[1])
    else:
        return '', (0,0)


def move_to_bottom(cur_pt, cur_str, board):
    new_str = deepcopy(cur_str)
    if cur_pt[0] + 1 < 4:
        value = board[cur_pt[0] + 1][cur_pt[1]]
        return str(new_str) + str(value), (cur_pt[0] + 1, cur_pt[1])
    else:
        return '', (0,0)



# mv 6 times
def DFS(cur_pt, cur_str, board, num_mv, all_string_list):
    #print(cur_str, num_mv)
    if num_mv == 6:
        if len(cur_str) == 7:
            all_string_list.append(cur_str);
        return
 
    for i in range(4):
        if i == 0:
            new_str, new_pt = move_to_right(cur_pt, cur_str, board)
            DFS(new_pt, new_str, board, num_mv + 1, all_string_list)
        elif i == 1:
            new_str, new_pt = move_to_left(cur_pt, cur_str, board)
            DFS(new_pt, new_str, board, num_mv + 1, all_string_list)
        elif i == 2:
            new_str, new_pt = move_to_top(cur_pt, cur_str, board)
            DFS(new_pt, new_str, board, num_mv + 1, all_string_list)
        elif i == 3:
            new_str, new_pt = move_to_bottom(cur_pt, cur_str, board)
            DFS(new_pt, new_str, board, num_mv + 1, all_string_list)
        

#result = []
T = int(input())

for test_case in range(1, T + 1):
    Board = [list(str(val) for val in input().split()) for _ in range(4)] # always 4 x 4
    all_string_list = []
    for i in range(4): 
        for j in range(4):
            DFS((i, j), str(Board[i][j]), Board, 0, all_string_list) 

    all_string_set = set(all_string_list)  
    #result.append(len(all_string_set))
    print("#{} {}".format(test_case, len(all_string_set)))
