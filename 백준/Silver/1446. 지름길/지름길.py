import sys
input = sys.stdin.readline
n, dest= map(int, input().split())
INF = int(1e9)
dists = [INF] * (dest+1)
sho = [[] for _ in range(dest+1)]
for i in range(n):
    start, end, dist = map(int,input().split())
    if end > dest or (end - start) < dist:
        continue
    sho[end].append((start, dist))

dists[0] = 0

for d in range(1, dest+1):
    a = dists[d-1] + 1
    b = dists[d]
    c = INF
    if len(sho[d]) > 0:
        for s in sho[d]:
            if(len(s) == 0):
                continue
            # print(s)
            start, dist = s
            # print(dist)
            c = min(c, dist + dists[start])
    dists[d] = min(a, b, c)

print(dists[d])