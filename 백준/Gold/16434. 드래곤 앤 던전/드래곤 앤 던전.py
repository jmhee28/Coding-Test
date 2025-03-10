import math
N, hatk = map(int, input().split())


hcurhp = 0
hmaxhp = 0

for i in range(N):
    t, a, h = map(int, input().split())
    if t == 1: # 몬스터    
        dmg = (math.ceil(h/hatk) - 1) * a
        if hcurhp >= dmg: 
            hcurhp -= dmg
        else:
            hmaxhp += dmg - hcurhp
            hcurhp = 0
    else: # 포션
        hatk += a
        hcurhp = min(hcurhp + h, hmaxhp)
print(hmaxhp + 1)
        