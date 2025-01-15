import sys
import heapq
input = sys.stdin.readline
INF = 1e9
graph = []
distances = []

def dijkstra(start):
    global distances
    q = []
    heapq.heappush(q, (0, start))
    distances[start][start] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        if distances[start][now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distances[start][i[0]]:
                heapq.heappush(q, (cost, i[0]))
                distances[start][i[0]] = cost
        
        
def execute():
    global graph, distances
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    distances = [[INF] * (n+1) for _ in range(n+1)]
    locations = []
    for i in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b,c))
        graph[b].append((a, c))
    k = int(input())
    locations = list(map(int, input().split()))
    
    # start - locations
    for location in locations:
        dijkstra(location)
    
    answer = -1
    min_sum = INF
    
    for i in range(1, n+1):
        tsum = 0
        for location in locations:
            tsum += distances[location][i]
        if tsum < min_sum:
            min_sum = tsum
            answer = i
    print(answer)


T = int(input())

for t in range(T):
    execute()
