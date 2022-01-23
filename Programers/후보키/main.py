from itertools import combinations
def solution(relation):
    answer = 0
    relation_t = []
    tmp_list = []
    for c in range(0,len(relation[0])):
        for r in range(0, len(relation)):
            tmp_list.append(relation[r][c])
        relation_t.append(tmp_list)
        tmp_list = []
    comb_list = []
    
    for i in range(1, len(relation_t) + 1):
        comb_list += list(combinations(range(len(relation_t)), i))
    
    combi= []
    for candi_comb in comb_list: # (0,1)
        # comb_list가 이미 후보키에 있는지
        check = False
        for key in combi: #[1] , [2,3]
            print(key, candi_comb)
            print(set(key).issubset(candi_comb))
            if set(key).issubset(candi_comb): # [2,3,4]
                check = True
                break;
        if check == True and len(combi) != 0:
            continue
            
        # 없다면 후보키가 될 수 있는지
        print(candi_comb)
        candi_val = []

        for row in relation:
            candi_val1 = ()
            for val in candi_comb: # [1,2,3]
                candi_val1 += (row[val],)
            candi_val.append(candi_val1)
        #print(candi_val)
        if len(candi_val) == len(set(candi_val)):
            combi.append(candi_comb)
        #print('------------------')
        #print(combi)

    #print(combi)
    answer = len(combi)
    return answer