from bisect import bisect_left
n = int(input())
arr =list( map(int, input().split()))
ans = [arr[0]]

for i in range(1, n):
    if arr[i] > ans[-1]:
        ans.append(arr[i])
    else:
        idx = bisect_left(ans, arr[i])
        ans[idx] = arr[i]

print(len(ans))
