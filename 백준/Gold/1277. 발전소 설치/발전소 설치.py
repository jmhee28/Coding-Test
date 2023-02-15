import sys
import heapq
import math
input = sys.stdin.readline
n,w = map(int, input().split())
m = float(input())
INF = int(1e9)
distance = [INF] * n
locations = []
graph = [[] for _ in range(n)]
for _ in range(n):
    x, y = map(int, input().split())
    locations.append((x, y))

for _ in range(w):
    a, b = map(int, input().split())
    a -= 1
    b-=1
    graph[a].append((b,0))
    graph[b].append((a,0))
for i in range(0, n):
    for j in range(i, n):
        if j not in graph[i]:
            nx, ny = locations[j]
            x, y = locations[i]
            d = math.sqrt(((nx-x)**2) + ((ny-y)**2))
            if d <= m:
                graph[i].append((j, d))
                graph[j].append((i, d))


q = []
heapq.heappush(q, (0,0))
distance[0] = 0
while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
        continue

    for j in graph[now]:
        cost = dist + j[1]
        if cost < distance[j[0]]:
            distance[j[0]] = cost
            heapq.heappush(q, (cost, j[0]))
       
# print(distance)
print(int(distance[n-1]*1000))

# 9 2
# 2.0
# 0 0
# 0 1
# 1 1
# 2 1
# 2 2
# 3 2
# 3 3
# 4 1
# 4 3
# 2 3
# 3 4