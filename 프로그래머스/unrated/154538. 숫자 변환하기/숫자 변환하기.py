def solution(x, y, n):
    answer = 0
    INF = float('inf')
    dp = [INF] * (y + 1)
    if x > y:
        return -1
    elif x == y:
        return 0
    dp[x] = 0
    for i in range(x, y + 1):
        if i - n >= x:
            dp[i] = dp[i - n] + 1
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)

    if dp[y] < 1000000:
        return dp[y]
    else:
        return -1


# solution(1, 2, 3)
