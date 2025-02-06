import sys
import bisect

input = sys.stdin.readline
MAX_SIZE = sys.maxsize

n, h = map(int, input().split())
top = []
bottom = []

for i in range(n):
    num = int(input())
    if i % 2 == 0:
        top.append(num)
    else:
        bottom.append(num)
top.sort()
bottom.sort()

countArr = [0] * (n+1)  
min_obs = MAX_SIZE
tbsize = n//2

for k in range(1, h + 1):
    count = 0
    top_boundary = bisect.bisect_left(top, k)
    bottom_boundary = bisect.bisect_left(bottom, h - k + 1) 
    count += tbsize - top_boundary
    count += tbsize - bottom_boundary 
    countArr[count] += 1
    min_obs = min(min_obs, count)

print(min_obs, countArr[min_obs])