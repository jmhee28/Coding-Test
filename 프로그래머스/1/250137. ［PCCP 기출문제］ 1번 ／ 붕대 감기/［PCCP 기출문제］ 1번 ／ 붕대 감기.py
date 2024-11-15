bandageRecovery = 0
currentHealth = 0
maxHealth = 0
bandageTime = 0
bandageExtraRecovery = 0
recoveryCnt = 0
def solution(bandage, health, attacks):
    global bandageTime, bandageRecovery, currentHealth, maxHealth, bandageExtraRecovery, recoveryCnt
    answer = 0
    bandageTime = bandage[0]
    bandageRecovery = bandage[1]
    bandageExtraRecovery = bandage[2]
    maxHealth = health
    currentHealth = health
    recoveryCnt = 0 # 연속성공 횟수
    currentSec = 0
    
    for attack in attacks:
        attackTime = attack[0]
        attackPower = attack[1]
        while currentSec < attackTime:
            #print("현체력: ", currentHealth, "현재시간: ", currentSec, "연속성공 횟수:", recoveryCnt)
            recoveryCnt += 1
            recover()
            currentSec += 1
            #print("현체력: ", currentHealth, "현재시간: ", currentSec, "연속성공 횟수:", recoveryCnt)
        # 공격
        currentHealth -= attackPower
        #print("현체력: ", currentHealth, "현재시간: ", currentSec, "연속성공 횟수:", recoveryCnt)
        recoveryCnt = 0 
        currentSec += 1
        #print("현체력: ", currentHealth, "현재시간: ", currentSec, "연속성공 횟수:", recoveryCnt)
        if currentHealth <= 0:
            return -1
    return currentHealth

def recover():
    global currentHealth,recoveryCnt
    if recoveryCnt >= bandageTime:
        currentHealth += bandageExtraRecovery
        recoveryCnt = 0
    currentHealth += bandageRecovery
    if currentHealth > maxHealth:
        currentHealth = maxHealth
        
