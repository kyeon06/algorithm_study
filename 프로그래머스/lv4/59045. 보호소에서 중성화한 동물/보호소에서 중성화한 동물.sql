-- 코드를 입력하세요
SELECT A.animal_id, A.animal_type, A.name
FROM ANIMAL_INS A LEFT JOIN ANIMAL_OUTS B ON A.animal_id = B.animal_id 
WHERE A.SEX_UPON_INTAKE like '%Intact%' and (B.SEX_UPON_OUTCOME like '%Spayed%' or B.SEX_UPON_OUTCOME like '%Neutered%')