import sys


sys.stdin = open("3459/input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////

    N = int(input())
    #               3*2       5*2                                               13 * 2     
    # 1 / 2 3 / 4 5 6 7 / 8 9 10 11 12 13 14 15 / 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 / 32
    # B  A1 A1 A A B B   B B   A A  A  A  A  A    A  A  A  A  A  A  A  A  A  A  B  B  B  B  B  B 
    #
    # 1 / 2 3 / 4 5 6 7 / (8 ~ 15)/ 8 ~ 29 / 
    # 1 -> 2 -> 4 5  ->  8  9 10 11  ->
    #      3 -> 6 7  -> 12 13 14 15  ->
    # N

    winner = 'Bob' # 'Alice'
    # 1 / 4 / 4 / 16 / 16 / 32 / 32
    # B 1 , 1+4 + 1 ~ 1+4 + 5
    # A 1 ~ 1+4

    i = 1
    idx = 1
    upper_bound = 1
    while True:
        #print(upper_bound,idx)
        if N <= upper_bound:
            if idx % 2 == 1:
                winner = 'Bob'
            else:
                winner = 'Alice'
            break
        else: 
            if idx % 2 == 1:
                i = i * 4
            upper_bound = upper_bound + i

            idx += 1
     


    print('#{} {}'.format(test_case, winner))
    # ///////////////////////////////////////////////////////////////////////////////////
