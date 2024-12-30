n = int(input())
board = []

# 메모 배열 초기화
memo = [[-1] * n for _ in range(n)]

for i in range(n):
    board.append(list(map(int, input().split())))

# DFS 함수 정의
def dfs(x, y):
    # 도착 지점에 도달하면 경로 하나 추가
    if x == n - 1 and y == n - 1:
        return 1
    
    # 이미 계산된 값이 있으면 반환
    if memo[x][y] != -1:
        return memo[x][y]
    
    memo[x][y] = 0  # 현재 위치에서 시작하는 경로 수 초기화
    distance = board[x][y]
    
    # 오른쪽 이동
    if y + distance < n:
        memo[x][y] += dfs(x, y + distance)
    # 아래로 이동
    if x + distance < n:
        memo[x][y] += dfs(x + distance, y)
    
    return memo[x][y]

# 시작점에서 DFS 실행
print(dfs(0, 0))