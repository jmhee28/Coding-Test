-- 코드를 입력하세요
SELECT info.INGREDIENT_TYPE, sum(fh.TOTAL_ORDER) as TOTAL_ORDER
from FIRST_HALF as fh
join ICECREAM_INFO info on fh.FLAVOR = info.FLAVOR
group by info.INGREDIENT_TYPE