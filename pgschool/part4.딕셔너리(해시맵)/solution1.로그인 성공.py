# 로그인 성공
# https://school.programmers.co.kr/tryouts/85912/challenges?language=python3

def solution(id_pw, db):
    db_dict = dict(db)
    answer = ""
    
    # 아이디가 있는지 확인
    if id_pw[0] in db_dict:
        # 비밀번호 확인
        if id_pw[1] == db_dict[id_pw[0]]:
            answer = "login"
        else: answer = "wrong pw"
    else:
        answer = "fail"
    return answer