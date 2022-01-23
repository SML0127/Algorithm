import sys
from collections import deque
from copy import deepcopy
sys.stdin = open("1486/input.txt", "r")

T = int(input()) 
for test_case in range(1, T + 1):
    
    N, B = map(int, input().split())
    height = list(map(int, input().split()))
    used = [False for _ in range(N)]
    height_set = set(height)
    q = deque()


    dictonary = {}
    for val in height:
        if val not in dictonary:
            dictonary[val] = 1
        else:
            dictonary[val] += 1

    cur_min = 999999999999

    for idx, val in enumerate(list(height_set)):
        tmp_dictonary = deepcopy(dictonary)
        tmp_dictonary[val] = tmp_dictonary[val] - 1 
        if tmp_dictonary[val] == 0:
            del tmp_dictonary[val]
        q.append((val, tmp_dictonary))
        while q:
            cur_sum, tmp_dic = q.popleft()
            #print(cur_sum, tmp_dic)
            for key in tmp_dic:
                if cur_sum + key >= B and (cur_sum + key - B < cur_min):
                    #print(cur_min, cur_sum + key, B, tmp_dic)
                    cur_min = cur_sum + key - B
                elif cur_sum + key < B:
                    tmp_dic1 = deepcopy(tmp_dic)
                    tmp_dic1[key] = tmp_dic1[key] - 1 
                    if tmp_dic1[key] == 0:
                        del tmp_dic1[key]        
                    q.append((cur_sum + key, tmp_dic1))

    print('#{} {}'.format(test_case, cur_min))
