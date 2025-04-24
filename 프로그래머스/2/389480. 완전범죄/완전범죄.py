def solution(info, n, m):
    answer = 0
    k = len(info)
    dp = [[n for _ in range(m)] for _ in range(k+1)]
    dp[0][0] = 0
    for i in range(1, k+1):
        ascore = info[i-1][0]
        bscore = info[i-1][1]
        for j in range(m):
            dp[i][j] = min(dp[i][j], dp[i-1][j] + ascore)
            if j + bscore < m:
                dp[i][j + bscore] = min(dp[i][j + bscore], dp[i-1][j])
    answer = n
    for j in range(m):
        answer = min(answer, dp[k][j])
    if answer >= n:
        return -1
    return answer

# solution([[1, 2], [2, 3], [2, 1]], 4, 4)