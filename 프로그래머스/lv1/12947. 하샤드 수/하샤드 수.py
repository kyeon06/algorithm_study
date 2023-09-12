def solution(x):
    lst = list(map(int, list(str(x))))
    if x % sum(lst) == 0:
        return True
    else:
        return False