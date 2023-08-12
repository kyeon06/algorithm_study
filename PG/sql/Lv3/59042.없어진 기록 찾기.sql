-- 없어진 기록 찾기
-- https://school.programmers.co.kr/learn/courses/30/lessons/59042

SELECT a.animal_id, a.name
FROM ANIMAL_OUTS a LEFT JOIN ANIMAL_INS b ON a.animal_id = b.animal_id
where b.animal_id is null
order by b.ANIMAL_ID