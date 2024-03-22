import math
defaultMin = 0
defaultFee = 0
timeUnit = 0
feeUnit = 0

def solution(fees, records):
    global defaultMin, defaultFee, timeUnit, feeUnit
    answer = []
    
    defaultMin, defaultFee, timeUnit, feeUnit = fees
    carDict = {}
    
    for record in records:
        # print(record)
        time, carNum, inout = record.split(" ")
        carNum = int(carNum)
        h, m = time.split(':')
        h = int(h)
        m = int(m)
        abstime = h * 60 + m
        # print(abstime, carNum, inout)
        if carNum not in carDict:
            carDict[carNum] = [[inout, abstime]]
        else:
            carDict[carNum].append([inout, abstime])
    values = []        
    for carNum, val in carDict.items():
        values.append([carNum,calculate(carNum, val)])
        # answer.append(calculate(carNum, val))
    values.sort(key= lambda x : x[0])
    for val in values:
        answer.append(val[1])
    return answer

def calculate(carNum, infos):
    # print("start: ", carNum)
    global defaultMin, defaultFee, timeUnit, feeUnit
    
    n = len(infos)
    fee = 0
    last = {}
    lastYn = n % 2 != 0
    if lastYn:
        n -= 1
    # print("lastYn: ", lastYn)    
    fee += defaultFee
    usedMins = 0
    for i in range(0, n, 2):
        # print(i,": " ,infos[i])
        # print(i + 1,": " ,infos[i+ 1])
        amode, aminute  = infos[i]
        bmode, bminute = infos[i+1]
        
        subMin = bminute - aminute
        usedMins += subMin        

    if lastYn:
        amode, aminute = infos[n]
        bminute = (23 * 60 + 59) 
        subMin =  bminute -  aminute
        usedMins += subMin
    print(usedMins)
    if usedMins > defaultMin:
        unit = math.ceil((usedMins - defaultMin) / timeUnit)
        # print("unit: ", unit)
        fee += unit * feeUnit
    # print("fee: ", fee)
    print()
    return fee
            