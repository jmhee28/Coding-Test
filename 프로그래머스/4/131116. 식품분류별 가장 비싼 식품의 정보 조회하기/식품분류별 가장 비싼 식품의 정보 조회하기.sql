-- 코드를 입력하세요
with food_rank as (
    SELECT CATEGORY, 
        PRICE,
        RANK() OVER(PARTITION by CATEGORY order by PRICE  desc) as price_rank,
        PRODUCT_NAME
    from FOOD_PRODUCT
    WHERE CATEGORY IN ( '과자', '국', '김치', '식용유')
    )
select CATEGORY, PRICE as MAX_PRICE, PRODUCT_NAME
from food_rank
where price_rank = 1
order by  MAX_PRICE desc