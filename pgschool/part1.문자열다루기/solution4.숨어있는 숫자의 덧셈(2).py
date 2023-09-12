# 숨어 있는 숫자의 덧셈(2)

# 숨어있는 숫자의 덧셈(2)

"""
# isalpha() 사용
isalpha()는 대소문자 관계없이 알파벳인지를 판별하는 함수

# isdigit() : 숫자를 판별하는 함수
"""

def solution(my_string):
    for i in my_string:
        if i.isalpha():
            my_string = my_string.replace(i, ' ')
    
    return sum(list(map(int, my_string.split())))

    
