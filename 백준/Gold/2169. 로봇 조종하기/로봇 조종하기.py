N, M = map(int, input().split())
mymap = []
dp = [[0] * M for _ in range(N)]
dx = [0, 0, 1]
dy = [1, -1, 0]

for i in range(N):
    mymap.append(list(map(int, input().split())))
dp[0][0] = mymap[0][0]
for i in range(1, M):
    dp[0][i] = dp[0][i-1] + mymap[0][i]

for i in range(1, N):
    tempArr = [[0] * M for _ in range(2)]
    # 왼 -> 오 : 위 or 왼
    tempArr[0][0] = dp[i-1][0] + mymap[i][0]
    tempArr[1][M-1] = dp[i-1][M-1] + mymap[i][M-1]
    for j in range(1, M):
        t = max(tempArr[0][j-1], dp[i-1][j]) 
        tempArr[0][j] = t + mymap[i][j]
    # 오 -> 왼 : 위 or 오
    for j in range(M-2, -1, -1):
        tempArr[1][j] = max(tempArr[1][j+1], dp[i-1][j]) + mymap[i][j]
    
    for j in range(M):
        dp[i][j] = max(tempArr[0][j],tempArr[1][j] )

# for i in range(N):
#     print(dp[i])

print(dp[N-1][M-1])