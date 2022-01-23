from collections import deque
def solution(key1, lock):
    answer = False
    need_list = []
    for idx, row in enumerate(lock):
        if 0 in row:
            for idx2, col in enumerate(row):
                if col == 0:
                    need_list.append([idx, idx2])
    q = deque()
    if len(need_list) == 0:
        return True
    tmp1 = key1
    left_right_dic = {}
    up_down_dic = {}
    for k in range(4):
        key = []
        tmp = [[0] * len(key1) for _ in range(len(key1))]
        for r in range(len(key1)):
            for c in range(len(key1)):
                tmp[c][len(key1) - 1 - r] = tmp1[r][c]

        for idx, row in enumerate(tmp):
            if 1 in row:
                for idx2, col in enumerate(row):
                    if col == 1:
                        key.append([idx, idx2])
        q.append([sorted(key),k,[0,0]])
        
        up_down_dic[k] = []
        tmp1 = tmp

    while q:
        candi_key, k, history = q.popleft()
        check = True
        cnt = 0
        for val in candi_key: 
            if val in need_list:
                cnt += 1
            if val[0] >= 0 and val[1] >= 0:
                if val[0] < len(lock) and val[1] < len(lock):
                    if lock[val[0]][val[1]] == 1:
                        check = False
                        break;
        if check == True and cnt == len(need_list):
            answer = True
            break;

        new_key = []
        dx, dy = (1,-1,0,0), (0,0,1,-1)
        for i in range(0,4): # +1, -1,  +1, -1
            new_candi_key = []
            new_candi_key1 = []

            check1 = True;
            
            if [history[0]+dx[i], history[1] + dy[i]] not in up_down_dic[k]: 
                for val in candi_key:
                    new_val = [val[0] + dx[i], val[1] + dy[i]]
                    if new_val[0] >= 0 and new_val[1] >= 0 and new_val[0] < len(lock) and new_val[1] < len(lock):
                        new_candi_key1.append(new_val)
                    new_candi_key.append(new_val)
                    
                if check1 == True:
                    if str(sorted(new_candi_key1)) not in left_right_dic:
                        q.append([sorted(new_candi_key), k, [history[0]+dx[i], history[1] + dy[i]]])
                        up_down_dic[k].append([history[0]+dx[i], history[1] + dy[i]])
                        left_right_dic[str(sorted(new_candi_key1))] = 1

                
    return answer