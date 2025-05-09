-- 코드를 입력하세요
with franks as (SELECT FOOD_TYPE, REST_ID, REST_NAME, FAVORITES,
    rank() over(partition by FOOD_TYPE order by FAVORITES desc) as frank
from REST_INFO)

select FOOD_TYPE, REST_ID, REST_NAME, FAVORITES
from franks
where frank = 1
order by FOOD_TYPE desc