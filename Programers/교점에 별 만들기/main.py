def solution(line):
    answer = []
    answer_list = []
    for idx, li in enumerate(line):
        for i in range(idx + 1, len(line)):
            a = int(li[0])
            b = int(li[1])
            e = int(li[2])
            c = int(line[i][0])
            d = int(line[i][1])
            f = int(line[i][2])
            if a * d - b*c != 0:
                if ((b*f - e*d)/(a*d - b*c)).is_integer() and ((e*c - a*f)/(a*d - b*c)).is_integer():
                    answer_list.append([(b*f - e*d)/(a*d - b*c), (e*c - a*f)/(a*d - b*c)])
    #print(answer_list)
    #print(len(answer_list))
    if len(answer_list) == 0:
        answer = ['']
    elif len(answer_list) == 1:
        answer =['*']
    else:
        min_x = sorted(answer_list)[0][0]
        min_y = sorted(answer_list, key = lambda item: item[1])[0][1]
        max_x = sorted(answer_list, reverse= True)[0][0]
        max_y = sorted(answer_list, key = lambda item: item[1], reverse = True)[0][1]
        x_dis = abs(max_x - min_x)
        y_dis = abs(max_y - min_y)
        tmp = ''
        for i in range(int(x_dis) + 1):
            tmp += '.'
        answer = [tmp] * (int(y_dis) + 1)

        for li in answer_list:
            t1 = int(abs(li[1] - min_y))
            t2 = int(abs(li[0] - min_x))
            answer[t1] = answer[t1][:t2] + '*' + answer[t1][t2+1:]
            #answer[int(li[1] + abs(min_y))] = answer[int(li[1] + abs(min_y))][:int(li[0] + abs(min_x))] + '*' + answer[int(li[1] + abs(min_y))][int(li[0] + abs(min_x))+1:]
        #    print(answer[int(li[0] + abs(min_x))])
        answer = answer[::-1]
    
    return answer