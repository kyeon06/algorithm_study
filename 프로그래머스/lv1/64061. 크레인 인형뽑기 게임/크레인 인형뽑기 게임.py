def solution(board, moves):
    s = []
    cnt = 0

    for move in moves:
        for line in board:
            if line[move-1] > 0:
                if line[move-1] in s[-1:]:
                    s.pop()
                    cnt += 2
                else:
                    s.append(line[move-1])
            # 인형 뽑은 후 빈칸으로 만들어주고 다음 무브로 이동        
                line[move-1] = 0
                break
    return cnt