def getdistance(idx, N, lst):
    dis = 0
    for i in range(N):
        dis += abs(lst[idx] - lst[i])
    return dis

N = int(input())
lst = list(map(int, input().split()))
lst.sort()

if N == 1:
    print(lst[0])
else:
    dis = getdistance(N//2, N, lst)
    sdis = getdistance(N//2-1, N, lst)
    if dis < sdis:
        print(lst[N//2])
    else:
        print(lst[N//2-1])