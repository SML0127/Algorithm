'''def go(left,right,depth,state):
    if depth == n:
        return 1
    if(D[state]>0):
        return D[state]
    cnt =0
    for i in range(n):
        if not visited[i]:
            visited[i]=True
            cnt+=go(left+mam[i],right,depth+1,state+mul[i])
            if left >= right +mam[i]:
                cnt+=go(left,right+mam[i],depth+1,state+mul[i]*2)
            visited[i] = False;
    D[state] = cnt
    return cnt
 
for cs in range(int(input())):
    ans = 0
    n = int(input())
    mam = list(map(int,input().split()))
    visited = [0]*10
    mul = [1, 3, 9, 27, 81, 243, 729, 2187, 6561,19683]
    D = [0] * (mul[n])
    print("#",cs+1," ",go(0,0,0,0),sep="")
'''
import sys
sys.stdin = open("3234/input.txt", "r")
T = int(input())
  
def dfs(used, idx, sum_l, sum_r, state):
    global ans
    global N
  
    if sum_r > sum_l:
        return 0
    if idx == N:
        return 1
    if dp[state] != -1:
        return dp[state]
  
    sol = 0
  
    for i in range(N):
        if used[i] == 0:
            used[i] = 1
            sol += dfs(used, idx + 1, sum_l + board[i], sum_r, state+m3[i])    
            sol += dfs(used, idx + 1, sum_l, sum_r+board[i], state+m3[i]*2)
            used[i] = 0
  
    dp[state] = sol
    return sol
  
for t in range(1, T+1):
    N = int(input())
    board = list(map(int, input().split()))
    ans = 0
    used = [0]*N
  
    m3 = [1, 3, 9, 27, 81, 243, 729, 2187, 6561]
    dp = [-1]*20000
  
    for i in range(N):
        idx = 1
        sum_r = 0
        sum_l = board[i]  # 첫 번째꺼는 무조건 왼쪽에 던짐
        used[i] = 1
        state = m3[i]
        ans += dfs(used, idx, sum_l, sum_r, state)
        used[i] = 0
  
    print("#%d %d" % (t, ans))
