def solution(new_id):
    answer = ''
    id_len = len(new_id)
    '''
    if id_len == 0:
        new_id = 'aaa'
    else:
        while new_id[-1] == '.':
            new_id = new_id[:-1]
            if len(new_id) == 0:
                new_id = ''
                break;
        new_id = new_id[::-1]
        while new_id[-1] == '.':
            new_id = new_id[:-1]
            if len(new_id) == 0:
                new_id = ''
                break;
        new_id = new_id[::-1]
    '''    
    check_dot = False    
    for w in new_id:
        if w.isalpha():
            w = w.lower()
        if w.isalpha() or w in ['0','1','2','3','4','5','6','7','8','9', '-','_','.']:
            if w == '.':
                if check_dot == False:
                    answer = answer + w
            else:
                answer = answer + w
            if w == '.':
                check_dot = True
            else:
                check_dot = False;
                

    if len(answer) >= 1:
        while answer[-1] == '.':
            answer = answer[:-1]
            if len(answer) == 0:
                answer = 'aaa'
                break;
        answer = answer[::-1]
        while answer[-1] == '.':
            answer = answer[:-1]
            if len(answer) == 0:
                answer = 'aaa'
                break;
        answer = answer[::-1]   
    
    id_len = len(answer)
    if id_len >= 16:
        answer = answer[:15]
    
    while answer[-1] == '.':
        answer = answer[:-1]
        if len(answer) == 0:
            answer = 'aaa'
            break;
    
        
    if len(answer) == 0:
        answer = 'aaa'

    while len(answer) <= 2:
        answer = answer + answer[-1]
                
    return answer