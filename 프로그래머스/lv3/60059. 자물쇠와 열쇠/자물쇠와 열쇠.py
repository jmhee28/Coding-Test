import copy
def solution(key, lock):
    answer = True
    M = len(key)
    N = len(lock)
   
    mlen = 2 * M + (N-2)
    tmap = [[-1 for i in range(mlen)] for j in range(mlen)]

    for i in range(M-1, M - 1 + N):
        for j in range(M-1, M - 1 + N):
            tmap[i][j] = lock[i - M + 1][j - M + 1]

    for x in range(0, mlen - M + 1):
        for y in range(0,mlen - M + 1 ):
            for i in range(4):
                aftermap = insertkey(x,y,key, tmap, M)
                
                if check(aftermap, N, M) == True:
                    return True
                key = rotate(key, M)

    return False

def rotate(key, M):
    ret =[[0 for i in range(M)] for j in range(M)]
    for i in range(M):
        c = M - i -1
        for j in range(M):
            ret[j][c] = key[i][j]
    return ret

def insertkey(x, y, key, kmap, M):
    retmap =copy.deepcopy(kmap)
    for i in range(x, x+M):
        for j in range(y, y+M):
            if retmap[i][j] != -1:
                # if retmap[i][j] + key[i-x][j-y] == 1:
                    retmap[i][j] += key[i-x][j-y]
    return retmap

def check(fmap, N, M):
    for i in range(M-1, M - 1 + N):
        for j in range(M-1, M - 1 + N):
            if fmap[i][j] != 1:
                return False
    return True





lock = [[1,1,1], [1,1,1], [1,1,1]]
key = [[1,1,1], [1,1,1], [1,1,1],]
print(solution(key, lock))