-- 카테고리 별 도서 판매량 집계하기
-- https://school.programmers.co.kr/learn/courses/30/lessons/144855

SELECT a.category, sum(b.sales)
FROM book a LEFT JOIN book_sales b ON a.book_id = b.book_id
where year(sales_date) = 2022 and month(sales_date) = 1
group by category
order by category