-- 코드를 작성해주세
SELECT A.ITEM_ID, A.ITEM_NAME, A.RARITY
FROM ITEM_INFO AS A
JOIN ( SELECT DISTINCT C.ITEM_ID, D.RARITY
       FROM ITEM_TREE C
       JOIN ITEM_INFO D ON C.PARENT_ITEM_ID = D.ITEM_ID
       WHERE D.RARITY = 'RARE'
     ) AS B ON A.ITEM_ID = B.ITEM_ID
ORDER BY A.ITEM_ID DESC;


# SELECT a.ITEMID, a.ITEMNAME, a.RARITY
# FROM ITEMINFO a
# JOIN (SELECT c.ITEMID, d.RARITY
# FROM ITEMTREE c
# JOIN ITEMINFO d ON c.PARENTITEMID = d.ITEMID
# WHERE d.RARITY = 'RARE') b ON a.ITEMID = b.ITEMID
# ORDER BY a.ITEMID DESC;