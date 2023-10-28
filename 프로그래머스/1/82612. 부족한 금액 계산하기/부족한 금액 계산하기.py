def solution(price, money, count):
    answer = -1
    res = money - sigma(price, count) 
    if res < 0:
        return abs(res)
    else: 
        return 0
    return answer

def sigma(x, y):
    result = 0
    for i in range(1, y+1):
        result += (x * i)
    return result
        