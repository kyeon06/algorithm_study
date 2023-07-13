-- 성분으로 구분한 아이스크림 총 주문량
-- https://school.programmers.co.kr/learn/courses/30/lessons/133026

select i.ingredient_type, sum(f.total_order)
from first_half f, icecream_info i
where f.flavor = i.flavor
group by i.ingredient_type