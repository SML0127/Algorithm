
import sys
from collections import deque

def read(board, mv, r, c, memory, q, visited, R, C):
    res = False
    visited[mv][memory][r][c] = 1
    if board[r][c] == '<':
        mv = 1
    elif board[r][c] == '>':
        mv = 0
    elif board[r][c] == '^':
        mv = 2
    elif board[r][c] == 'v':
        mv = 3
    elif board[r][c] == '_':# 0 right, 1 left, 2 top, 3 bottom
        if memory == 0:
            mv = 0
        else:
            mv = 1
    elif board[r][c] == '|':
        if memory == 0:
            mv = 3
        else:
            mv = 2
    elif board[r][c] == '?':
        if visited[3][memory][(r+1) % R][c] != 1:
            #visited[3][memory][(r+1) % R][c] = 1
            
            q.append([3, (r+1) % R, c, memory])
        new_r = r
        if new_r - 1 < 0:
            new_r = R - 1
        if visited[2][memory][new_r][c]!= 1:
            #visited[2][memory][new_r][c] = 1
            q.append([2, new_r, c, memory])


        if visited[0][memory][r][(c+1) % C] != 1:
            #visited[0][memory][r][(c+1) % C] = 1
            q.append([0, r, (c+1) % C, memory])
        
        new_c = c
        if new_c - 1 < 0:
            new_c = C - 1

        if visited[1][memory][r][new_c] != 1:
            #visited[1][memory][r][new_c] = 1
            q.append([1, r, new_c, memory])
        return False

    elif board[r][c] == '@':
        return True

    elif board[r][c] in ['0', '1', '2','3', '4', '5', '6', '7', '8', '9']:
        memory = int(board[r][c])
    elif board[r][c] == '+':
        memory = memory + 1 
        if memory >= 16:
            memory = 0
    elif board[r][c] == '-':
        memory = memory - 1 
        if memory < 0:
            memory = 15

    if mv == 0:
        c = (c + 1) % C
    elif mv == 1:
        c = c - 1
        if c < 0:
            c = C - 1
    elif mv == 2:
        r = r - 1
        if r < 0:
            r = R - 1
    elif mv == 3:
        r = (r + 1) % R
    if visited[mv][memory][r][c] != 1:
        q.append([mv, r, c, memory])
 
    return False


sys.stdin = open("1824/input.txt", "r")
T = int(input())

for test_case in range(1, T + 1):
    R, C = map(int, input().split())
    board = [list(input()) for _ in range(R)]
    visited = [[[[0 for _ in range(C)] for _ in range(R)] for _ in range(16)] for _ in range(5)]
    memory = 0
    mv = 0 # 0 right, 1 left, 2 top, 3 bottom
    r, c = 0, 0
    res = False
    q = deque() # to in (격자칸, 메모리)
    q.append([0, r, c, memory])
    while q:

        mv, r, c, memory = q.popleft()
        res = read(board, mv, r, c, memory, q, visited, R, C)
        if res == True:
            break;

    if res == True:
        res = 'YES'
    else:
        res = 'NO'
    print('#{} {}'.format(test_case, res))
    # ///////////////////////////////////////////////////////////////////////////////////
