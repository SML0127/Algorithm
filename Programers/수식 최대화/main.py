import re
def solution(expression):
    answer = 0
    num_list = re.findall('\d+', expression)
    op_list = re.findall('\+|\-|\*', expression)
    cp_num_list = num_list
    cp_op_list = op_list
    process_set = [[0,1,2],[0,2,1],[1,0,2],[1,2,0],[2,0,1],[2,1,0]]
    # 0 = *, 1 = +, 2 = -
    cur_max = -9999999
    for order in process_set:
        cp_num_list = list(map(int, num_list))
        cp_op_list = op_list
        for op in order:
            if op == 0: # *
                for idx, op1 in enumerate(cp_op_list):
                    if op1 == '*':
                        cp_num_list[idx + 1] = cp_num_list[idx] * cp_num_list[idx+1]
                        cp_num_list[idx] = ''
                tmp_op_list, tmp_num_list = [], []
                for val in cp_op_list:
                    if val != '*':
                        tmp_op_list.append(val)
                for val in cp_num_list:
                    if val != '':
                        tmp_num_list.append(val)
                cp_op_list, cp_num_list = tmp_op_list, tmp_num_list
            elif op == 1: # +
                for idx, op1 in enumerate(cp_op_list):
                    if op1 == '+':
                        cp_num_list[idx + 1] = cp_num_list[idx] + cp_num_list[idx+1]
                        cp_num_list[idx] = ''
                tmp_op_list, tmp_num_list = [], []
                for val in cp_op_list:
                    if val != '+':
                        tmp_op_list.append(val)
                for val in cp_num_list:
                    if val != '':
                        tmp_num_list.append(val)
                cp_op_list, cp_num_list = tmp_op_list, tmp_num_list           
            elif op == 2: # -
                for idx, op1 in enumerate(cp_op_list):
                    if op1 == '-':
                        cp_num_list[idx + 1] = cp_num_list[idx] - cp_num_list[idx+1]
                        cp_num_list[idx] = ''
                tmp_op_list, tmp_num_list = [], []
                for val in cp_op_list:
                    if val != '-':
                        tmp_op_list.append(val)
                for val in cp_num_list:
                    if val != '':
                        tmp_num_list.append(val)
                cp_op_list, cp_num_list = tmp_op_list, tmp_num_list
        if cur_max < abs(cp_num_list[0]):
            cur_max = abs(cp_num_list[0])
    answer = cur_max
    return answer