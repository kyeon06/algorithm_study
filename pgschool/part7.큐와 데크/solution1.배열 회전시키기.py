from collections import deque

def solution(numbers, direction):

    dq = deque(numbers)

    if direction == "right":
        num = dq.pop()
        dq.appendleft(num)
    else:
        num = dq.popleft()
        dq.append(num)
    return list(dq)


print(solution([1,2,3], "right"))