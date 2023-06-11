X, Y = 0,0
def getSyms(bx, by, n, m):
    syms = []
    if not (Y == by and bx < X):
        syms.append((bx * -1, by)) #왼쪽 y축 대칭
    if not (Y == by and bx > X):
        syms.append((bx + (m-bx)*2, by)) #오른쪽 y축 대칭
    if not (X == bx and by < Y):
        syms.append((bx, by * -1)) #아래 x축 대칭
    if not (X == bx and by > Y):
        syms.append((bx, by + (n-by) * 2)) #위 x축 대칭
    return syms

def solution(m, n, startX, startY, balls):
    global X, Y
    X = startX
    Y = startY
    answer = []
    for ball in balls:
        bx, by = ball[0], ball[1]
        syms = getSyms(bx, by, n, m)
        dis = []
        for sym in syms:
            sx, sy = sym
            distance = pow(abs(sx-startX), 2) + pow(abs(sy-startY), 2)
            dis.append(distance)
        answer.append(min(dis))
    return answer