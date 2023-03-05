def right(s):
    stack =[]
    for i in range(len(s)):
        if s[i] == '(':
            stack.append('(')
        else:
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    return True

def seperate(s):
    ret =[]
    a = 0
    b = 0
    if s[0] == '(':
            a += 1
    else:
        b += 1
    for i in range(1, len(s)):
        if a == b:
            break
        if s[i] == '(':
            a += 1
        else:
            b += 1
    return [s[:a+b], s[a+b:]]
    
def solution(p):
    answer = ''
    if right(p) == True:
        return p
    u, v = seperate(p)
    if right(u):
        answer = u + solution(v)
    else:
        answer += '(' + solution(v) + ')'
        u = u[1:-1]
        t = ''
        for i in range(len(u)):
            if u[i] == '(':
                t += ')'
            else:
                t += '('
        answer += t
                
        
    return answer