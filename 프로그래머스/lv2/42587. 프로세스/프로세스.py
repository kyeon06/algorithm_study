def solution(priorities, location):
    lst = []
    cnt = 0
    for k, v in enumerate(priorities):
        lst.append((k,v))
    
    while True:
        J = lst.pop(0)
        for n in lst:
            if J[1] < n[1]:
                lst.append(J)
                break
        else:
            cnt += 1
            if J[0] == location:
                return cnt