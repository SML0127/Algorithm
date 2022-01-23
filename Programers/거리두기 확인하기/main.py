def move(a, b, x, y, cnt, place, is_success):
    if cnt >= 2:
        return;
    if x-1 >= 0:
        if place[x-1][y] == 'O':
            move(a, b, x-1, y, cnt + 1, place, is_success) 
        elif place[x-1][y] == 'P' and (x-1 != a or y != b):
            is_success[0] *= 0
            return;
    if x+1 < 5:
        if place[x+1][y] == 'O':
            move(a, b, x+1, y, cnt + 1, place, is_success)
        elif place[x+1][y] == 'P' and (x+1 != a or y != b):
            is_success[0] *= 0
            return;
    if y-1 >= 0:
        if place[x][y-1] == 'O':
            move(a, b, x, y-1, cnt + 1, place, is_success)
        elif place[x][y-1] == 'P' and (x != a or y-1 != b):
            is_success[0] *= 0
            return;
    if y+1 < 5 :
        if place[x][y+1] == 'O':
            move(a, b, x, y+1, cnt + 1, place, is_success)
        elif place[x][y+1] == 'P' and (x!= a or y+1 != b):
            is_success[0] *= 0
            return;
def check_p(x, y, place, is_success):
    move(x, y, x, y, 0, place, is_success)
    if is_success == [1]:
        return True
    else:
        return False
    
def check(place):
    for row, val1 in enumerate(place):
        for col, val2 in enumerate(val1):
            if val2 == 'P':
                is_success = [1]
                res = check_p(row, col, place, is_success)
                
                if res == False:
                    return 0
    return 1

def solution(places):
    answer = []
    for place in places:
        answer.append(check(place)) 

    return answer