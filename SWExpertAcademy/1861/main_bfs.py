
import sys
from collections import deque
sys.stdin = open("1861/input.txt", "r")
T = int(input())
for test_case in range(1, T + 1):
 
    N = int(input())
    board = [list(int(val) for val in input().split()) for _ in range(N)]

    result = 0
    q = deque()

    for i in range(N):
        for j in range(N):
            start = board[i][j]
            if i < N - 1:
                if board[i][j] + 1 == board[i+1][j]:
                    q.append((i,j,start, 1))
            if i > 0:
                if board[i][j] + 1 == board[i-1][j]:
                    q.append((i,j,start, 1))
            if j < N - 1:
                if board[i][j] + 1 == board[i][j+1]:
                    q.append((i,j,start, 1))
            if j > 0:
                if board[i][j] + 1 == board[i][j-1]:
                    q.append((i,j,start, 1))
    res_start, res_depth = 0, 0 

    while q:
        i, j, start, depth = q.popleft()

        if i < N - 1:
            if board[i][j] + 1 == board[i+1][j]:
                q.append((i+1,j,start, depth + 1))
        if i > 0:
            if board[i][j] + 1 == board[i-1][j]:
                q.append((i-1,j,start, depth + 1))
        if j < N - 1:
            if board[i][j] + 1 == board[i][j+1]:
                q.append((i,j+1,start, depth + 1))
        if j > 0:
            if board[i][j] + 1 == board[i][j-1]:
                q.append((i,j-1,start, depth + 1))     


        if depth == res_depth and start < res_start:
            res_start = start
        elif depth > res_depth:
            res_depth = depth
            res_start = start
    
    print('#{} {} {}'.format(test_case, res_start, res_depth))
 