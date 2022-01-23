

import sys
sys.stdin = open("1868/input.txt", "r")

T = int(input())

def search(N, click_i, click_j, board, num_all):
    cnt = 0
    for i in range(click_i-1, click_i+2):
        for j in range(click_j-1, click_j+2):
            if i >= 0 and j>=0 and i < N and j < N:
                if board[i][j] == '*':
                    cnt += 1
    board[click_i][click_j] = cnt
    if cnt == 0:
        
        for i in range(click_i-1, click_i+2):
            for j in range(click_j-1, click_j+2):
                if i >= 0 and j>=0 and i < N and j < N:
                    if board[i][j] == '.':
                        num_all[0] = num_all[0] - 1
                        search(N, i, j, board, num_all)


def search_one_block(N, click_i, click_j, board):
    cnt = 0
    for i in range(click_i-1, click_i+2):
        for j in range(click_j-1, click_j+2):
            if i >= 0 and j>=0 and i < N and j < N:
                if board[i][j] == '*':
                    cnt += 1
    if cnt == 0:
        return True
    else:
        return False

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    N = int(input()) # <= 300
    cnt = 0
    board = []
    for _ in range(N):
        tmp = []
        string_tmp = input()
        for idx in range(len(string_tmp)):
            if str(string_tmp[idx]) == '.':
                cnt += 1
            tmp.append(str(string_tmp[idx]))
        board.append(tmp)
    #print(board)
    #print(len(board), len(board[0]))
    num_all = [cnt]
    #exist_zero = False
    for i in range(N):
        for j in range(N):
            if board[i][j] == '.':
                if search_one_block(N, i, j, board):
                    #exist_zero = True
                    search(N,i,j,board, num_all)


    print('#{} {}'.format(test_case, num_all[0]))
    #board = [list(str(val) for val in input().split()) for _ in range(N)] # * = , . = ??
    # ///////////////////////////////////////////////////////////////////////////////////
