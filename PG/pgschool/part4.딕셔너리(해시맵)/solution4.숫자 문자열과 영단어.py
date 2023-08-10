# 숫자 문자열과 영단어
# https://school.programmers.co.kr/tryouts/85915/challenges

def solution(s):
    word = {
        "zero" : "0",
        "one" : "1",
        "two" : "2",
        "three" : "3",
        "four" : "4",
        "five" : "5",
        "six" : "6",
        "seven" : "7",
        "eight" : "8",
        "nine" : "9",
    }
    
    for eng, num in word.items():
        s = s.replace(eng, num)
    
    return int(s)