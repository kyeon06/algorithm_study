def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        chk = bin(arr1[i] | arr2[i])
        chk = chk[2:].zfill(n)
        chk = chk.replace("1", "#").replace("0", " ")
        answer.append(chk)
    
    return answer
        
                
        