s1 = input()
s2 = input()

m = len(s1)
n = len(s2)

dp = [[0] * (n+1) for _ in range(m+1)]

for i in range(1, m+1):
    for j in range(1, n+1):
        if s1[i-1] == s2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

max_cnt = dp[m][n]

result = []

i = m
j = n

while dp[i][j] != 0:
    if dp[i-1][j] == dp[i][j]:
        i -= 1
    elif dp[i][j - 1] == dp[i][j]:
        j -= 1 
    else:
        result.append(s2[j-1])
        i-=1
        j-=1

result.reverse()

print(max_cnt)
for k in result:
    print(k, end='')