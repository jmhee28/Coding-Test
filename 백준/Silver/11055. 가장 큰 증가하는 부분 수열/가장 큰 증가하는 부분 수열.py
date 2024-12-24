import copy

n = int(input())

arr = list(map(int, input().split()))
dp = copy.deepcopy(arr)

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(arr[i] + dp[j], dp[i])
            
print(max(dp))