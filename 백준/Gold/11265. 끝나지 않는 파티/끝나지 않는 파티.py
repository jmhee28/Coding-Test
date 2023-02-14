import sys
input = sys.stdin.readline
INF = int(1e9)
n, m = map(int, input().split())
graph = [[] for i in range(n+1)]
costumer = []
for i in range(n):
    graph[i] = list(map(int, input().split()))


for k in range(n):
    for a in range(n):
        for b in range(n):
            if graph[a][b] > (graph[a][k]+graph[k][b]):
                graph[a][b] = graph[a][k]+graph[k][b]


for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    if graph[a][b] <= c:
        print("Enjoy other party")
    else:
        print("Stay here")
