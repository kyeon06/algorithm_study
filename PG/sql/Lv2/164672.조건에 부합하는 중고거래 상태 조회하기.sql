-- 조건에 부합하는 중고거래 상태 조회하기
-- https://school.programmers.co.kr/learn/courses/30/lessons/164672

SELECT BOARD_ID, WRITER_ID, TITLE, PRICE, IF(STATUS = "SALE", "판매중", IF(STATUS = "RESERVED", "예약중", "거래완료")) as 거래상태
from USED_GOODS_BOARD
where DATE_FORMAT(CREATED_DATE, "%Y-%m-%d") = "2022-10-05"
order by BOARD_ID DESC