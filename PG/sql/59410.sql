-- null 처리
-- coalesce 함수 사용하기

select animal_type, coalesce(name,"No name") as name, sex_upon_intake
from animal_ins