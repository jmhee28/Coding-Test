import sys
from itertools import combinations

input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
N = int(input())
board = []
answer = sys.maxsize


def check(rc):
    visited = []
    total = 0
    for i in rc:
        x, y = i
        temp = board[x][y]
        visited.append(i)
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if (nx, ny) not in visited:
                temp += board[nx][ny]
                visited.append((nx, ny))
            else:
                return -1
        total += temp
    return total


for i in range(N):
    board.append(list(map(int, input().split())))
flowers = [(r, c) for r in range(1, N - 1) for c in range(1, N - 1)]

for rc in combinations(flowers, 3):
    ret = check(rc)
    if ret != -1:
        answer = min(ret, answer)
print(answer)