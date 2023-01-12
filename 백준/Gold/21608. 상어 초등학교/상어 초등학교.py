
def getnear(r, c, N):
    cand = [(r-1, c), (r, c-1), (r+1, c),(r, c+1)]
    near = []
    for i in cand:
        if 0 <= i[0] < N and 0 <= i[1] < N:
            near.append(i)
    return near
def getSatisfaction(like):
    if like == 0:
        return 0
    elif like == 1:
        return 1
    elif like == 2:
        return 10
    elif like == 3:
        return 100
    elif like == 4:
        return 1000
    

answer = 0
N = int(input())
positions = [[0 for _ in range(N)] for _ in range(N)]
students = []
prefer = {}
for i in range(N ** 2):
    lst =list(map(int, input().split()))
    students.append(lst)
    prefer[lst[0]] = lst[1:]


for i in range(0, N**2):
    student = students[i][0]
    likestudents = students[i][1:]
    info = []
    for r in range(N):
        for c in range(N):
            nears = getnear(r,c,N)
            like = 0 #좋아하는 학생수
            vacants = 0 #비어있는 자리 수
            if positions[r][c] == 0:
                for near in nears: #인접한 곳 검사
                    if positions[near[0]][near[1]] in likestudents:
                        like += 1
                    elif positions[near[0]][near[1]] == 0:
                        vacants += 1
                info.append((like, vacants, -r, -c))
    info.sort(key = lambda x:(x[0], x[1], x[2], x[3] ), reverse=True)
    selected = info[0]
    pos = (-1 * selected[2]), (-1* selected[3])
    positions[pos[0]][pos[1]] = student

for i in range(N):
    for j in range(N):
        curstudent = positions[i][j]
        curnear = getnear(i, j, N)
        cnt = 0
        for n in curnear:
            if positions[n[0]][n[1]] in prefer[curstudent]:
                cnt += 1
        answer += getSatisfaction(cnt)
print(answer)