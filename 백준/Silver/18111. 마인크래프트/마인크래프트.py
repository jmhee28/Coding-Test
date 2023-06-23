import sys

input = sys.stdin.readline
N, M, B = map(int, input().split())
house = []

for i in range(N):
    house.append(list(map(int, input().split())))

ansT = sys.maxsize
ansH = 0
for h in range(257):
    less = 0
    great = 0
    for i in range(N):
        for j in range(M):
            if house[i][j] < h:
                less += h - house[i][j]
            else:
                great += house[i][j] - h
    if B + great >= less:
        time = great * 2 + less
        if ansT >= time:
            ansT = time
            ansH = h
print(ansT, ansH)
