-- 조건별로 분류하여 주문상태 출력하기
-- https://school.programmers.co.kr/learn/courses/30/lessons/131113

SELECT order_id, product_id, DATE_FORMAT(out_date, "%Y-%m-%d"), IF(DATE_FORMAT(out_date, "%m-%d") <= "05-01", "출고완료", IF(DATE_FORMAT(out_date, "%m-%d") > "05-01", "출고대기", "출고미정"))
FROM food_order
order by order_id