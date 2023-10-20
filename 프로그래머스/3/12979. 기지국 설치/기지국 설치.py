import math

def solution(n, stations, w):
    answer = 0
    # 기지국이 안닿는 거리 구하기
    dist = []
    # 앞
    dist.append(stations[0]-w-1)
    # 중간
    for i in range(1, len(stations)):
        dist.append((stations[i]-w-1)-(stations[i-1]+w))
    # 뒤
    dist.append(n-(stations[-1]+w))
    
    cover = w * 2 + 1
    for d in dist:
        if d > 0:
            answer += math.ceil(d/cover)

    return answer