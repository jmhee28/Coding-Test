import sys
import heapq

input = sys.stdin.readline
looks = []
INF = sys.maxsize

n, m  = map(int, input().split())
looks = list(map(int, input().split()))
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)
looks[n-1] = 0
for i in range(m):
    a, b, t = map(int, input().split())
    graph[a].append((b, t))
    graph[b].append((a, t))
    
def dijk(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            if looks[i[0]] == 1:
                    continue
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
                
dijk(0)
if distance[n-1] == INF: 
    print(-1)
else:
    print(distance[n-1])