
import sys
from collections import deque
sys.stdin = open("1226/input.txt", "r")

def move(board, start_i, start_j, mv, q, visited):
    movement = [(-1,0), (1,0), (0,1), (0,-1)]
    all_mv_x = movement[mv][0] 
    all_mv_y = movement[mv][1]

    if (start_i + all_mv_x >= 1 and start_i + all_mv_x <= 14 and start_j + all_mv_y >= 1 and start_j + all_mv_y <= 14) and board[start_i + all_mv_x ][start_j + all_mv_y] == 0: 
        if visited[start_i + all_mv_x][start_j + all_mv_y] == 0:
            q.append([start_i + all_mv_x, start_j + all_mv_y, mv])
        return False;
    if (start_i + all_mv_x >= 1 and start_i + all_mv_x <= 14 and start_j + all_mv_y >= 1 and start_j + all_mv_y <= 14) and board[start_i + all_mv_x ][start_j + all_mv_y] == 3: 
        return True;
        

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for _ in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    board = []
    test_case = int(input())
    visited = []
    s = (1,1)
    for i in range(16):
        tmp = []
        tmp2 = []
        string_tmp = input()
        for idx in range(16):
            tmp.append(int(string_tmp[idx]))
            if int(string_tmp[idx]) == 2:
                s = (i, idx)
                tmp2.append(0)
            elif int(string_tmp[idx]) == 1:
                tmp2.append(1)
            else:
                tmp2.append(0)
        #print(tmp2)
        board.append(tmp)
        visited.append(tmp2)

    #print(visited)
    #각 시점에서 4방향으로 구르는걸 계속 queue에 저장, 정확히는 움직인 후의 좌표 랑 어느 방향으로 움직엿었는지


    q = deque()
    q.append([s[0], s[1],  -1])
    
    result = 0
    while q:
        start_i, start_j, prev_mv = q.popleft()
        #print(start_i, start_j)
        visited[start_i][start_j] = 1
        
        if start_i - 1 > 0: # to top
            if board[start_i - 1][start_j] != 1:
                if prev_mv != 1:
                    res = move(board, start_i, start_j, 0, q, visited)
        if start_i + 1 < 15: # bottom
            if board[start_i + 1][start_j] != 1:
                if prev_mv != 0:
                    res = move(board, start_i, start_j, 1, q, visited)
        if start_j - 1 > 0: # left
            if board[start_i][start_j - 1] != 1:
                if prev_mv != 2:
                    res = move(board, start_i, start_j, 3, q, visited)
        if start_j + 1 < 15: # right
            if board[start_i][start_j + 1] != 1:
                if prev_mv != 3:
                    res = move(board, start_i, start_j, 2, q, visited)
        if res == True:
            result = 1
            

    print('#{} {}'.format(test_case, result))


    # ///////////////////////////////////////////////////////////////////////////////////
