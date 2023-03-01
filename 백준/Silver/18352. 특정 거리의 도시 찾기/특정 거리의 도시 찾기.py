from collections import deque

n,m,k,x = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

distance = [-1] * ( n + 1 )

q = deque()
distance[x] = 0
q.append(x)

while q:
    a = q.popleft()
    for i in graph[a]:
        if distance[i] == -1:
            distance[i] = distance[a] + 1
            q.append(i)
flag = False
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        flag = True
if flag == False:
    print(-1)
