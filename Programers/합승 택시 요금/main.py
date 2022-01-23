def solution1(n, s, a, b, fares):
    d = [ [ 20000001 for _ in range(n) ] for _ in range(n) ]
    for x in range(n):
        d[x][x] = 0
    for x, y, c in fares:
        d[x-1][y-1] = c
        d[y-1][x-1] = c

    for i in range(n):
        for j in range(n):
            for k in range(n):
                if d[j][k] > d[j][i] + d[i][k]:
                    d[j][k] = d[j][i] + d[i][k]

    minv = 40000002
    for i in range(n):
        minv = min(minv, d[s-1][i]+d[i][a-1]+d[i][b-1])
    return minv

def solution(n, s, a, b, fares):
    answer = 0
    s = s-1
    a = a-1
    b = b-1

    global_cost = [[999999999 for _ in range(n)] for _ in range(n)]
    for row in fares:
        global_cost[row[0]-1][row[1]-1] = row[2]
        global_cost[row[1]-1][row[0]-1] = row[2]
    for i in range(n):
        global_cost[i][i] = 0
        
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i == 0 and j == 3:
                    print(global_cost[i][k], global_cost[k][j])
                if global_cost[i][j] > global_cost[i][k] + global_cost[k][j]:
                    global_cost[i][j] = global_cost[i][k] + global_cost[k][j] 
    print(global_cost)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i == 0 and j == 3:
                    print(global_cost[i][k], global_cost[k][j])
                if global_cost[i][j] > global_cost[i][k] + global_cost[k][j]:
                    global_cost[i][j] = global_cost[i][k] + global_cost[k][j]
    print(global_cost)
    global_min = 999999999999
    for i in range(n):
        global_min = min(global_min, global_cost[s][i] + global_cost[i][a] + global_cost[i][b])
    answer= global_min 
    
    
    return answer