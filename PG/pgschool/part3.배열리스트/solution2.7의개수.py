def solution(array):
    my_str = ''
    for a in array:
        my_str += str(a)
    return my_str.count('7')