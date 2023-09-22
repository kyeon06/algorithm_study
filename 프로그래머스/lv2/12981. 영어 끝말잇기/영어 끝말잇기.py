def solution(n, words):
    answer = []
    chk = []
    
    for w in range(len(words)):
        if chk:
            if chk[-1][-1] == words[w][0] and words[w] not in chk:
                chk.append(words[w])
            else:
                no = w % n + 1
                turn = w // n + 1
                return [no, turn]
        else:
            chk.append(words[w])
    
    return [0,0]