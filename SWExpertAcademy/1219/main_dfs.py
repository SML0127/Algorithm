
import sys
from collections import deque
from copy import deepcopy
sys.stdin = open("1219/input.txt", "r")

def DFS(graph, visited, src, res):
    if res[0] == 1:
        return 1
    if src in graph:
        for dst in graph[src]:
            if dst == '99':
                res[0] = 1
            else:
                if dst in graph:
                    if visited[int(src)][int(dst)] == 0:
                        for val in graph[dst]:
                            new_visited = deepcopy(visited)
                            new_visited[int(src)][int(dst)] = 1
                            DFS(graph, new_visited, val, res)
                    
    return res[0]

        


T = 10

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for _ in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    test_case, num_edges = map(int, input().split())

    input_str = list(input().split())
    S, D = 0, 99
    visited = [[0 for _ in range(100)] for _ in range(100)]
    graph = {}
    result = 0


    for i in range(num_edges):
        if input_str[2*i] not in graph:
            graph[input_str[2*i]] = [input_str[2*i+1]] 
        else:
            graph[input_str[2*i]] = graph[input_str[2*i]] + [input_str[2*i+1]]

    #print(graph)
    res = [0]
    result = DFS(graph, visited, '0', res)
        
  
    print('#{} {}'.format(test_case, result))

    # ///////////////////////////////////////////////////////////////////////////////////
