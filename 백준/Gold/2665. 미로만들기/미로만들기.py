import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

rooms = []
n = int(input())
distance = [[INF] * n for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(n):
    strarr = input().strip()
    room = [(int(ch) ^ 1) for ch in strarr]
    rooms.append(room)
    
def dijkstra(start):
    x, y = start
    q = []
    heapq.heappush(q, (0, start))
    distance[x][y] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        x, y = now
        if distance[x][y] < dist:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                cost = dist + rooms[nx][ny]
                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost
                    heapq.heappush(q, (cost, (nx, ny)))
        
dijkstra((0,0))
print(distance[n-1][n-1])