def solution(answers):
    s1 = [1,2,3,4,5]
    s2 = [2,1,2,3,2,4,2,5]
    s3 = [3,3,1,1,2,2,4,4,5,5]

    c1, c2, c3 = 0, 0, 0

    for i in range(len(answers)):
        a1 = i % 5
        a2 = i % 8
        a3 = i % 10
        
        if s1[a1] == answers[i]:
            c1 += 1
        
        if s2[a2] == answers[i]:
            c2 += 1
        
        if s3[a3] == answers[i]:
            c3 += 1
        
    max_ = max( c1, c2, c3)
    result = []
    if max_ == c1:
        result.append(1)
    if max_ == c2:
        result.append(2)
    if max_ == c3:
        result.append(3)
    
    return result

print(solution([1,2,3,4,5]))