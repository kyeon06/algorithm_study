-- 저자 별 카테고리 별 매출액 집계하기

select b.author_id, b.author_name, a.category, sum(c.sales * a.price) as sales
from book as a, author as b, book_sales as c
where a.author_id = b.author_id and a.book_id = c.book_id and left(c.sales_date, 7) = "2022-01"
group by a.author_id, a.category
order by a.author_id, a.category DESC