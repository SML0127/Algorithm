# 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
# 아래 표준 입출력 예제 필요시 참고하세요.
import sys

sys.stdin = open("1245/input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    N = int(input())
    x_axis = list(int(val) for val in input().split())
    board = []
    #res = ' '

    for idx, val in enumerate(x_axis):
        if idx >= len(x_axis) / 2:
            break;
        # 0 1 2 3, 0 
        board.append((x_axis[idx], x_axis[int(len(x_axis)/2) + idx])) 

    result = []
    


    for i in range(len(board)):
        if i == len(board) - 1:
            break;
        delta = (board[i+1][0] - board[i][0]) / 2  
        delta2 = delta/2

        d1 = board[i][0]
        is_find = False;
        prev = 0
        while True:
            F1 = 0

            for i0 in range(0, i+1):
                d2 = board[i0][0]
                m2 = board[i0][1]
                if i0 == i:
                    F1 = F1 + ( m2  / ((delta) *  (delta)))
                else:

                    F1 = F1 + ( m2  / ((float(d1) - float(d2) +float(delta)) * (float(d1) - float(d2) + float(delta))))

 
            for i2 in range(i +1, len(board)):
                d2 = board[i2][0]
                m2 = board[i2][1]
                F1 = F1 - (m2  / ((d2 - d1 - delta) *  (d2 - d1- delta))) 
            if prev != 0:
                if prev - (board[i][0] + delta) <= 0.000000000001 and  prev - (board[i][0] + delta) >= -0.000000000001 :
                    is_find = True;

            if is_find == True:
                result.append(board[i][0] + delta)
                break;
            prev = board[i][0] + delta

            if F1 > 0:
                delta = delta + delta2
                delta2 = delta2/2
            elif F1 < 0:
                delta = delta - delta2
                delta2 = delta2/2 
            

            


    res = ''
    for val in result:
        res = res + ' ' + '{:.10f}'.format(val)
    print('#{}{}'.format(test_case, res))
        


    # ///////////////////////////////////////////////////////////////////////////////////
