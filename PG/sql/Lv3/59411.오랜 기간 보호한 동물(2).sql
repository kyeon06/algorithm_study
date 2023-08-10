-- 오랜 기간 보호한 동물(2)
-- https://school.programmers.co.kr/learn/courses/30/lessons/59411

SELECT a.animal_id, a.name
FROM animal_ins a LEFT JOIN animal_outs b ON a.animal_id = b.animal_id
ORDER BY DATEDIFF(B.DATETIME,A.DATETIME) DESC
LIMIT 2