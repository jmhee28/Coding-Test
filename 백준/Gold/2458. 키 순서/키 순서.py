import sys
INF = sys.maxsize

N, M = map(int, input().split())
graph = [[False] * (N+1) for _ in range(N+1)]


for i in range(M):
    a, b = map(int, input().split())
    graph[a][b] = True
  
for i in range(N + 1):
    graph[i][i] = True
    
for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if graph[i][k] and graph[k][j]:
                graph[i][j] = True
                
cnt = [0] * (N+1)               
for i in range(1, N+1):
        for j in range(1, N+1):
            if graph[i][j] or graph[j][i]:
                cnt[i] += 1

answer = 0
for i in range(1, N+1):
    if cnt[i] == N:
        answer += 1
print(answer)
    
