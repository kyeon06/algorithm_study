def solution(array, commands):
    result = [sorted(array[k[0]-1:k[1]])[k[2]-1] for k in commands]    
    return result