-- 코드를 작성해주세요
with parent as (
    select distinct(PARENT_ITEM_ID) as pid
    from ITEM_TREE
    where PARENT_ITEM_ID is not null
    )
 select ITEM_ID, ITEM_NAME, RARITY
 from ITEM_INFO
 where ITEM_ID not in (select pid from parent)
 order by ITEM_ID desc