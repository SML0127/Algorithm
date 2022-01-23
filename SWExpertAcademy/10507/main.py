import sys

sys.stdin = open("10507/input.txt", "r")
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    n, p = map(int, input().split()) # n, p <=200,000, n <= 1,000,000
    days = []
    visited = [False for _ in range(1000000)]

    for val in input().split():
        days.append(int(val))
        visited[int(val)-1] = True
  
    start, end, candidate_max = 0, 0, 0
    max_day = p + 1
    origin_p = p 
    cur_d_idx = -1
    while end <= days[-1] + origin_p:
        #print(end, days[-1] + origin_p, cur_d_idx)
        #print()
        if visited[end]: # 3 5 6 10 11 => F F T F F F T T F F F T T
            end += 1
            candidate_max += 1
            cur_d_idx += 1
            max_day = max(max_day, candidate_max)
        else:
            if p == 0:
                max_day = max(max_day, candidate_max)
                if visited[start] == False:
                    p += 1
                start += 1
                candidate_max -= 1
            else:
                p -= 1
                candidate_max += 1
                end += 1

        if p == 0 and cur_d_idx + 1 < len(days): 
            if days[cur_d_idx + 1] - days[cur_d_idx] >= max_day:
                start = days[cur_d_idx+1] - origin_p - 1 
                end = days[cur_d_idx+1] - origin_p - 1
                max_day = max(max_day, candidate_max)
                candidate_max = 0
                p = origin_p
                cur_d_idx = cur_d_idx + 1
    max_day = max(max_day, candidate_max)
        
    print('#{} {}'.format(test_case, max_day))
        


    # ///////////////////////////////////////////////////////////////////////////////////
