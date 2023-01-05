import sys



T = int(input())
for i in range(T):
    N = int(input())
    score = []
    for j in range(N):
        a, b = map(int, sys.stdin.readline().split())
        score.append((a,b))
    score.sort()
    # print(score)

    cur = score[0]
    cnt = 1
    for k in range(1,N):
        if score[k][1] < cur[1]:
            cur = score[k]
            cnt += 1
    print(cnt)
        