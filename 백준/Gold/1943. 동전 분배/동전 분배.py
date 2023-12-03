import sys
input = sys.stdin.readline

for t in range(3):
    N = int(input())
    coins = []
    total = 0
    dp = [0] * 100001
    for i in range(N):
        coin, cnt = map(int, input().split())
        coins.append((coin, cnt))
        total += coin * cnt
        for c in range(1, cnt+1):
            dp[c * coin] = 1
        
    if total % 2 != 0:
        print(0)
        continue
    elif dp[total//2] == 1:
        print(1)
        continue
        
    total //= 2

    dp[0] = 1
    for coin, cnt in coins:
        for j in range(total, coin-1, -1):
            if dp[j-coin] == 1:
                for k in range(1, cnt+1):
                    if j - coin + coin * k > total:
                        break
                    dp[j-coin + coin * k] = 1
                    

    print(dp[total])