import sys
from copy import deepcopy
sys.stdin = open("1486/input.txt", "r")

T = int(input())

def find(cnt, cur_height, height, N, ans):
    if cnt == N:
        if cur_height >= B:
            ans[0] = min(ans[0], cur_height)
            return

    if cnt < N:
        find(cnt + 1, cur_height + height[cnt], height, N, ans)
        find(cnt + 1, cur_height, height, N, ans)


for test_case in range(1, T + 1):
    
    N, B = map(int, input().split())
    height = list(map(int, input().split()))
    used = [False for _ in range(N)]
    height_set = set(height)
    ans = [999999999999]
    find(0, 0, height, N, ans)
                    

    print('#{} {}'.format(test_case, ans[0] - B))
