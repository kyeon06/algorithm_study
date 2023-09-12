-- 가격대 별 상품 개수 구하기
-- https://school.programmers.co.kr/learn/courses/30/lessons/131530

select FLOOR(price/10000) * 10000 as price_group, count(*)
from product
group by price_group
order by price_group