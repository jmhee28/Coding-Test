import math
N,M,K = map(int, input().split())
# 위 대각선위오 오, 대각선아래오, 아래, 대각선아래왼, 왼, 대각선위왼
dx = [-1,-1,0, 1, 1,  1,  0,  -1 ]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
dic = {}
ans = M
for i in range(M):
    r, c, m, s, d = map(int, input().split())
    dic[(r-1,c-1)] = [(m,s,d)]

def move(x, y, d, s):
    nx = (x + dx[d] * s) % N
    ny = (y + dy[d] * s) % N
    
    if nx < 0:
        nx = N + nx
    if ny < 0:
        ny = N + ny
    return (nx, ny)

for i in range(K):
    newdic = {}
    for key, val in dic.items():
        x, y = key
        for j in range(len(val)):
            m, s, d = val[j]
            nx, ny = move(x, y, d, s)
            if (nx, ny) not in newdic:
                newdic[(nx, ny)] = [(m, s, d)]
            else:
                newdic[(nx, ny)].append((m, s, d))
    dic = {}
    ans = 0
    for key, val in newdic.items():
        x, y = key
        nm = 0
        nd = 0 # 모두 짝or홀 => nd = 0 
        ns = 0
        dlst = []
        if len(val) > 1:
            msum = 0
            ssum = 0
            direction = val[0][2] % 2
            valsd =[]
            for j in range(len(val)):
                m, s, d = val[j]
                msum += m
                ssum += s
                if d % 2 != direction:
                    nd = 1
            nm = math.floor(msum / 5)
            ns = math.floor(ssum / len(val))
            if nd == 0:
                dlst = [0, 2, 4, 6]
            else:
                dlst = [1, 3, 5, 7]
            if nm > 0:
                ans += nm * 4
                for t in range(4):
                    if (x, y) not in  dic:
                        dic[(x, y)] = [(nm, ns, dlst[t])]
                    else:
                        dic[(x, y)].append((nm, ns, dlst[t])) 
                
        else:
            m, s, d = val[0]
            ans += m
            if (x, y) not in  dic:
                dic[(x, y)] = [(m, s, d)]
            else:
                dic[(x, y)].append((m, s, d))
print(ans)
    