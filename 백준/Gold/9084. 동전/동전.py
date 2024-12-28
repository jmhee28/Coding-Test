T = int(input())

for t in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    M = int(input())
    
    dp = [0] * (M + 1)
    
    dp[0] = 1
    
    for i in range(N):
        for j in range(coins[i], M + 1):
            dp[j] += dp[j - coins[i]]
    print(dp[M])
