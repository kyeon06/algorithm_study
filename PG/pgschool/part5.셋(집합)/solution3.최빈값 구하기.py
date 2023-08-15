def solution(array):
    
    maxNum = max(array) + 1
    chk = [0] * maxNum 
    
    for num in array:
        chk[num] += 1
    
    modCnt = 0
    answer = 0
    for i in range(len(chk)):
        if chk[i] == max(chk):
            modCnt +=1
            answer = i
    
    if modCnt > 1:
        answer = -1
    
    return answer

# 좀 더 간단한 풀이
def solution(array):
	count = [0] * (max(array)+1) # 숫자 출연 횟수를 셀 리스트

	for i in array:
		count[i] += 1

	m = 0 # 최빈값의 개수
	for c in count:
		if c == max(count):
			m += 1
    
	if m > 1: # 최빈값이 2개 이상이면 -1을 리턴
		return -1
	else: # 최빈값이 1개이면 해당 숫자를 리턴
		return count.index(max(count))