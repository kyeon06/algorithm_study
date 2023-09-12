def solution(X, Y):
    X = [int(x) for x in X]
    Y = [int(y) for y in Y]
    
    setNum = set(X)

    x_dict = { n:X.count(n) for n in setNum }
    print(x_dict)
    y_dict = { n:Y.count(n) for n in setNum }
    print(y_dict)


    result = []
    for n in setNum:
        for i in range(min(x_dict[n], y_dict[n])):
             result.append(n)
    

    if sum(result) == 0 and len(result) > 0:
        return "0"
    elif sum(result) == 0 and len(result) == 0:
        return "-1"
    else:
        result = [str(n) for n in result]
        return "".join(sorted(result, reverse=True))