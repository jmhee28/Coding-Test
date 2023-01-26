from collections import deque
import sys
n, m = map(int, sys.stdin.readline().split())

holes = set()

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    holes.add((a,b))


queue = deque()
queue.append([0,0,0])

ans = -1
while queue:
    a, b, cnt = queue.popleft()
    if b == m:
        ans = cnt
        break

    for i in range(-2, 3):
        for j in range(-2, 3):
            x = a + i
            y = b + j
            if (x, y) in holes:
                holes.remove((x,y))
                queue.append([x, y, cnt + 1])

        
print(ans)