-- 재구매가 일어난 상품과 회원 리스트 구하기
-- https://school.programmers.co.kr/learn/courses/30/lessons/131536

SELECT USER_ID, PRODUCT_ID
from ONLINE_SALE
group by user_id, product_id
having count(*) >= 2
order by 1, 2 DESC