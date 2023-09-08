from collections import deque
def solution(priorities, location):

    q = deque(priorities)
    answer = 0

    while q:
        m = max(q)
        p = q.popleft()
        location -= 1
        if p != m:
            q.append(p)
            if location < 0:
                location = len(q) -1
        else:
            answer += 1
            if location < 0:
                break
    return answer

        

print(solution([2, 1, 3, 2], 2))

# https://velog.io/@naro-kim/%EC%8A%A4%ED%83%9D%ED%81%90-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%94%84%EB%A1%9C%EC%84%B8%EC%8A%A4-%ED%8C%8C%EC%9D%B4%EC%8D%AC