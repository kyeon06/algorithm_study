-- 조건에 맞는 회원 수 구하기
-- left(컬럼명, N) : 왼쪽에서부터 N번째까지 해당되는 부분

select count(*) as userCount
from user_info
where left(joined,4) = "2021" and age >= 20 and age <= 29