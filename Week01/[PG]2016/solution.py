#시작시간 : 1시 4분
#종료시간 : 1시 46분

# 1,3,5,7,8,10,12월은 31일
# 2월은 29일 , 4,6,9,11월은 30일

month, day = map(int, input().split())
yoil = ['SUN','MON','TUE','WED','THU','FRI','SAT']
start = yoil.index('FRI')

def solution(month, day):
    for m in range(1, month):
        if m == 1:
            end = (start + 31) % 7
        elif m == 2:
            end = (end + 29) % 7
        elif m in [3,5,7,8,10,12]:
            end = (end + 31) % 7
        elif m in [4,6,9,11]:
            end = (end + 30) % 7

    if month == 1:
        result = (start+day) % 7 - 1
        result_yoil = yoil[result]
    else:
        result = (end + day) % 7 - 1
        result_yoil = yoil[result]

    return result_yoil


print(solution(month,day))


# 프로그래머스 제출용
# def solution(a, b):
#     yoil = ['SUN','MON','TUE','WED','THU','FRI','SAT']
#     start = yoil.index('FRI')
#     month = a
#     day = b

#     for m in range(1, month):
#         if m == 1:
#             end = (start + 31) % 7
#         elif m == 2:
#             end = (end + 29) % 7
#         elif m in [3,5,7,8,10,12]:
#             end = (end + 31) % 7
#         elif m in [4,6,9,11]:
#             end = (end + 30) % 7

#     if month == 1:
#         result = (start+day) % 7 - 1
#         result_yoil = yoil[result]
#     else:
#         result = (end + day) % 7 - 1
#         result_yoil = yoil[result]

#     return result_yoil
