# 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
# 아래 표준 입출력 예제 필요시 참고하세요.

# 표준 입력 예제
'''
a = int(input())                        정수형 변수 1개 입력 받는 예제
b, c = map(int, input().split())        정수형 변수 2개 입력 받는 예제 
d = float(input())                      실수형 변수 1개 입력 받는 예제
e, f, g = map(float, input().split())   실수형 변수 3개 입력 받는 예제
h = input()                             문자열 변수 1개 입력 받는 예제
'''

# 표준 출력 예제
'''
a, b = 6, 3
c, d, e = 1.0, 2.5, 3.4
f = "ABC"
print(a)                                정수형 변수 1개 출력하는 예제
print(b, end = " ")                     줄바꿈 하지 않고 정수형 변수와 공백을 출력하는 예제
print(c, d, e)                          실수형 변수 3개 출력하는 예제
print(f)                                문자열 1개 출력하는 예제
'''

import sys


'''
      아래의 구문은 input.txt 를 read only 형식으로 연 후,
      앞으로 표준 입력(키보드) 대신 input.txt 파일로부터 읽어오겠다는 의미의 코드입니다.
      여러분이 작성한 코드를 테스트 할 때, 편의를 위해서 input.txt에 입력을 저장한 후,
      아래 구문을 이용하면 이후 입력을 수행할 때 표준 입력 대신 파일로부터 입력을 받아올 수 있습니다.

      따라서 테스트를 수행할 때에는 아래 주석을 지우고 이 구문을 사용하셔도 좋습니다.
      아래 구문을 사용하기 위해서는 import sys가 필요합니다.

      단, 채점을 위해 코드를 제출하실 때에는 반드시 아래 구문을 지우거나 주석 처리 하셔야 합니다.
'''
#sys.stdin = open("4112/input.txt", "r")
p_array = []
p_array.append((1, 1))
i, k = 1, 2
while True:

    prev_s, prev_d = p_array[-1][0], p_array[-1][1] 
    if prev_d + k > 10000:
        p_array.append((prev_s + i, prev_d + k))
        break;
    else:    
        p_array.append((prev_s + i, prev_d + k))
    i = i + 1
    k = k + 1

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''

    S, D = map(int, input().split()); # <= 10,000
    result = 0


    if S > D:
        tmp = S
        S = D
        D = tmp
    candi1 = S
    candi2 = S
    if S != D:
        idx_s, s_s, s_d = 0, 0, 0
        idx_d, d_s, d_d = 0, 0, 0
        # S를 D의 위치로 이동, 최소랑 최대 값 나오고 그 range에서 D랑 최소값 연산
        i , k = 1, 2
        check = False
        for idx, val in enumerate(p_array):
            if S >= val[0] and S <= val[1]:
                check = True
                idx_s = idx
                s_s, s_d = val[0], val[1]
            if D >= val[0] and D <= val[1]:
                idx_d = idx
                d_s, d_d = val[0], val[1]
                break;
            if check == True:
                candi1 = candi1 + i
                candi2 = candi2 + k
            i = i + 1
            k = k + 1
        #print(candi1, candi2)

        min_width = -1
        for i in range(candi1, candi2 +1):
            #print(D-i)
            if min_width ==  -1:
                min_width = abs(D- i)
            elif min_width > abs(D - i):
                min_width = abs(D- i)

        result = idx_d - idx_s + min_width
        
        
        width = 0
        result = result + width
    
    print("#{} {}".format(test_case, result))
    # ///////////////////////////////////////////////////////////////////////////////////
