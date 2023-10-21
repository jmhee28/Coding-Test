from collections import deque
import copy
import sys

mentoStatus = {}
reqDict = {}
INF = 1e9
answer = 0
dp = []
def solution(k, n, reqs):
    global answer
    global dp
    dp = [[INF for _ in range(n + 2)] for _ in range(k +2)]

    for i in range(k): # 유형 별 멘토인원 적어도 하나
        mentoStatus[i+1] = 1
        reqDict[i+1] = []
    for req in reqs:
        reqDict[req[2]].append(req)
    
    makeDp(k, n) 
    curMen = n - k
    while curMen > 0:
        maxReduce = 0
        maxReduceIdx = 1
        for i in range(1, k+1):
            reduce = dp[i][mentoStatus[i]] - dp[i][mentoStatus[i]+1]
            if reduce > maxReduce:
                maxReduce = reduce
                maxReduceIdx = i
        mentoStatus[maxReduceIdx] += 1
        curMen -= 1   
    for i in range(1, k+1):
        answer += dp[i][mentoStatus[i]]    
    return answer

def makeDp(k, n): ## 멘토 분배 시 걸리는 대기시간 구하기
    for m in range(1, n+1):
        for i in range(1, k+1):
            w = getWaitTime(i, m, copy.deepcopy(reqDict[i]))
            dp[i][m] = w  
                      
def getWaitTime(typeNum, mcnt, requests):
    result = 0
    mentos = {}
    if mcnt >= len(requests):
        return result
    
    for i in range(mcnt):
        mentos[i] = [requests[i]]
        
    for i in range(mcnt, len(requests)):
        rTime = requests[i][0] # 요청시각
        dTime = requests[i][1] # 상담시간
        leastWait = INF
        leastWaitMento = -1
        for j in range(mcnt):
            prev = mentos[j][len(mentos[j])-1]
            if (prev[0] + prev[1]) > rTime:
                curWait = (prev[0] + prev[1]) - rTime
                if curWait <= leastWait :
                    leastWaitMento = j
                    leastWait = curWait
            else:
                leastWaitMento = j
                leastWait = 0
        if leastWaitMento == -1:
            mentos[0].append(requests[i])
        else:  
            requests[i][0] = rTime + leastWait
            result += leastWait
            mentos[leastWaitMento].append(requests[i])
    return result

        
# r = solution(3,	5,	[[10, 60, 1], [15, 100, 3], [20, 30, 1], [30, 50, 3], [50, 40, 1], [60, 30, 2], [65, 30, 1], [70, 100, 2]])
# print(r)