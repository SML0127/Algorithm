def find(results, table, idx, r, c, result):
    result += table[4*r+c]
    if idx == 6:
        results.add(result)
    else:
        # go down
        if r > 0: # row > 0 => up
            find(results, table, idx+1, r-1, c, result)
        if r < 3: # row < 3 => down
            find(results, table, idx+1, r+1, c, result)
        if c > 0: # col > 0 => left
            find(results, table, idx+1, r, c-1, result)
        if c < 3: # col < 3 => right
            find(results, table, idx+1, r, c+1, result)

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    table = str(input()).split() + str(input()).split() + str(input()).split() + str(input()).split()
    results = set([])

    for i in range(0,4):
        for j in range(0,4):
            result = ''
            find(results, table, 0, i, j, result)
    print(results)
    print('#{} {}'.format(test_case, len(results)))