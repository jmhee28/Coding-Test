import sys
input = sys.stdin.readline

n = int(input())
time = []
pos = []
for i in range(n):
    t, p = map(int, input().split())
    time.append(t)
    pos.append(p)

max_val = 0
dp = [0] * (n+1)

for i in range(n-1, -1, -1):
    t = time[i] + i
    if t <= n:
        dp[i] = max(dp[t]+ pos[i], max_val)
        max_val = dp[i]
    else:
        dp[i] = max_val
print(max_val)