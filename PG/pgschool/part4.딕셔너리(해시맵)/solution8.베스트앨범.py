# 베스트앨범

def solution(genres, plays):
    answer = []
    genre_play_sum = {}
    
    # ["장르", "재생수", "인덱스"] 리스트 만들기
    genre_play_info = [[g, p, i] for i, (g, p) in enumerate(zip(genres, plays))]
    genre_play_info = sorted(genre_play_info, key = lambda x: (x[0], -x[1], x[2]))
    
    # {"장르" : 총 재생횟수} dict 만들기
    for g, p in zip(genres, plays):
        if g not in genre_play_sum:
            genre_play_sum[g] = p
        else:
            genre_play_sum[g] += p
    
    genre_play_sum = sorted(genre_play_sum.items(), key=lambda item: -item[1])
    
    # 순서대로 앨범에 수록하기
    for item in genre_play_sum:
        cnt = 0
        for g, p, i in genre_play_info:
            if g == item[0]:
                answer.append(i)
                cnt += 1
                if cnt == 2:
                    break
    return answer