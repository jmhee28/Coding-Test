import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize
n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for i in range(m):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))    

def dijstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q :
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

a, b = map(int, input().split())
dijstra(a)
print(distance[b])