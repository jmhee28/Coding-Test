from collections import deque

def solution(queue1, queue2):
    answer = -2
    total = sum(queue1) + sum(queue1)
    div = total // 2
    q1 = deque(queue1)
    q2 = deque(queue2)
    mcnt = len(q1) *3
    s1 = sum(q1)
    s2 = sum(q2)
    cnt = 0
    
    while 1:
        if cnt > mcnt or s1 == s2:
            break
        if s1 > s2:
            t = q1.popleft()
            q2.append(t)
            s1 -= t
            s2 += t
        elif s1 < s2:
            t = q2.popleft()
            q1.append(t)
            s1 += t
            s2 -= t
        cnt += 1
    if s1 == s2:
        return cnt
    else:
        return -1