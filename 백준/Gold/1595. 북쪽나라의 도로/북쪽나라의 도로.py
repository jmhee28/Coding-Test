import sys


MAX = 10000
graph = [[] for _ in range(MAX)]


while True:
    try:
        A, B, C= map(int, input().split())
        graph[A].append((B, C))
        graph[B].append((A, C))
        
    except:
        break



def dfs(cur, visited, distances):
    visited[cur] = True
    for node, cost in graph[cur]:
        if not visited[node]:
            distances[node] = distances[cur] + cost
            dfs(node, visited, distances)
            
answer = 0
for i in range(MAX):
    visited = [False] * (MAX)
    distances = [0] * (MAX)
    if len(graph[i]) > 0:
        dfs(i, visited, distances)
        maxDist = max(distances)
        answer = max(maxDist, answer)
print(answer)