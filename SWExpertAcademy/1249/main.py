
from copy import deepcopy
from collections import deque

def DFS(N, board, r, c, cur_cost, cost_list, mv, visited):    
    visited[r][c] = 1
    cur_cost = cur_cost + board[r][c]
    if mv > (N -1) * 2:
        return;
    if r == N-1 and c == N-1:
        cur_min = min(cost_list); 
        if cur_min == -1:
            cost_list[0] = cur_cost
        elif cost_list[0] > cur_cost:
            cost_list[0] = cur_cost
        return;
    if r > 0:
        if visited[r - 1][c] != 1:
            cur_visited = deepcopy(visited)
            DFS(N, board, r - 1, c,  cur_cost, cost_list, mv + 1, cur_visited)
    if r < N - 1:
        if visited[r + 1][c] != 1:
            cur_visited = deepcopy(visited)
            DFS(N, board, r + 1, c,  cur_cost, cost_list, mv + 1, cur_visited)
    if c > 0:
        if visited[r][c - 1] != 1:
            cur_visited = deepcopy(visited)
            DFS(N, board, r, c - 1,  cur_cost, cost_list, mv + 1, cur_visited)
    if c < N - 1:
        if visited[r][c + 1] != 1:
            cur_visited = deepcopy(visited)
            DFS(N, board, r, c + 1,  cur_cost, cost_list, mv + 1, cur_visited)





def BFSOLD(N, board, r, c, cur_cost, mv, q):    
    cost_list[0] = -1
    while q:
        visited, r, c, cur_cost, mv = q.popleft()
        cur_cost = cur_cost + board[r][c]
        visited[r][c] = 1
        if r == N-1 and c == N-1:
            cur_min = cost_list[0]; 
            if cur_min == -1:
                cost_list[0] = cur_cost
            elif cost_list[0] > cur_cost:
                cost_list[0] = cur_cost
        
        if mv <= int(N * N / 2) + (N - 1):
            if r > 0:
                if visited[r - 1][c] != 1:
                    if cost_list[0] == -1 or (board[r-1][c] + cur_cost) < cost_list[0]:
                        cur_visited = deepcopy(visited)
                        q.append((cur_visited, r-1, c, cur_cost, mv + 1))
            if r < N - 1:
                if visited[r + 1][c] != 1:
                    #cur_visited = deepcopy(visited)
                    if cost_list[0] == -1 or (board[r+1][c] + cur_cost) < cost_list[0]:
                        cur_visited = deepcopy(visited)
                        q.append((cur_visited, r+1, c, cur_cost, mv + 1))
            if c > 0:
                if visited[r][c - 1] != 1:
                    #cur_visited = deepcopy(visited)
                    if cost_list[0] == -1 or (board[r][c-1] + cur_cost) < cost_list[0]:
                        cur_visited = deepcopy(visited)
                        q.append((cur_visited, r, c-1, cur_cost, mv + 1))
            if c < N - 1:
                if visited[r][c + 1] != 1:
                    #cur_visited = deepcopy(visited)
                    if cost_list[0] == -1 or (board[r][c+1] + cur_cost) < cost_list[0]:
                        cur_visited = deepcopy(visited)
                        q.append((cur_visited, r, c+1, cur_cost, mv + 1))
    
    return cost_list[0]


def BFS(N, board, r, c, cur_cost, mv, q, cost_map):    
    while q:
        r, c, mv = q.popleft()            

        if mv > N*N:
            return ;

        if r > 0:
            if cost_map[r][c] + board[r-1][c] < cost_map[r-1][c]:
                cost_map[r-1][c] = cost_map[r][c] + board[r-1][c]
                q.append((r-1, c, mv + 1))
        if r < N - 1:
            if cost_map[r][c] + board[r+1][c] < cost_map[r+1][c]:
                cost_map[r+1][c] = cost_map[r][c] + board[r+1][c]
                q.append((r+1, c,mv + 1))
        if c > 0:
            if cost_map[r][c] + board[r][c-1] < cost_map[r][c-1]:
                cost_map[r][c-1] = cost_map[r][c] + board[r][c-1]
                q.append((r, c-1,mv + 1))
        if c < N - 1:  
            if cost_map[r][c] + board[r][c+1] < cost_map[r][c+1]:
                cost_map[r][c+1] = cost_map[r][c] + board[r][c+1]
                q.append((r, c+1, mv + 1))




T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    N = int(input())
    board = []
    for _ in range(N):
        line = str(input())
        new_line = []
        for val in line:
            new_line.append(int(val))
        board.append(new_line)

    r, c, mv = 0, 0, 0
    cost_list = [-1]
    cost_map = [[99999999999999999 for i in range(N)] for j in range(N)]
    cost_map[0][0] = 0
    q = deque()
    q.append((r, c, 0))

    #DFS(N, board, r, c, 0, cost_list, 0, visited)
    cost = BFS(N, board, r, c, 0, 0, q, cost_map)
    #print(cost_map)
    print('#{} {}'.format(test_case, cost_map[N-1][N-1]))
    # ///////////////////////////////////////////////////////////////////////////////////
