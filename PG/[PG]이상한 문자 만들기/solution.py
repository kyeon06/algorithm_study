1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
def solution(s):
    result = []

    words = s.split(' ')

    for word in words:
        changed = ''
        for idx in range(len(word)):
            if idx % 2 == 0:
                changed += word[idx].upper()
            else:
                changed += word[idx].lower()

        result.append(changed)

    return ' '.join(result)