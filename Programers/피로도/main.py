from collections import deque
import copy
def solution(k, dungeons):
    answer = -1
    n = len(dungeons)
    remain_k = k
    q = deque()
    q.append([k, [], 0])
    
    while q:
        remain_k, visited, cnt = q.popleft()
        #print(remain_k, visited, cnt)
        for i in range(n):
            #is_visited = False
            if i not in visited:
                a = dungeons[i][0]
                b = dungeons[i][1]
                if remain_k >= a:
                    next_remain_k = remain_k - b
                    #is_visited = True
                    new_visited = copy.deepcopy(visited)
                    new_visited.append(i)
                    if answer < cnt + 1:
                        answer = cnt + 1
                    q.append([next_remain_k, new_visited, cnt+1])
    print(answer)
        
    return answer