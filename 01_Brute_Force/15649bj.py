def dfs(cnt, visit):
    if cnt == M :
        print(*arr)
        return
    else:
        for i in range(1, N+1):
            if visit[i] == 0:
                arr[cnt] = i
                visit[i] = 1
                dfs(cnt+1, visit)
                visit[i] =0
                
N, M = map(int, input().split())
arr = [0 for _ in range(M)]
visited = [0 for _ in range(N+1)]

dfs(0, visited)   