import sys
input = sys.stdin.readline

n = int(input()) # 50000 이하
trains = list(map(int, input().split())) # trains[i] <= 100
maxDrawCnt = int(input())

prefixSum = [0] * n
prefixSum[0] = trains[0]

for i in range(1, n):
    prefixSum[i] = prefixSum[i-1] + trains[i]

dp = [[0] * n for _ in range(4)]

for i in range(maxDrawCnt):
    dp[1][i] = prefixSum[i]

for i in range(maxDrawCnt, n):
    curPrefixSum = prefixSum[i] - prefixSum[i - maxDrawCnt]
    dp[1][i] = max(dp[1][i-1], curPrefixSum)
    
for i in range(2, 4):
    for j in range(n):
        if j < maxDrawCnt:
            dp[i][j] = dp[i-1][j]
            continue
        
        dp[i][j] = max(
            dp[i-1][j-maxDrawCnt] + (prefixSum[j] - prefixSum[j-maxDrawCnt]), 
            dp[i-1][j-1] + trains[j],
            dp[i][j-1]
        )

answer = dp[3][n-1]
print(answer)