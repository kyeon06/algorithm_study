"""
set 자료형
1. 교집합
s1 & s2
s1.intersection(s2)

2. 합집합
s1 | s2
s1.union(s2)

3. 차집합
s1 - s2
s1.difference(s2)

4. 공통된 부분이 하나도 없다.
s1.isdisjoint(s2)
"""

def solution(spell, dic):
    answer = 2
    spell = set(spell)
    
    for word in dic:
        if len(spell - set(word)) == 0:
            answer = 1
    return answer