

#겨울
## S2D2가 땅을 돌아다니면서 땅에 양분을 추가한다. 
## 각 칸에 추가되는 양분의 양은 A[r][c]이고, 입력으로 주어진다.

# K년이 지난 후 상도의 땅에 살아있는 나무의 개수를 구하는 프로그램을 작성하시오.
import sys
import heapq
import copy
from collections import deque

input = sys.stdin.readline

dx = [1, -1, 0, 0, 1, 1, -1, -1 ]
dy = [0, 0, 1, -1, 1, -1, 1, -1 ]

N, M, K = map(int, input().split())
nutritions = [ [5 for _ in range(N)] for _ in range(N)]
orgNutritions = []
field = [[deque() for _ in range(N)] for _ in range(N)] # 나무 나이 저장 나무 죽으면 팝

for i in range(N):
    a = list(map(int, input().split()))
    orgNutritions.append(a)
    
for i in range(M):
    x, y, z = map(int, input().split()) # (x, y) : 나무 위치, z: 나무의 나이
    field[x-1][y-1].append(z) # 나이 어린 나무가 우선

        
def age():
    global field, nutritions
    # 봄
    ## 나무가 자신의 나이만큼 양분을 먹고, 나이가 1 증가한다. 
    ## 각각의 나무는 나무가 있는 1×1 크기의 칸에 있는 양분만 먹을 수 있다.
    ## 하나의 칸에 여러 개의 나무가 있다면, 나이가 어린 나무부터 양분을 먹는다. 
    ## 만약, 땅에 양분이 부족해 자신의 나이만큼 양분을 먹을 수 없는 나무는 양분을 먹지 못하고 즉시 죽는다.

    for i in range(N):
        for j in range(N):
            alive = deque()
            dead_nutrition = 0
            trees = field[i][j]
            for age in trees:
                if nutritions[i][j] >= age:
                    nutritions[i][j] -= age
                    alive.append(age + 1)
                else:
                    dead_nutrition += age // 2
            field[i][j] = alive
            nutritions[i][j] += dead_nutrition
    
    # 가을
    ## 나무가 번식한다. 번식하는 나무는 나이가 5의 배수이어야 하며, 인접한 8개의 칸에 나이가 1인 나무가 생긴다. 
    ## 어떤 칸 (r, c)와 인접한 칸은 (r-1, c-1), (r-1, c), (r-1, c+1), (r, c-1), (r, c+1), (r+1, c-1), (r+1, c), (r+1, c+1) 이다. 
    ## 상도의 땅을 벗어나는 칸에는 나무가 생기지 않는다.
    to_grow = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(len(field[i][j])):
                if field[i][j][k] % 5 == 0:
                    for d in range(8):
                        nx = i + dx[d]
                        ny = j + dy[d]
                        if 0 <= nx < N and 0 <= ny < N:
                            # field[nx][ny].appendleft(1)
                            to_grow[nx][ny] += 1
               
        #겨울
        ## S2D2가 땅을 돌아다니면서 땅에 양분을 추가한다. 
        ## 각 칸에 추가되는 양분의 양은 A[r][c]이고, 입력으로 주어진다.
            nutritions[i][j] += orgNutritions[i][j]
    for i in range(N):
        for j in range(N):
            field[i][j].extendleft([1] * to_grow[i][j])
            
for _ in range(K):
    age()
    
answer = 0

for i in range(N):
    for j in range(N):
        answer += len(field[i][j])

print(answer)