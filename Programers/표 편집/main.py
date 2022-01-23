class Node:
    def __init__(self):
        self.removed = False
        self.up = None
        self.down = None
        
def solution(n,k,command):
    answer = ''
    nodeArr = [Node() for _ in range(n)]
    for i in range(1, n):
        nodeArr[i-1].down = nodeArr[i]
        nodeArr[i].up = nodeArr[i-1]
    curNode = nodeArr[k]
    deleted = []
    for cmd in command:
        if 'D' in cmd:
            mv = int(cmd.split()[1])
            for _ in range(mv):
                curNode = curNode.down
        elif 'U' in cmd:
            mv = int(cmd.split()[1])
            for _ in range(mv):
                curNode = curNode.up
        elif 'C' in cmd:
            deleted.append(curNode)
            curNode.removed = True
            up = curNode.up
            down = curNode.down
            if up:
                up.down = down
            if down:
                down.up = up
                curNode = down
            else:
                curNode = up

        elif 'Z' in cmd:

            backup_node = deleted.pop()
            backup_node.removed = False
            up = backup_node.up
            down = backup_node.down
            if up:
                up.down = backup_node
            if down:
                down.up = backup_node
    for node in nodeArr:
        if node.removed == True:
            answer+='X'
        else:
            answer+='O'
    return answer


def solution1(n, k, command):
    answer = ''
    deleted = []
    input_list = ['O' for i in range(n)]
    for cmd in command:
        if 'D' in cmd:
            mv = int(cmd.split()[1])
            cnt = 0
            while True:
                jump = input_list[k+1: k+mv+1].count('X')     
                k += mv
                if jump == 0:
                    break;
                mv = jump
            if k > n:
                k = n - 1
        elif 'U' in cmd:
            mv = int(cmd.split()[1])
            cnt = 0
            while True:
                jump = input_list[k-mv: k].count('X')
                k -= mv
                if jump == 0:
                    break;
                mv = jump
            if k < 0: 
                k = 0
        elif 'C' in cmd:
            deleted.append(k)
            input_list[k] = 'X'
            if k == n-1:
                k -= 1
                while True:
                    jump = input_list[k-mv: k].count('X')
                    k -= mv
                    if jump == 0:
                        break;
                    mv = jump

            else:
                check = False
                while True:
                    k += 1
                    if k not in deleted:
                        break;
                    if k == n-1 and k in deleted:
                        check = True
                        break;
                while check:
                    k -= 1
                    if k not in deleted:
                        break;
                    if k <= 0:
                        break;
        elif 'Z' in cmd:
            if len(deleted) >= 0:
                input_list[deleted[-1]] = 'O'
                deleted = deleted[:-1]
        #print(k, input_list)
    answer = "".join(input_list)
    return answer