import sys
input = sys.stdin.readline
INF = int(1e9)
n, m, r = map(int, input().split())
items = []
graph = [[INF for _ in range(n+1)] for _ in range(n+1)]
items = list(map(int, input().split()))

for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a][b] = l
    graph[b][a] = l

for i in range(1, n+1):
    for j in range(1, n+1):   
        if i== j:
            graph[i][j] = 0

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])
answer = 0
for i in range(1, n+1):
    cnt = 0
    for j in range(1, n+1):
        if graph[i][j] <= m:
            cnt += items[j-1]
    answer = max(answer, cnt)
print(answer)
