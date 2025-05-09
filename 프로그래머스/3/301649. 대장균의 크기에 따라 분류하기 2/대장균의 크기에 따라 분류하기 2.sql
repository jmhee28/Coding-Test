-- 코드를 작성해주세요

with prank as (
    SELECT ID,  
        percent_rank() OVER(ORDER BY SIZE_OF_COLONY desc) AS percentile_rank
    FROM ECOLI_DATA
)
select ID,
    case 
        when percentile_rank <= 0.25 then "CRITICAL"
        when percentile_rank <= 0.50 then "HIGH"
        when percentile_rank <= 0.75 then "MEDIUM"
        else "LOW"
    end as COLONY_NAME
from prank
order by ID 
