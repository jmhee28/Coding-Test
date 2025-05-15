-- 코드를 작성해주세요
with nINFO as 
(
    select FISH_TYPE, 
        case 
            when LENGTH <= 10 then 10
            when LENGTH is NULL then 10
        else LENGTH
        end as nLENTH
    from FISH_INFO
),temp as (
    select FISH_TYPE, COUNT(*) as FISH_COUNT, MAX(nLENTH) as MAX_LENGTH, AVG(nLENTH) as AVG_LEN
        from  nINFO       
        group by FISH_TYPE
)
# select * from nINFO
select FISH_COUNT, MAX_LENGTH, FISH_TYPE
from temp
where AVG_LEN >= 33
order by FISH_TYPE