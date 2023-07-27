-- 조건에 맞는 도서와 저자 리스트 출력하기
-- https://school.programmers.co.kr/learn/courses/30/lessons/144854

SELECT b.book_id, a.author_name, date_format(b.published_date, "%Y-%m-%d")
from book b, author a
where b.author_id = a.author_id and b.category = "경제"
order by b.published_date