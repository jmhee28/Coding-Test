import sys, math
INF = sys.maxsize
input = sys.stdin.readline

cities = []
N = int(input())
distances = [[0] * N for _ in range(N)]
def calcDistance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    ret = math.sqrt(((x1 - x2) ** 2) + (( y1 - y2 ) ** 2) )
    return round(ret, 6)

for i in range(N):
    x, y = map(int, input().split())
    cities.append((x, y))

for i in range(N):
    curCity = cities[i]
    for j in range(N):
        if j == i: continue
        nextCity = cities[j]
        dist = calcDistance(curCity, nextCity)
        distances[i][j] = dist
        distances[j][i] = dist

FULL = (1<<N) - 1
ans = INF
for s in range(N):
    dp = [[INF] * N for _ in range(1 << N)]
    dp[1 << s][s] = 0
    
    for mask in range(1 << N):
        if (mask & (1 << s)) == 0:
            continue
        for u in range(N):
            cur = dp[mask][u]
            if cur >= INF:
                continue
            for v in range(N):
                w = distances[u][v]
                if (mask >> v) & 1:
                    continue
                nxt = mask | (1 << v)
                nv = cur + w
                if nv < dp[nxt][v]:
                    dp[nxt][v] = nv
    for u in range(N):
        if dp[FULL][u] < INF :
            ans = min(ans, dp[FULL][u] + distances[u][s])
print(ans)