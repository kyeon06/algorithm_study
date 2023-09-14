def solution(brown, yellow):
    answer = []
    
    for a in range(brown//2, 0, -1):
        for b in range(1, a+1):
            if (a * b) == (brown + yellow):
                if (a-2) + (b-2) == (brown - 4) // 2:
                    answer.append(a)
                    answer.append(b)
    return answer