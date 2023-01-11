from itertools import combinations
N, M = map(int, input().split())
mp = []
chickenpos =[]
housepos =[]
distance ={} #(idx, dis)
chickidx=[]
for i in range(N):
    mp.append(list(map(int, input().split())))
for i in range(N):
    for j in range(N):
        if mp[i][j] == 2:
            chickenpos.append((i, j))
        elif mp[i][j] == 1:
            housepos.append((i, j))

for i in range(len(chickenpos)):
    chickidx.append(i)
    for j in range(len(housepos)):
        dis = abs(chickenpos[i][0] - housepos[j][0]) + abs(chickenpos[i][1] - housepos[j][1])
        if i not in distance:
            distance[i] =[(j, dis)] 
        else:
            distance[i].append((j,dis))
lst = list(combinations(chickidx, M))
ans = -1
for i in lst:
    housedis = {}
    for j in i:
        for d in distance[j]:
            if d[0] in housedis:
                housedis[d[0]].append(d[1])
            else: 
                housedis[d[0]]= [d[1]]

    s=0
    for k,v in housedis.items():
        s += min(v)
    if ans == -1:
        ans = s
    elif ans > s:
        ans = s       
print(ans)