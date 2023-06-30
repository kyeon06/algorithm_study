-- 나이 정보가 없는 회원 수 구하기

select count(*) as users
from user_info
where age is null