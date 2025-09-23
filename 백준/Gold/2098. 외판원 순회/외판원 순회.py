import sys
INF = sys.maxsize
input = sys.stdin.readline
N = int(input())
prices = []
FULL = (1 << N) - 1
for _ in range(N):
    prices.append(list(map(int, input().split())))
    
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
                w = prices[u][v]
                if w == 0:
                    continue
                if (mask >> v) & 1:
                    continue
                nxt = mask | (1 << v)
                nv = cur + w
                if nv < dp[nxt][v]:
                    dp[nxt][v] = nv
    for u in range(N):
        if dp[FULL][u] < INF and prices[u][s] != 0:
            ans = min(ans, dp[FULL][u] + prices[u][s])
print(ans)