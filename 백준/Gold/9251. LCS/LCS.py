astr = input()
bstr = input()
n = len(astr)
m = len(bstr)

LCS = [[0 for _ in range(m+1)] for _ in range(n+1)]
result = []

for i in range(1, n+1):
    for j in range(1, m+1):
        if astr[i-1] == bstr[j-1]:
            LCS[i][j] = LCS[i-1][j-1] + 1
        else:
            LCS[i][j] = max(LCS[i][j-1], LCS[i-1][j])
            
cur  = LCS[n][m]     
r, c = n, m  
while 1:
    if cur == 0:
        break
    if cur == LCS[n-1][m]:
        cur = LCS[n-1][m]
        n -= 1
    elif cur == LCS[n][m-1]:
        cur = LCS[n][m-1]
        m -= 1
    else:
        result.append(bstr[m-1])
        cur = LCS[n-1][m-1]
        n-=1
        m-=1
        
print(len(result))    
             
# for i in range(len(result)-1, -1 , -1):
#     print(result[i], end='')