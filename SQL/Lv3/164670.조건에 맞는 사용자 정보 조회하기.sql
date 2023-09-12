-- 조건에 맞는 사용자 정보 조회하기
-- https://school.programmers.co.kr/learn/courses/30/lessons/164670

select user_id, nickname, concat(city ,' ',street_address1, ' ',street_address2) as 전체주소,
CONCAT(SUBSTR(TLNO,1,3),'-',SUBSTR(TLNO,4,4),'-',SUBSTR(TLNO,8,4)) as 전화번호
from USED_GOODS_USER
where user_id in (select writer_id
from used_goods_board group by writer_id HAVING count(*) >= 3)
ORDER BY user_id desc