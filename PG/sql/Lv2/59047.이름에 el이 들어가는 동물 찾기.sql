-- 이름에 el이 들어가는 동물 찾기
-- https://school.programmers.co.kr/learn/courses/30/lessons/59047
/*
조건 1 : 이름에 el이 들어간다.
조건 2 : 대소문자를 구분하지 않는다.
조건 3 : 동물 타입은 'Dog'
조건 4 : 이름순으로 정렬한다.
*/

select animal_id, name
from animal_ins
where lower(name) like '%el%' and animal_type = "Dog"
order by name