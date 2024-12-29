s1 = input()
s2 = input()
s3 = input()

N, M, K = len(s1), len(s2), len(s3)

dp = [[[0] * (N+1) for _ in range(M+1)] for _ in range(K+1)]

for k in range(1, K + 1):
    for m in range(1, M + 1):
        for n in range(1, N + 1):
            if s1[n-1] == s2[m-1] == s3[k-1]:
                dp[k][m][n] = dp[k-1][m-1][n-1] + 1
            else:
                dp[k][m][n] = max(dp[k-1][m][n], dp[k][m-1][n], dp[k][m][n-1])
print(dp[K][M][N])