def solution(dirs):
    answer = 0
    
    move = {"U" : [0,1], "D" : [0,-1], "R" : [1,0], "L" : [-1,0]}
    first = [0,0]
    second = [0,0]
    chk = []
    
    for d in dirs:
        # 이동한 위치 설정
        second[0] += move[d][0]
        second[1] += move[d][1]
        
        if second[0] > 5 or second[0] < -5 or second[1] > 5 or second[1] < -5:
            second[0] -= move[d][0]
            second[1] -= move[d][1]
            continue

        tmp = first + second
        tmp2 = second + first
        if tmp in chk:
            first = second.copy()
            continue
        else:
            # 이동 전 위치 + 이동한 위치 저장
            chk.append(tmp)
            chk.append(tmp2)

        # 현재 위치 변경
        first = second.copy()
        answer += 1        

    return answer