#참고 - https://velog.io/@bjo6300/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%91%98%EB%A7%8C%EC%9D%98-%EC%95%94%ED%98%B8

def solution(s, skip, index):
    answer = ''
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    
    for sk in skip:
        # skip 알파벳 제거
        alpha = alpha.replace(sk, "")
    
    for i in s:
        change = alpha[(alpha.index(i) + index) % len(alpha)]
        answer += change
    return answer