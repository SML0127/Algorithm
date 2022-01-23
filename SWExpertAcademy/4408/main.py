T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
 
for test_case in range(1, T + 1):
    #N = 0
    N = int(input())

    board = [[int(val) for val in input().split()] for _ in range(N)]
    #print(board)

    # min # of bag
    #continue; 
    unique_bags = []; 
    
    for i in range(N):
        sr = board[i][0] # 10, 30 
        dt = board[i][1] # 20, 40
 
        if sr > dt:
            tmp = sr
            sr = dt
            dt = tmp 
        if len(unique_bags) == 0:
            unique_bags.append([[sr, dt]])
        else:
            is_new_bag = True;
            for bag in unique_bags: # [[(sr1, dt1), (sr2, dt2), (sr3, dt3)], []...]
                go_to_bag = True
                for ran in bag:
                    if (sr < ran[0] and dt < ran[0]):
                        if dt % 2 == 1 and dt + 1 == ran[0]:
                            go_to_bag = False;
                        else:
                            continue;
                    elif (sr > ran[1] and dt > ran[1]):
                        if sr % 2 == 1 and sr == ran[0] + 1:
                            go_to_bag = False;
                        else:
                            continue;
                    else:
                        go_to_bag = False;
                        break;
                if go_to_bag == True:
                    is_new_bag = False;
                    bag.append([sr, dt])
                    break;
                else: # check next bag
                    continue;
            if is_new_bag == True:
                unique_bags.append([[sr, dt]]) 
                
    result = len(unique_bags)
    print
    print("#{} {}".format(test_case, result))
    # ///////////////////////////////////////////////////////////////////////////////////
