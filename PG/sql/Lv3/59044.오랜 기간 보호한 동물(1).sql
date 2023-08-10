-- 오랜 기간 보호한 동물(1)
-- https://school.programmers.co.kr/learn/courses/30/lessons/59044

SELECT A.NAME, A.DATETIME
FROM animal_ins A LEFT JOIN animal_outs B ON A.animal_id = B.animal_id
WHERE B.animal_id is Null
ORDER BY A.DATETIME
LIMIT 3