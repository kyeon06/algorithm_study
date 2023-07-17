-- 입양 시각 구하기(1)
-- https://school.programmers.co.kr/learn/courses/30/lessons/59412

SELECT hour(DATETIME) as HOUR, count(*) as COUNT
from animal_outs
where hour(DATETIME) >= 9 and hour(DATETIME) <= 19
group by HOUR
order by HOUR