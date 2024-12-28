n, t = map(int, input().split())

times = []
scores = []

for i in range(n):
    k, s = map(int, input().split())
    times.append(k)
    scores.append(s)

dp = [0] * (t + 1)
for i in range(n):
    for j in range(t, 0, -1):
        if times[i] <= j:
            dp[j] = max(dp[j], dp[j - times[i]] + scores[i])
            
print(dp[t])
