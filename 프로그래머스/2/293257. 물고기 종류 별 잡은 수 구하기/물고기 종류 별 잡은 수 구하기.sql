-- 코드를 작성해주세요
select count(fi.ID) as FISH_COUNT, 
ni.FISH_NAME as FISH_NAME
from FISH_INFO as fi
join FISH_NAME_INFO as ni
on fi.FISH_TYPE = ni.FISH_TYPE
group by ni.FISH_NAME
order by FISH_COUNT desc