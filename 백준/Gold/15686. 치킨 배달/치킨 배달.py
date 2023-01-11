from itertools import combinations
N, M = map(int, input().split())
mp = []
chickenpos =[] #치킨집 위치
housepos =[] # 집위치
distance ={} #(idx, dis)
chickidx=[]
for i in range(N):
    mp.append(list(map(int, input().split())))
#치킨집, 집 위치 저장
for i in range(N):
    for j in range(N):
        if mp[i][j] == 2:
            chickenpos.append((i, j))
        elif mp[i][j] == 1:
            housepos.append((i, j))

# 치킨집에서 집 거리 저장
# distance[치킨집 index] = [(집 index, 집과의 거리), ...]
for i in range(len(chickenpos)):
    chickidx.append(i)
    for j in range(len(housepos)):
        dis = abs(chickenpos[i][0] - housepos[j][0]) + abs(chickenpos[i][1] - housepos[j][1])
        if i not in distance:
            distance[i] =[(j, dis)] 
        else:
            distance[i].append((j,dis))
# 치킨집 고르기
lst = list(combinations(chickidx, M))
ans = -1
for i in lst: # i : 고른 치킨집
    housedis = {} # 고른 치킨집과 집과의 거리 housedis[집 index] = [치킨집과의 거리]
    for j in i: # j: i에 있는 치킨집 index
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