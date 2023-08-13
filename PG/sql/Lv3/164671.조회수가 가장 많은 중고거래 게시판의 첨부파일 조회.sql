-- 조회수가 가장 많은 중고거래 게시판의 첨부파일 조회하기
-- https://school.programmers.co.kr/learn/courses/30/lessons/164671

select concat('/home/grep/src/', b.board_id,'/',file_id,file_name,file_ext) as file_path
from USED_GOODS_BOARD b LEFT JOIN USED_GOODS_FILE f ON b.board_id = f.board_id
where b.views in (select max(views) from USED_GOODS_BOARD)
order by file_id desc