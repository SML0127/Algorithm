T = int(input())

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())
        
    lands_x = list(map(int, input().split()))
    lands_y = list(map(int, input().split()))
    visited = [0]
    not_visited = [int(val) for val in range(1, N)]
    E = float(input())
    cost = 0
    while True:
        if len(visited) == N:
            break;
        cur_min = 9999999999999
        cur_idx = -1
        for idx in visited:
            for i in not_visited:
                distance = E * (pow(lands_x[idx] -lands_x[i], 2) + pow(lands_y[idx] -lands_y[i], 2))
                if cur_min > distance:
                    cur_min = distance
                    cur_idx = i
        not_visited.remove(cur_idx)
        visited.append(cur_idx)
        cost += cur_min
    
    print('#{} {}'.format(test_case, round(cost)))
    # ///////////////////////////////////////////////////////////////////////////////////
