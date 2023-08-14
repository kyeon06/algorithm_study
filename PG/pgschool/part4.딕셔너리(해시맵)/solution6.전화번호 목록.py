# 전화번호 목록

def solution(phone_book):
    phone_book.sort()

    for p1, p2 in zip(phone_book, phone_book[1:]):

        if p2.startswith(p1):
            return False
        
    return True


# 해시를 이용한 풀이
# https://coding-grandpa.tistory.com/86
def solutionHash(phone_book):
    # 1. Hash map을 만든다
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    
    # 2. 접두어가 Hash map에 존재하는지 찾는다
    for phone_number in phone_book:
        jubdoo = ""
        for number in phone_number:
            jubdoo += number
            # 3. 접두어를 찾아야 한다 (기존 번호와 같은 경우 제외)
            if jubdoo in hash_map and jubdoo != phone_number:
                return False
    return True

print(solutionHash(["6", "12", "6789"]))