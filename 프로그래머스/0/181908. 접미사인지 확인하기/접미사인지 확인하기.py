def solution(my_string, is_suffix):
    lst = [my_string[i:] for i in range(len(my_string))]
    
    if is_suffix in lst:
        return 1
    return 0