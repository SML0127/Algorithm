def solution(s):
    answer = []
    s_list = s.split('},') # 
    if len(s_list) == 1:
        answer = [int(s_list[0].split('{{')[1].split('}}')[0])]
    else:
        tmp_list = []
        for idx, val in enumerate(s_list):
            if idx == 0:
                num_list = val.split('{{')[1].split(',')
            elif idx == len(s_list) - 1:
                num_list = val.split('{')[1].split('}}')[0].split(',')
            else:
                num_list = val.split('{')[1].split(',')
            tmp_list.append(num_list)
        sorted_list = sorted(tmp_list, key = lambda item: len(item))
        
        for idx, val in enumerate(sorted_list):
            if idx == 0:
                answer.append(int(val[0]))
            else:
                for v in val:
                    if int(v) not in answer:
                        answer.append(int(v))

        
    return answer