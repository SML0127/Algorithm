def solution(numbers, hand):
    answer = ''
    cur_l, cur_r = 10, 12
    for val in numbers:
        print(val, cur_l, cur_r)
        val = int(val)
        if int(val) in [1, 4, 7]:
            answer += 'L'
            cur_l = int(val)
        elif int(val) in [3, 6, 9]:
            answer += 'R'
            cur_r = int(val)
        else:
            if int(val) == 0:
                val = 11
            len_l = (abs(((val-1) //3) - (cur_l-1)//3)) + abs((val -1)%3 - (cur_l-1)%3)
            len_r = (abs((val-1) //3 - (cur_r-1)//3)) + abs((val-1)%3 - (cur_r-1)%3)  
            print(len_l, len_r)
            if len_r < len_l:
                answer += 'R'
                cur_r = int(val)
            elif len_r > len_l:
                answer += 'L'
                cur_l = int(val)
            else:
                if hand == 'right':
                    answer += 'R'
                    cur_r = int(val)
                else:
                    answer += 'L'
                    cur_l = int(val)   
    return answer