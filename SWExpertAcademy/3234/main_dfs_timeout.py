
import sys
from copy import deepcopy
sys.stdin = open("3234/input.txt", "r")

def put(weights, used, left, right, result):
    #print(used, left, right)
    if len(weights) == len(left) + len(right):
        result[0] += 1
        return;

    lw, rw = 0, 0
    for i in left:
        lw += i
    for i in right:
        rw += i
    rm, aw = 0, 0
    for idx in range(len(weights)):
        if idx not in used:
            rm += weights[idx]
    for val in weights:
        aw += val
    if lw >= rm + rw or lw >= aw - lw: 
        n = len(weights) - len(used)
        np = 1
        for i in range(1, n+1):
            np *= i
        result[0] += pow(2, n) * np
        return;

    for cur_idx in range(len(weights)):
        if cur_idx not in used:
            w = weights[cur_idx]
            lw, rw = 0, 0
            for i in left:
                lw += i
            for i in right:
                rw += i

            # put to right
            if lw >= rw + w:
                new_left = deepcopy(left)
                new_right = deepcopy(right)
                new_right.append(w)
                new_used = deepcopy(used)
                new_used.append(cur_idx)
                put(weights, new_used, new_left, new_right, result)
            # put to left
            new_left = deepcopy(left)
            new_left.append(w)
            new_right = deepcopy(right)
            new_used = deepcopy(used)
            new_used.append(cur_idx)
            put(weights, new_used, new_left, new_right, result)

def put_right_heavy(weights, used, left, right, result):
    #print(used, left, right)
    if len(weights) == len(left) + len(right):
        
        #print(used, left, right)
        result[0] += 1
        print(result[0])
        return;
    lw, rw = 0, 0
    for i in left:
        lw += i
    for i in right:
        rw += i
    rm = 0
    for idx in range(len(weights)):
        if idx not in used:
            rm += weights[idx]
    if rw >= rm + lw: 
        n = len(weights) - len(used)
        np = 1
        for i in range(1, n+1):
            np *= i
        result[0] += pow(2, n) * np
        print(result[0])
        return;

    for cur_idx in range(len(weights)):
        if cur_idx not in used:
            w = weights[cur_idx]
            lw, rw = 0, 0
            for i in left:
                lw += i
            for i in right:
                rw += i

            # put to right
            if lw <= rw + w:
                new_left = deepcopy(left)
                new_right = deepcopy(right)
                new_right.append(w)
                new_used = deepcopy(used)
                new_used.append(cur_idx)
                #print('0', weights, new_used, new_left, new_right, result)
                put_right_heavy(weights, new_used, new_left, new_right, result)
            # put to left
            if lw  + w <= rw:
                new_left = deepcopy(left)
                new_left.append(w)
                new_right = deepcopy(right)
                new_used = deepcopy(used)
                new_used.append(cur_idx)
                #print('1', weights, new_used, new_left, new_right, result)
                put_right_heavy(weights, new_used, new_left, new_right, result)


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    
    N = int(input())
    weights = list(map(int, input().split()))
    result = [0]
    left, right, used = [], [], []
    cur_idx = 0
    put(weights, used, left, right, result)
    
  

    print('#{} {}'.format(test_case, result[0]))
    # ///////////////////////////////////////////////////////////////////////////////////
