import re
def solution(record):
    answer = []

    user_dic={}
    for val in record:
        if val.split()[0] != 'Leave':
            user_dic[val.split()[1]] = val.split()[2]
        if val.split()[0] == 'Enter':
            answer.append(val.split()[1] + '님이 들어왔습니다.')
        elif val.split()[0] == 'Leave':
            answer.append(val.split()[1] + '님이 나갔습니다.')
    
    for idx, val in enumerate(answer):
        answer[idx] = user_dic[val.split('님이')[0]] + '님이' + val.split('님이')[1]
    
    return answer