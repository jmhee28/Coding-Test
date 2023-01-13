from itertools import product

def solution(users, emoticons):
    elen = len(emoticons) #이모티콘 갯수
    answer = []
    discounts = [10, 20, 30, 40]
    disproducts = list(product(discounts, repeat = elen))
    
    lst = []
    
    for disproduct in disproducts:
        pluscnt = 0 #플러스 서비스 가입자 수 
        sale = 0 # 판매액
        ecosts = [] # 이모티콘 할인 적용 금액
        for i in range(elen):
            cost = emoticons[i] * ( 0.01 * (100 - disproduct[i]))
            ecosts.append(cost)
        for user in users:            
            buycost = 0 # 한명이 사는 금액
            for i in range(elen): 
                if disproduct[i] >= user[0]: #할인률이 더 크면 구매
                    buycost += int(ecosts[i])
            if buycost >= user[1]: #금액이 기준 이상이면 가입
                pluscnt += 1
            else: #아니면 sale에 추가
                sale += buycost
        lst.append((pluscnt, sale))
    lst.sort(key = lambda x:(x[0], x[1]), reverse = True)        
    return lst[0]