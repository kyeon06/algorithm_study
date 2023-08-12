-- 대여 기록이 존재하는 자동차 리스트 구하기
-- https://school.programmers.co.kr/learn/courses/30/lessons/157341

SELECT distinct(a.car_id)
FROM CAR_RENTAL_COMPANY_CAR a LEFT JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY b ON a.car_id = b.car_id
WHERE month(b.START_DATE) = 10 and a.car_type = "세단"
ORDER BY car_id DESC