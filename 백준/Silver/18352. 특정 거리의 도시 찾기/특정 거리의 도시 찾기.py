import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n, m, k, x = map(int, input().split())
distance = [INF] * (n+1)
graph = [[] for i in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))

def dijk(start):
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
                heapq.heappush(q, (cost, i[0]))

dijk(x)
answer = []
for i in range(1, n+1):
    if distance[i] == k:
        answer.append(i)
if len(answer) == 0:
    print(-1)
else:
    answer.sort()
    for i in answer:
        print(i)