def solution(s):
    s_lst = list(s)


    first = s_lst[0]
    cnt_1 = 0
    cnt_2 = 0
    result = 0

    for i in range(len(s_lst)):

        # 첫 문자와 같을 경우
        if s_lst[i] == first:
            cnt_1 += 1
        # 첫 문자와 다를 경우
        elif s_lst[i] != first:
            cnt_2 += 1
        
        # 두 횟수 같아지면
        if cnt_1 == cnt_2:
            result += 1
            cnt_1 = 0
            cnt_2 = 0
            if i < len(s_lst)-1:
                first = s_lst[i+1]
        # 두 횟수가 다를 때 더이상 읽을 문자가 없을 경우
        elif cnt_1 != cnt_2 and i == len(s_lst)-1:
            result += 1

    return result



