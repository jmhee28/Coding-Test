def solution(arrayA, arrayB):
    answer = 0
    
    arrayA.sort()
    arrayB.sort()
    
    agcd = getGcd(arrayA)
    bgcd = getGcd(arrayB)
    
    if checkAB(agcd, arrayB):
        answer = agcd
    if checkAB(bgcd, arrayA):
        answer = max(bgcd, answer)

    return answer

def gcd(a, b):
    if b == 0: 
        return a
    return gcd(b, a % b)

def getGcd(arr):
    arrGcd = arr[0]
    for i in range(1, len(arr)):
        arrGcd = gcd(arrGcd, arr[i])
        
    return arrGcd
        

def checkAB(gcdNum, arr):
    for i in range(len(arr)):
        if arr[i] % gcdNum == 0:
            return False
    return True