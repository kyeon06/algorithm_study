def solution(n, m):
    # 두개의 숫자를 리스트에 넣어준다.
    lst = [n, m]
    
    #결과값을 담을 빈 배열 생성
    result = []
    
    #최대공약수
    # i는 두개의 숫자 중 가장 작은 값에 1을 더한만큼 반복한다.
    for i in range(1, min(lst)+1):
        # 두개의 숫자를 i로 나눴을 경우 나머지가 0이면 공약수로 판단해서 max_에 업데이트 해준다.
        if max(lst) % i == 0 and min(lst) % i == 0:
            max_ = i
            
    # 마지막으로 나눈 공약수를 최대공약수라고 보고 result에 넣어준다.
    result.append(max_)
    
    
    #최소공배수
    # 두 수 중에 큰 값을 작은 값으로 나눴을 때 나머지가 0이면 result에 큰 수를 넣어준다.
    if max(lst)%min(lst) == 0:
        result.append(max(lst))
    # 두 수 중에 큰 값을 최대 공약수로 나눴을 때 나머지가 0이면 아래와 같이 계산해 result에 넣어준다.
    elif max(lst)%max_ == 0:
        result.append(min(lst)*(max(lst)//max_))
    # 위의 두 경우가 아닌 경우 큰수와 작은수를 곱하여 result에 넣어준다.
    else:
        result.append(n*m)
        
    return result
