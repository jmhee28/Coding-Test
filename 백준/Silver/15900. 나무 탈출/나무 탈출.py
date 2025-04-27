import sys
input = sys.stdin.readline
sys.setrecursionlimit(600000)
N = int(input())
graph = [[] for _ in range(N+1)]
distances = [0] * (N+1)
visited = [False] * (N+1)
count = 0
# 루트에서 리프까지 홀수이면 성원 승, 짝수면 형석 승
# 리프노드 -> 리스트 길이가 1
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(cur):
    global visited, distances
    visited[cur] = True
    for node in graph[cur]:
        if visited[node] == False:
            distances[node] = distances[cur] + 1
            dfs(node)
            
dfs(1)

for i in range(2, N+1):
    if len(graph[i]) == 1:
        count += distances[i]

answers = ["No", "Yes"]
print(answers[count % 2])