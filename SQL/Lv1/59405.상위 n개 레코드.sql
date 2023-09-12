-- 상위 n개 레코드
-- limit : 상위 N개의 데이터를 조회할 경우 사용

select name
from animal_ins
order by datetime
limit 1