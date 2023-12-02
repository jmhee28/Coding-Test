import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

N,M,X = map(int, input().split())
fromX = [[] for _ in range(N+1)]
toX = [[] for _ in range(N+1)]
distFromX = [INF] * (N+1)
distToX = [INF] * (N+1)

for i in range(M):
    a, b, c = map(int, input().split())
    fromX[a].append((b,c))
    toX[b].append((a, c))
    
def dijkstra(start, graph, distance):
    q =[]
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue
        
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost, i[0]))

dijkstra(X, fromX, distFromX)
dijkstra(X, toX, distToX)
answer = 0

for i in range(1, N+1):
    answer = max(answer, distFromX[i] + distToX[i])
print(answer)