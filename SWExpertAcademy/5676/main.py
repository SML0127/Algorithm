

def find(rect, line):


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # -10,000 ~ 10,000
    line = input().split()
    rect = [(int(line[0]), int(line[1])),(int(line[0]), int(line[3])), (int(line[2]), int(line[1])), (int(line[2]), int(line[3]))]

    line = input().split()
    stright_line = [(int(line[0]), int(line[1])),(int(line[2]), int(line[3]))]
    num = 0

    num = find(rect, stright_line)

    print('#{} {}'.format(test_case, num))
    # ///////////////////////////////////////////////////////////////////////////////////
