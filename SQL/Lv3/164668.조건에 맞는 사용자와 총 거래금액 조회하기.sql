-- 조건에 맞는 사용자와 총 거래금액 조회하기
-- https://school.programmers.co.kr/learn/courses/30/lessons/164668

SELECT b.USER_ID, b.NICKNAME, sum(a.PRICE) as TOTAL_SALES
FROM USED_GOODS_BOARD a LEFT JOIN USED_GOODS_USER b ON a.WRITER_ID = b.USER_ID
WHERE a.STATUS = "DONE"
GROUP BY b.USER_ID
HAVING sum(a.PRICE) >= 700000
ORDER BY TOTAL_SALES