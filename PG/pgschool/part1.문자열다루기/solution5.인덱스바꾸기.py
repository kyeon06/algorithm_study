def solution(my_string, num1, num2):

    lst = list(my_string)
    tmp = ""
    tmp = lst[num1]
    lst[num1] = lst[num2]
    lst[num2] = tmp

    return ''.join(lst)



my_string = "hello"
solution(my_string, 1,2)