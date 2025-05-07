-- 코드를 입력하세요
with SALES as(
    SELECT BOOK_ID, SALES_DATE, sum(SALES) as BOOKSALES
    from BOOK_SALES
    WHERE SALES_DATE LIKE '2022-01%'
    group by BOOK_ID
             ),
author_sales as(
    select bk.BOOK_ID, bk.AUTHOR_ID, s.BOOKSALES * bk.PRICE as bsales, bk.CATEGORY
    from BOOK as bk
    join SALES as s on bk.BOOK_ID=s.BOOK_ID
)
select a.AUTHOR_ID, a.AUTHOR_NAME, atsa.CATEGORY, 
 sum(atsa.bsales) as TOTAL_SALES
from AUTHOR as a
join author_sales as atsa on a.AUTHOR_ID = atsa.AUTHOR_ID
group by a.AUTHOR_ID,atsa.CATEGORY
order by a.AUTHOR_ID, atsa.CATEGORY DESC