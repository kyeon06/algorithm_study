def solution(arr1, arr2):
    
    lst = []
    for a, b in zip(arr1, arr2):
        tmp = [a[i]+b[i] for i in range(len(a))]
        lst.append(tmp)
        
    return lst
        
        