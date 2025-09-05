import sys, heapq

N, M = map(int, input().split())
INF = sys.maxsize
graph = [[] for _ in range(N + 1)]

distances =[INF for _ in range(N+1)]

for i in range(M):
    a, b, c = map(int, input().split()) # 노드1, 노드2, 소의 마리수
    graph[a].append((b, c))
    graph[b].append((a, c))

def dijkstra(start):
    q = []
    q.append((0, start))
    distances[start] = 0
    
    while q:
        dist , cur = heapq.heappop(q)
        if distances[cur] < dist:
            continue
        for node in graph[cur]:
            cost = dist + node[1]
            if cost < distances[node[0]]:
                distances[node[0]] = cost
                heapq.heappush(q, (cost, node[0]))
                
dijkstra(1)
print(distances[N])