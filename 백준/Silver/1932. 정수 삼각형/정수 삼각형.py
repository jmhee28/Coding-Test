n = int(input())
triangle = []
dp = [[0 for i in range(n)] for j in range(n)]

for i in range(n):
    triangle.append(list(map(int, input().split())))

dp[n-1] = triangle[n-1]

for i in range(n-2, -1, -1):
    m = i + 1
    for j in range(m):
        dp[i][j] = triangle[i][j] + max(dp[i+1][j], dp[i+1][j+1])
print(dp[0][0])