N, M = 0, 0 
def paint(sidx, painted):
    for i in range(sidx, sidx + M):
        if i < N:
            painted[i] = 1
def solution(n, m, section):
    global N, M
    N, M = n, m
    answer = 0
    if m == 1:
        return len(section)
    painted = [1 for _ in range(n)]
    for s in section: 
        painted[s-1] = 0
    for s in section: 
        if painted[s-1] == 0:
            paint(s-1, painted)
            answer += 1
    return answer