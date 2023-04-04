import copy
n = int(input())
onejump=[]
twojump = []
dp = [0 for _ in range(n)]

for i in range(n-1):
    one, two = map(int, input().split())
    onejump.append(one)
    twojump.append(two)

threejump = int(input())

if n > 3:
    dp[0] = 0
    dp[1] = onejump[0]
    dp[2] = twojump[0]

    for i in range(2, n):
        val = min(dp[i-2] + twojump[i-2], dp[i-1] + onejump[i-1])
        dp[i] = val
    ans = dp[n-1]
    elist = [ans]
    for j in range(3, n):
        tdp = copy.deepcopy(dp)
        tdp[j] = tdp[j-3] + threejump
        for k in range(j+1, n):
            tdp[k] = min(tdp[k-2] + twojump[k-2], tdp[k-1] + onejump[k-1])
        elist.append(tdp[n-1])
    print(min(elist))
elif n == 3:
    print(min(sum(onejump), twojump[0]))
elif n == 2:
    print(onejump[0])
elif n == 1:
    print(0)


    

