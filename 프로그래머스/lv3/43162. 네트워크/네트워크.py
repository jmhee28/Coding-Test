N = 0
def solution(n, computers):
    global N
    N = n
    visited = [False] * n
    answer = 0
    for i in range(n):
        if not visited[i]:
            dfs(visited,computers,i)
            answer +=1           
    return answer

def dfs(visited, computers, x):
    visited[x] = True
    for i in range(0,N):
        if computers[x][i] == 1 and not visited[i]:
            dfs(visited, computers,i)

            
    