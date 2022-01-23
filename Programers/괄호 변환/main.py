import re
def check_valid(p):
    check = 0
    for wd in p:
        if wd == '(':
            check += 1
        elif wd == ')':
            check -= 1
        if check < 0:
            return False
    return True

def decompse(cp_p):
    u, v = '', ''
    for i in range(1, len(cp_p)+1):
        num_b_l = len(re.findall('\(',cp_p[:i]))
        num_b_r = len(re.findall('\)',cp_p[:i]))
        if num_b_l == num_b_r:
            u = cp_p[:i]
            v = cp_p[i:]
            break;
    return u, v

def func(cp_p):
    answer_list = []
    if cp_p == '':
        return ''
    u, v = decompse(cp_p)
    tmp_string = ''
    print('func:', u, v)
    if check_valid(u) == True:
        answer_list.append(u)
        cp_p = v
        v = func(cp_p)
        res = ''
        for char in answer_list:
            res += char
        print('38', res, v)
        return res + v
    else:
        tmp_string = '('
        v = func(v)
        tmp_string += v + ')'
        print('43', tmp_string)
        u = u[1:-1].replace('(','-').replace(')','+').replace('-',')').replace('+','(')
        tmp_string += u
        print('45', tmp_string)
        return tmp_string
    return ''

def solution(p):
    answer = ''
    tmp_string = ''
    if p == '':
        answer = p
    else:
        cp_p = p
        res = func(cp_p)
        #print('anw: ', answer_list)
        #for char in answer_list:
        #    answer += char
        answer += res

    return answer