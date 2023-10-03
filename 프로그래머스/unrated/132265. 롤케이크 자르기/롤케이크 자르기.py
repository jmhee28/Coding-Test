from collections import Counter

def solution(topping):
    answer = 0
    global n
    n = len(topping)
    toppCounts = Counter(topping)
    print(toppCounts)
    aArr = {}
    for i in range(n):
        item = topping[i]
        subFromDict(toppCounts, item)
        addToDict(aArr, item)
        if len(toppCounts) == len(aArr):
            answer += 1
    return answer

def addToDict(dic, item):
    if item not in dic:
        dic[item] = 1
    else:
        dic[item] += 1
def subFromDict(dic, item):
    if item not in dic:
        return
    dic[item] -= 1
    if dic[item] == 0:
        del dic[item]