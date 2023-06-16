# 문자열 계산하기

def solution(my_string):
    my_string_list = my_string.split()

    for idx in range(0,len(my_string_list),2):
        my_string_list[idx] = int(my_string_list[idx])
    
    result = my_string_list[0]
    for value in range(1, len(my_string_list)-1):
        if my_string_list[value] == "+":
            result += my_string_list[value+1]
        elif my_string_list[value] == "-":
            result -= my_string_list[value+1]

    return result