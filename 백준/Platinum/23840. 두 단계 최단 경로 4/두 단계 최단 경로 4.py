import sys, heapq
from collections import defaultdict

INF = sys.maxsize
input = sys.stdin.readline

# N(10 ≤ N ≤ 100,000), 간선의 수 M(10 ≤ M ≤ 300,000)
N, M = map(int, input().split())  
graph = [[] for _ in range(N + 1)]

for i in range(M):
    # 도시 u와 도시 v 사이의 가중치가 정수 w인 양방향 도로, 
    # (1 ≤ u, v ≤ N, u ≠ v, 1 ≤ w ≤ 1,000,000)
    u, v, w = map(int, input().split())  
    graph[u].append((v, w))
    graph[v].append((u, w))
    
# (1 ≤ X, Z ≤ N, X ≠ Z)
X, Z = map(int, input().split())
#  (3 ≤ P ≤ min(20, N - 3))
P = int(input())
# 서로 다른 중간 정점 Y(1 ≤ Y ≤ N, X ≠ Y ≠ Z)
Y = list(map(int, input().split()))

important = [X] + Y + [Z]
nodeCnt = len(important)  # 최대 22
index = {node: i for i, node in enumerate(important)}


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    dist = [INF] * (N+1)
    dist[start] = 0
    
    while q:
        d, now = heapq.heappop(q)
        if d > dist[now]:
            continue
        for i in graph[now]:
            cost = d + i[1]
            if cost < dist[i[0]]:
                dist[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return dist

distances = [[INF]*nodeCnt for _ in range(nodeCnt)]
for node in important:
    d = dijkstra(node)
    for other in important:
        distances[index[node]][index[other]] = d[other]
        
def tsp():
    FULL = (1 << nodeCnt) - 1
    ans = INF
    start = X
    dp = [[INF]*nodeCnt for _ in range(1<<nodeCnt)]
    start_idx = 0  # X의 인덱스 = 0
    end_idx = nodeCnt - 1  # Z의 인덱스 = 마지막
    dp[1<<start_idx][start_idx] = 0
    
    for mask in range(1 << nodeCnt):
        for u in range(nodeCnt):
            cur = dp[mask][u]
            if cur >= INF:
                continue
            for v in range(nodeCnt):
               w = distances[u][v]
               if w >= INF:
                   continue
               if mask & (1<<v):  # 이미 방문
                    continue
               nxt = mask | (1 << v) 
               nv = cur + w
               if nv < dp[nxt][v]:
                   dp[nxt][v] = nv
                   
 
    ans = dp[FULL][end_idx]
    return -1 if ans == INF else ans    
               
                
ans = tsp()
print(ans)