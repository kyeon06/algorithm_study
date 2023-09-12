from math import ceil
from collections import deque

def solution(progresses, speeds):
    days = []
    answer = []

    for p, s in zip(progresses, speeds):
        days.append(ceil((100-p)/s))

    dq = deque(days)
    cnt = 1
    start = dq.popleft()

    while True:

        nxt = dq.popleft()

        if nxt <= start:
            cnt += 1
        else:
            answer.append(cnt)
            start = nxt
            cnt = 1
        
        if len(dq) == 0:
            answer.append(cnt)
            break

    return answer

print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))