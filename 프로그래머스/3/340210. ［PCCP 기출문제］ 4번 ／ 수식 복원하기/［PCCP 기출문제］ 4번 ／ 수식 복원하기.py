def calculate(base, eqaution):
    op1, op2, operator = eqaution[0], eqaution[1], eqaution[2]
    nop1 = to_10base(op1, base)
    nop2 = to_10base(op2, base)
    if operator == "+":
        return nop1 + nop2
    else:
        return nop1 - nop2
    
def to_10base(n, base):
    n = int(n)
    t = 0
    ret = 0
    while n:
        cur = n % 10
        ret += (base ** t) * cur
        t += 1
        n //= 10
    return ret

def to_base(n, base):
    if n == 0: return "0"
    digits = []
    while n:
        digits.append(str(n % base))
        n //= base
    return "".join(reversed(digits))

def getBases(bases, extracted): # bases: 진법들, tobeSolved: 풀어야할 식
    # [식idx1] = [진법 1, 진법 2]
    # [식idx2] = [진법 2] - 진법 1로 못풀으면 바로 false
    trueBase = []
    posBaseDict = {}
    for b in bases:
        posBaseDict[b] = True
        
    for eqaution in extracted:
        op1, op2, operator, result = eqaution
        for b in bases:
            ten_result = to_10base(result, b)
            calc = calculate(b, eqaution)
            if calc != ten_result:
                posBaseDict[b] = False
    for k in posBaseDict.keys():
        if posBaseDict[k]:
            trueBase.append(k)
    return trueBase

def solution(expressions):
    answer = []
    max_num = 0
    numbers = []
    extracted = []
    tobeSolved = []
    bases = [] # 가능한 진법들
    for e in expressions:
        ex = e.split(" ")
        op1, operator, op2, result = ex[0], ex[1], ex[2], ex[4]
        
        numbers.extend(list(ex[0]))
        numbers.extend(list(ex[2]))
        
        if result != 'X':
            numbers.extend(list(ex[4]))
            extracted.append([op1, op2, operator, result])
            # if len(result) > max(len(op1), len(op2)) and operator == "+":
            #     temp = int(op1) + int(op2)
            #     s = str(temp)[0]
            #     max_num = max(max_num, int(s) - 1)
        else:
            tobeSolved.append([op1, op2, operator])
    max_num = max(max_num, int(max(numbers)))
    # if max_num == 1: -> 2진법
    #    continue
    
    for i in range(max_num + 1 , 10):
        bases.append(i)
    
    trueBases = getBases(bases, extracted)
    toSolveCnt = len(tobeSolved)
    answerCandidates = [set() for _ in range(toSolveCnt)]
    
    for i in range(toSolveCnt):
        op1, op2, operator = tobeSolved[i]
        for base in trueBases:
            val = calculate(base, [op1, op2, operator])
            val = to_base(val, base)
            answerCandidates[i].add(val)
            
    for i in range(toSolveCnt):
        op1, op2, operator = tobeSolved[i]
        eq = op1 + " " + operator +  " " + op2 + " = "
        if len(answerCandidates[i]) == 1:
            eq +=  str(list(answerCandidates[i])[0])
        else:
            eq += "?"
        answer.append(eq)
    # print(answer)
    return answer
# solution(	["10 - 2 = X", "30 + 31 = 101", "3 + 3 = X", "33 + 33 = X"])
# solution(["1 + 1 = 10", "1 + 11 = X", "1 + 10 = 11"])