-- 코드를 입력하세요
with hdiff as (
    SELECT h.HISTORY_ID, h.CAR_ID, datediff(h.END_DATE, h.START_DATE) + 1 as diff, c.DAILY_FEE
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY as h
    join CAR_RENTAL_COMPANY_CAR as c on h.CAR_ID = c.CAR_ID
    where c.CAR_TYPE = '트럭'
),
tplan as (
    select REGEXP_REPLACE(DURATION_TYPE, '[^0-9]','') as days, DISCOUNT_RATE
    from  CAR_RENTAL_COMPANY_DISCOUNT_PLAN
    where CAR_TYPE='트럭'
),
seven as (
      select DISCOUNT_RATE 
        from tplan
        where days = 7
),
thirty as (
      select DISCOUNT_RATE 
        from tplan
        where days = 30
),
ninety as (
      select DISCOUNT_RATE 
        from tplan
        where days = 90
)

# select * from tplan

select h.HISTORY_ID,
    case 
        when h.diff >= 7 and h.diff < 30 
            then FLOOR(h.diff * h.DAILY_FEE * (1 - (select DISCOUNT_RATE from seven)/100))
        when h.diff >= 30 and h.diff < 90 
            then FLOOR(h.diff * h.DAILY_FEE * (1 - (select DISCOUNT_RATE from thirty)/100))
        when h.diff >= 90
            then FLOOR(h.diff * h.DAILY_FEE * (1 - (select DISCOUNT_RATE from ninety)/100))
        else h.diff * h.DAILY_FEE
    end as fee
from hdiff as h
order by fee desc, h.HISTORY_ID desc