-- 코드를 입력하세요
SELECT ORDER_ID, PRODUCT_ID, DATE_FORMAT(OUT_DATE,"%Y-%m-%d"), 
    case when OUT_DATE > '2022-05-01' THEN "출고대기"
        when OUT_DATE <= '2022-05-01' THEN "출고완료"
        else "출고미정"
        end
        as 출고여부
        
from FOOD_ORDER
ORDER BY ORDER_ID