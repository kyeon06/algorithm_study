def solution(s, n):
    chars = list(s)
    for code in range(len(chars)):  

        if ord(chars[code]) >= ord('A') and ord(chars[code]) <= ord('Z'):
            if (ord(chars[code]) + n) > ord('Z'):
                chars[code] = chr(ord(chars[code]) + n - ord('Z') + ord('A') - 1)
            else:
                chars[code] = chr(ord(chars[code]) + n)
        elif ord(chars[code]) >= ord('a') and ord(chars[code]) <= ord('z'):
            if (ord(chars[code]) + n) > ord('z'):
                chars[code] = chr(ord(chars[code]) + n - ord('z') + ord('a') - 1)
            else:
                chars[code] = chr(ord(chars[code]) + n)

    return "".join(chars)