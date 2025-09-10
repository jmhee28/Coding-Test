import sys
INF = sys.maxsize

D, P = map(int, input().split())
lengths = []
capacities = []
dp = [0 for _ in range(D+1)]

for i in range(P):
    L, C = map(int, input().split())
    lengths.append(L)
    capacities.append(C) 
dp[0] = INF

for i in range(P):
    for j in range(D, lengths[i] -1, -1):
      dp[j] = max(dp[j], min(dp[j - lengths[i]], capacities[i]))
print(dp[D])