from itertools import combinations
import re
def compress(s):
    tmp_list = []
    for w in s:
        str1 = ''
        for c in w:
            str1 +=c
        tmp_list.append(str1)
    return tmp_list

def solution(orders, course):
    answer = []
    for num in course:
        course_dic = {}
        check = ''
        for order in orders:
            order = "".join(sorted(order))
            check += order +' '
            tmp = compress(list(combinations(order, num)))
            for val in tmp: 
                if val not in course_dic:
                    course_dic[val] = 1
                else:
                    course_dic[val] += 1
        max_value = 0
        for key, value in course_dic.items():
            if value >= 2:
                if max_value < value:
                    max_value = value
        for key, value in course_dic.items():
            if value >= 2 and value == max_value:
                answer.append(key)
    answer = sorted(answer)
    print(answer)
    return answer