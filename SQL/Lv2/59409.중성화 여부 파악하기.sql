-- 중성화 여부 파악하기
-- https://school.programmers.co.kr/learn/courses/30/lessons/59409

/*
IF(조건문, 참, 거짓)
*/

SELECT animal_id, name,
IF((sex_upon_intake like '%Neutered%') or (sex_upon_intake like '%Spayed%'), 'O', 'X') as 중성화
from animal_ins
order by animal_id