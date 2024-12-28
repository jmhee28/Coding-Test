import sys
input = sys.stdin.readline

while True:
    
    N, M = map(float, input().split())
    N = int(N)
    M = int(M * 100 + 0.5)
    if N == 0 and M == 0:
        break
    calories = []
    prices = []
    
    for i in range(N):
        c, p = map(float, input().split())
        calories.append(int(c))
        prices.append(int(p * 100 + 0.5))
    dp = [0] * (M+1)
    
    for i in range(N):
        for j in range(1, M + 1):
            if prices[i] <= j:
                dp[j] = max(dp[j], dp[j-prices[i]] + calories[i])
            
    print(dp[M])            