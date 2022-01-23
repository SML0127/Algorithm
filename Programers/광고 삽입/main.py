def solution(play_time, adv_time, logs):
    answer = ''
    # sec 

    play_time_sec = 0
    for idx, value in enumerate(play_time.split(':')):
        if idx == 0:
            play_time_sec += 3600 * int(value)
        elif idx == 1:
            play_time_sec += 60 * int(value)
        else:
            play_time_sec += int(value)
            
    t_count = [0] * (play_time_sec + 1)
    start_list = []
    finish_list = []
    if play_time == adv_time:
        return '00:00:00'
    for log in logs:
        s_time, f_time = 0, 0
        for idx, value in enumerate(log.split('-')[0].split(':')):
            if idx == 0:
                s_time += 3600 * int(value)
            elif idx == 1:
                s_time += 60 * int(value)
            else:
                s_time += int(value)
        start_list.append(s_time)
        for idx, value in enumerate(log.split('-')[1].split(':')):
            if idx == 0:
                f_time += 3600 * int(value)
            elif idx == 1:
                f_time += 60 * int(value)
            else:
                f_time += int(value)
        finish_list.append(f_time)
        t_count[s_time] += 1
        t_count[f_time] -= 1
        
    adv_time_sec = 0
    for idx, value in enumerate(adv_time.split(':')):
        if idx == 0:
            adv_time_sec += 3600 * int(value)
        elif idx == 1:
            adv_time_sec += 60 * int(value)
        else:
            adv_time_sec += int(value)
            
    candi = {}
    f_time1 = sorted(finish_list, reverse=True)[0]

    for i in range(1, play_time_sec):
        t_count[i] += t_count[i-1]

    
    default_val = 0
    for i in range(adv_time_sec+1):
        default_val += t_count[i]
    print(default_val)
    candi_val = default_val
    new_answer = 0
    for i in range(0, play_time_sec - adv_time_sec + 1):
        default_val -= t_count[i]
        default_val += t_count[i + adv_time_sec]
        if default_val > candi_val:
            candi_val = default_val
            new_answer = i+1
    
    answer += str(new_answer // 3600).zfill(2) + ':' + str(new_answer % 3600 // 60).zfill(2) + ':'+ str(new_answer % 3600 % 60).zfill(2)
    
    return answer