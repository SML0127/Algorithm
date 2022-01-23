def solution(board, moves):
    answer = 0
    height = len(board)
    box = []
    for mv in moves:
        mv = mv - 1
        for h in range(0, height):
            if board[h][mv] != 0:
                id = board[h][mv]
                box.append(id)
                board[h][mv] = 0
                break;
    check = True
    while check:
        check = False
        for idx, val in enumerate(box):
            if idx >= 1:
                if pre_val == val and val != 0:
                    box[idx] = 0
                    box[idx-1] = 0
                    answer += 2
                    val = 0
                    check = True
            pre_val = val
        new_box = []
        for idx, val in enumerate(box):
            if val != 0:
                new_box.append(val)
        box = new_box
    return answer