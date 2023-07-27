-- 상품별 오프라인 매출 구하기
-- https://school.programmers.co.kr/learn/courses/30/lessons/131533

SELECT p.product_code, (p.price * sum(s.SALES_AMOUNT)) as sales
from product p, offline_sale s 
where p.product_id = s.product_id
group by product_code
order by 2 DESC, 1