import heapq
import sys
input = sys.stdin.readline

T = int(input())
graph = []
INF = 1e9
distances = []

def dijkstra(start):
    global graph, distances
    q = []
    heapq.heappush(q, (0, start))
    distances[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        if dist > distances[now]:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distances[i[0]]:
                distances[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    
    
    
for t in range(T):
    n, d, c = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    distances = [INF] * (n+1)
    for _ in range(d):
        a, b, s = map(int, input().split())
        graph[b].append((a, s))
    dijkstra(c)
    cnt = 0
    time = 0
    for i in range(1, n+1):
        if distances[i] != INF:
            time = max(distances[i], time)
            cnt += 1
    print(cnt, time)