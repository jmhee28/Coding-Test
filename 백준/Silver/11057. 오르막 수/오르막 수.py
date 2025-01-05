n = int(input())

dp = [[0] * (10) for _ in range(n+1)]
dp[1][0] = 1

for i in range(1, 10):
    dp[1][i] = 1 + dp[1][i-1]
    
if n > 1:
    for i in range(2, n+1):
        for j in range(10):
            if j == 0:
                dp[i][j] = dp[i-1][9]
            else:
                dp[i][j] = dp[i-1][9] - dp[i-1][j-1] + dp[i][j-1]

print(dp[n][9] % 10007)