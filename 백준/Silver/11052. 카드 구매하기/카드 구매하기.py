import copy

n = int(input())
pays = [0] + list(map(int, input().split()))

dp = copy.deepcopy(pays)



for i in range(1, n + 1):
    dp[i] = max(dp[i], dp[1] * i)
    for j in range(1, i):
        dp[i] = max(dp[j] + dp[i-j], dp[i])

print(dp[n])