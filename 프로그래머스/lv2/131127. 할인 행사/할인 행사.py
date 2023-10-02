
n = 0
m = 0
targetCount = {}
answer = 0

def solution(want, number, discount):
    global n, m
  
    n = len(want)
    m = len(discount)
    for i in range(n):
        item = want[i]
        targetCount[item] = number[i]      
    
    
    for i in range (0, m-9):
        start = i
        end = i+10
        targetDiscount = discount[start:end]
        checkArr(targetDiscount, want)
        
    return answer

def checkArr(targetDiscount,  want):
    global n, m, answer
    flag = 0
    for j in range(n):
        item = want[j]
        if targetDiscount.count(item) < targetCount[item]:
            flag = 1
            break
    if flag == 0:
        answer += 1