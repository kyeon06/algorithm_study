-- 대여 횟수가 많은 자동차들의 월별 대여 횟수 구하기
-- https://school.programmers.co.kr/learn/courses/30/lessons/151139

select month(start_date) as MONTH, car_id, count(*) as RECORDS
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE DATE_FORMAT(START_DATE, '%Y-%m') between "2022-08" and "2022-10"
and car_id in (select car_id from CAR_RENTAL_COMPANY_RENTAL_HISTORY where DATE_FORMAT(START_DATE, '%Y-%m') between "2022-08" and "2022-10" group by car_id having count(*) >= 5)
GROUP BY MONTH, car_id
order by MONTH, car_id DESC