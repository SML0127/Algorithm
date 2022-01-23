 
import sys 
def status2int(R, C, r, c, dir, mem):
    dic = {
        '<':0, '>':1, '^':2, 'v':3
    }
    return (C*r + c) * 4*16 + dic[dir]*16 + mem
 
def get_next_pos(R, C, dir, r, c):
    if dir == 'v':
        return (r+1) if r < (R-1) else 0, c
    elif dir == '^':
        return (r-1) if r > 0 else (R-1), c
    elif dir == '>':
        return r, (c+1) if c < (C-1) else 0
    elif dir == '<':
        return r, (c-1) if c > 0 else (C-1)
 
def find(board, visited, queue, R, C, test_case):
 
    result = False
 
    while (len(queue) > 0):
        (r, c, dir, mem) = queue.pop()
        #print(queue, r,c,dir,mem)
        v = board[r*C+c]
        if v == '@':
            return True
        visited_idx = status2int(R, C, r, c, dir, mem)
        if visited[visited_idx] == True:
            continue
 
        visited[visited_idx] = True
        if v == '?':
            for dir in ['<','>','^','v']:
                new_r, new_c = get_next_pos(R, C, dir, r, c)
                queue.append((new_r, new_c, dir, mem))
        else:
            if v in ['<','>','^','v']:
                dir = v
            elif v == '_':
                dir = '>' if mem == 0 else '<'
            elif v == '|':
                dir = 'v' if mem == 0 else '^'
            elif v in ['0','1','2','3','4','5','6','7','8','9']:
                mem = int(v)
            elif v == '+':
                mem = (mem + 1) if mem < 15 else 0
            elif v == '-':
                mem = (mem - 1) if mem > 0 else 15
            new_r, new_c = get_next_pos(R, C, dir, r, c)
            queue.append((new_r, new_c, dir, mem))
    return result
 
sys.stdin = open("1824/input.txt", "r")
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    R, C = map(int, input().split())
    board = ''
    for i in range(0, R):
        board += input().strip()
 
    #print(board)
 
    visited = [False] * (len(board)*4*64)
    queue = [(0,0,'>',0)]
    result = find(board, visited, queue, R, C, test_case)
    print("#{} {}".format(test_case, 'YES' if result else 'NO'))