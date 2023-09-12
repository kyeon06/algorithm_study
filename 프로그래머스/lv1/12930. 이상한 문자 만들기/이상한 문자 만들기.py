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