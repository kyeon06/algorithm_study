def solution(phone_number):
    n = len(phone_number) - 4
    hide = "*" * n
    return hide + phone_number[n:]