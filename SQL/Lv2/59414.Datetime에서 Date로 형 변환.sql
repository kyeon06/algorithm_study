-- DATETIME에서 DATE로 형 변환
-- https://school.programmers.co.kr/learn/courses/30/lessons/59414

/*
date_format(값, 형식)
*/

SELECT animal_id, name, date_format(datetime, "%Y-%m-%d") as 날짜
from animal_ins
order by animal_id