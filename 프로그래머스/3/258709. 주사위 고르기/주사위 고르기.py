from collections import defaultdict, Counter
import copy
D = 6
N = 0
diceComb = []
diceInfo = []
def chooseDice(chosen, start):
    if len(chosen) == N // 2:
        diceComb.append(chosen[:])
        return
    for i in range(start, N):
        chooseDice(chosen + [i], i + 1)

            
def getPos(comb, numbers, curIdx, diceCombPos):
    if len(numbers) == N//2:
        # print(numbers)
        s = 0
        p = 1
        for num, cnt in numbers:
            s += num
            p *= cnt
        diceCombPos.append((s, p))
        return
    diceIdx = comb[curIdx]
    for d in diceInfo[diceIdx]: # 각 주사위에서 나올 수 있는 숫자, 횟수 # Counter 형태
        diceNum, cnt = d, diceInfo[diceIdx][d]
        numbers.append((diceNum, cnt))
        getPos(comb, numbers, curIdx + 1, diceCombPos)
        numbers.pop()
        
            
def solution(dice):
    global N, diceInfo
    N = len(dice)
    answer = []
    diceInfo = [Counter() for _ in range(N)]
    for i in range(N):
        diceInfo[i] = Counter(dice[i])

    chooseDice([], 0) ## 주사위 조합 diceComb 만들기
    combPos = []
    for i in range(len(diceComb)):
        diceCombPos = []
         # 각 조합에서 나올 수 있는 숫자, 횟수
        getPos(diceComb[i], [], 0, diceCombPos)
        ## diceCombPos : (숫자 합, 경우의 수)
        ## 숫자합이 같으면 확률 더하기
        posMap = defaultdict(int)
        for s, p in diceCombPos:
            posMap[s] += p
        combPos.append(posMap)
    ## combPos : 각 조합에서 나올 수 있는 (숫자 합, 경우의 수) 딕셔너리
    # for i in range(len(diceComb)):
    #     print(f"조합 {diceComb[i]}")
    #     print(combPos[i])
    # 각 조합이 이길 확률
    # 주사위를 a, b 각각 n/2 가짐
    # 주사위 조합을 한 개 고르면 상대 주사위가 정해짐 -> 이거를 어떻게 처리하지?
    # 예를 들어, 4개 주사위가 있을 때, (0,1) 조합을 고르면 (2,3) 조합이 상대가 됨
    awin = 0
    for i in range(len(diceComb)):
        win = 0
        lose = 0
        j = len(diceComb) - 1 - i
        for s1, p1 in combPos[i].items():
            for s2, p2 in combPos[j].items(): 
                if s1 > s2:
                    win += p1 * p2
                elif s1 < s2:
                    lose += p1 * p2
        if awin < win:
            awin = win
            answer = diceComb[i]
        # print(f"조합 {diceComb[i]} vs {diceComb[j]} : {win} : {lose}")
    
    answer = [a + 1 for a in answer]
        
    return answer


