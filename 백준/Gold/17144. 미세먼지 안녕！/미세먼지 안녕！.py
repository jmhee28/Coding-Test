import sys
import copy
input = sys.stdin.readline
r,c,t = map(int, input().split())
room = []
proom = []
#오른 위 왼 아래
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
purifier = []
for i in range(r):
    lst = list(map(int, input().split()))
    room.append(lst)
    proom.append(copy.deepcopy(lst))
    if room[i][0] == -1:
        purifier.append(i)


def getSum():
    s = 0
    for i in range(r):
        s += sum(room[i])
    return s

def propagate():
    for i in range(r):
        for j in range(c):
            if proom[i][j] > 0:
                propagation = proom[i][j] // 5
                for d in range(4):
                    nx = i + dx[d]
                    ny = j + dy[d]
                    if  0 <= nx < r and 0 <= ny < c and room[nx][ny] != -1:
                        room[nx][ny] += propagation
                        room[i][j] -= propagation
def purifyUp():
    p = purifier[0]
    #오른쪽부터 시작
    d = 0
    before = 0
    x, y = p, 1
    while True:
        nx = x + dx[d]
        ny = y + dy[d]
        if nx == r or ny == c or nx == -1 or ny == -1:
            d = (d+1)%4
            continue
        if x == p and y == 0:
            break
        room[x][y], before = before, room[x][y]
        x, y = nx, ny
    

def purifyDown():
    p = purifier[1]
    #오른쪽부터 시작
    d = 0
    before = 0
    x, y = p, 1
    while True:
        nx = x + dx[d]
        ny = y + dy[d]
        if nx == r or ny == c or nx == -1 or ny == -1:
            d = (d - 1) % 4
            continue
        if x == p and y == 0:
            break
        room[x][y], before = before, room[x][y]
        x, y = nx, ny
for i in range(t):
    propagate()
    purifyUp()
    purifyDown()
    proom = copy.deepcopy(room)
print(getSum()+2)
# 6 6 10
# -1 100 0 0 0 0
# -1 100 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 50 0 0 0 0
# 0 50 0 0 0 0