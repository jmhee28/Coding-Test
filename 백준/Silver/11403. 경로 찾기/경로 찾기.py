import sys
input = sys.stdin.readline

n = int(input())
INF = int(1e9)
graph = [[] for i in range(n)]

for i in range(n):
    lst = list(map(int,input().split()))
    for j in range(n):
        if lst[j] == 0:
            lst[j] = INF
    graph[i] = lst

for k in range(n):
    for a in range(n):
        for b in range(n):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])
for i in range(n):
    for j in range(n):
        if graph[i][j] < INF:
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()