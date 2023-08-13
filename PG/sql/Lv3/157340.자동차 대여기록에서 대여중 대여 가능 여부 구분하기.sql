-- 자동차 대여 기록에서 대여중 / 대여 가능 여부 구분하기
-- https://school.programmers.co.kr/learn/courses/30/lessons/157340

SELECT car_id, max(IF('2022-10-16' between start_date and end_date, "대여중", "대여 가능")) as AVAILABILITY
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
group by car_id
order by car_id desc