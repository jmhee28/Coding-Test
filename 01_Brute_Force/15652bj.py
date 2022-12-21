def dfs(cnt):
    if cnt == M:
        print(*arr)
        return
    else:
        for i in range(1, N+1):
            if cnt > 0 and arr[cnt-1] <= i:
                arr[cnt] = i
                dfs(cnt+1)
            elif cnt == 0:
                arr[cnt] = i
                dfs(cnt+1)

N, M = map(int, input().split())
arr = [0 for _ in range(M)]
dfs(0)   