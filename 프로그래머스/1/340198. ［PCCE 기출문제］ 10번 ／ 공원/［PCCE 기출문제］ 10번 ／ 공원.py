n = 0
m = 0
gpark = []
def search(x, y):
    length = 1
    while True:
        for i in range(x, x + length):
            for j in range(y, y + length):
                if not (0 <= i < n and 0 <= j < m and gpark[i][j] == "-1"):
                    return length
        length += 1
    return length

def solution(mats, park):
    global n, m, gpark
    gpark = park
    answer = -1
    max_len = -1
    n = len(park)
    m = len(park[0])
    
    for i in range(n):
        for j in range(m):
            if park[i][j] == "-1":
                cur_len = search(i, j) - 1
                max_len = max(max_len, cur_len)
    
    mats.sort(reverse=True)
    
    for mat in mats:
        if mat <= max_len:
            return mat
    
    return answer