n = int(input())
mod = 1000000000
dp = [[0] * 11 for _ in range(101)]

dp[1] = [1] * 10

for i in range(1, 10):
    dp[2][i] = 2
dp[2][9] = 1

if n > 2:
    for i in range(3, n+1):
        for j in range(1, 10):
            if j == 1:
                dp[i][j] = (dp[i-2][1] + dp[i-1][2])
            else:
                dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1])
                

answer = 0

for i in range(1, 10):
    answer += dp[n][i]
    
print(answer % mod)
