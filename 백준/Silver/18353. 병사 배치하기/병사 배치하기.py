import sys
from bisect import bisect_left

input = sys.stdin.readline
n = int(input())
lst = list(map(int, input().split()))
lst.reverse()
dp = [1]
x = [lst[0]]

for i in range(1, n):
    if lst[i] > x[-1]:
        x.append(lst[i])
        dp.append(dp[-1]+1)
    else:
        idx = bisect_left(x, lst[i])
        x[idx] = lst[i]
print(n- len(x))