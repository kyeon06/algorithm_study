-- 있었는데요 없었습니다
-- https://school.programmers.co.kr/learn/courses/30/lessons/59043

SELECT A.animal_id, A.name
FROM animal_ins A LEFT JOIN animal_outs B ON A.animal_id = B.animal_id
Where A.DATETIME > B.DATETIME
ORDER BY A.DATETIME