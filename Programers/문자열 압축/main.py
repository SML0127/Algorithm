def solution(s):
    answer = 0
    string_len = len(s)
    result = {}
    idx = 0
    pre_val = -1
    cur_min = 9999
    for k in range(1, int(len(s))):
        idx = 0
        len_dic = {}
        prev_val = -1
        cand_string = ''
        cnt = 1
        while True:
            if idx > len(s):
                break;
            val = s[idx: idx+k]
            if prev_val == -1:
                if idx + 2*k > len(s):
                    if cnt == 1:
                        cnt = ''
                    cand_string += str(cnt) + val + s[idx + k: ]
                    cnt = 1
                    break;
            elif prev_val != -1:
                if prev_val == val:
                    cnt += 1
                    if idx + 2*k > len(s):
                        if cnt == 1:
                            cnt = ''
                        cand_string += str(cnt) + prev_val +  s[idx + k: ]
                        cnt = 1
                        break;
                else:
                    if idx + 2*k > len(s):
                        if cnt == 1:
                            cnt = ''
                        cand_string += str(cnt) + prev_val + val + s[idx+k: ]
                        cnt = 1
                        break;
                    else:
                        if cnt == 1:
                            cnt = ''
                        cand_string += str(cnt) + prev_val
                        cnt = 1
            prev_val = val
            idx += k
        len_dic[k] = cand_string
        if cur_min > len(cand_string) and len(cand_string) != 0:
            cur_min = len(cand_string)
        str1 = ''
    #    print(len_dic)
    if cur_min == 9999:
        cur_min = 1
    #print(cur_min)

    
    return cur_min