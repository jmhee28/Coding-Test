-- 코드를 작성해주세요
with monthInfo as (
    select MONTH(DIFFERENTIATION_DATE) as month,
        case when  MONTH(DIFFERENTIATION_DATE) in (1, 2, 3) then "1Q"
         when  MONTH(DIFFERENTIATION_DATE) in (4, 5, 6) then "2Q"
         when  MONTH(DIFFERENTIATION_DATE) in (7, 8, 9) then "3Q"
        else "4Q"
        end as QUARTER
    from ECOLI_DATA
)
select QUARTER,  count(*) as ECOLI_COUNT
from monthInfo
group by QUARTER
order by QUARTER