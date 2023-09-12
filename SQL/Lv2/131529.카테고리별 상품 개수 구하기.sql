-- 카테고리 별 상품 개수 구하기
-- https://school.programmers.co.kr/learn/courses/30/lessons/131529

SELECT left(product_code,2) as category, count(*) as products
from product
group by category
order by category