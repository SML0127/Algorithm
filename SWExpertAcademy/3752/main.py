from collections import deque



T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.
        2, 3, 5 => 7 (0, 2, 3, 5, 7, 8, 10)
        0점 + # of unique  + (2, N)개에 대해 조합
    '''
    N = int(input())
    score_board = [int(val) for val in input().split()]; # [2, 3, 5], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    score_set = set([])
    score_list = []
    score_set.add(0)

    for val in score_board:
        #   map(연산 or cast, list or set) => list
        score_set = score_set.union(set(map(lambda x: x+ val, score_set)))
        #for val1 in score_set:
        #    score_list.append(val + val1)
        #    score_list.append(val + 0)
        #score_set = set(score_list)

 



    result = len(score_set)
    print('#{} {}'.format(test_case, result))
    # ///////////////////////////////////////////////////////////////////////////////////
