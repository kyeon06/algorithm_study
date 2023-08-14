# 완주하지 못한 선수

# 정렬
def solution(participant, completion):

    participant.sort()
    completion.sort()
    
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    
    return participant[len(participant)-1]

# Hash 사용
def solution1(participant, completion):
    hashDict = {}
    sumHash = 0

    # participant dict 만들고 sum(hash) 구하기
    for part in participant:
        hashDict[hash(part)] = part
        sumHash += hash(part)
    
    # completion의 sum(hash) 빼기
    for com in completion:
        sumHash -= hash(com)
    
    return hashDict[sumHash]
    

print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))