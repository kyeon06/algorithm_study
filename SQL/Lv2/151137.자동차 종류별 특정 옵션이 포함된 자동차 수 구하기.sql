-- 자동차 종류 별 특정 옵션이 포함된 자동차 수 구하기
-- https://school.programmers.co.kr/learn/courses/30/lessons/151137

SELECT CAR_TYPE, count(OPTIONS) as CARS
from CAR_RENTAL_COMPANY_CAR
where OPTIONS LIKE '%통풍시트%' OR OPTIONS LIKE '%열선시트%' OR OPTIONS LIKE '%가죽시트%'
group by CAR_TYPE
order by CAR_TYPE