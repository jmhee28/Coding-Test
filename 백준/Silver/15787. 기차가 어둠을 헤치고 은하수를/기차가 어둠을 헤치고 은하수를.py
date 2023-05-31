import copy
n, m = map(int, input().split())
trains = [[0 for _ in range(21)] for _ in range(n+1)]

for i in range(m):
    cmd = list(map(int, input().split()))
    command = cmd[0]
    train = cmd[1]
    if len(cmd) == 3:
        idx = cmd[2]
        if command == 1:
            if trains[train][idx] == 0:
                trains[train][idx] = 1
        elif command == 2:
            if trains[train][idx] == 1:
                trains[train][idx] = 0
    else:
        if command == 3:
            temp = copy.deepcopy(trains[train])
            trains[train][1] = 0
            for j in range(2, 21):
                trains[train][j] = temp[j-1]
        elif command == 4:
            temp = copy.deepcopy(trains[train])
            trains[train][20] = 0
            for j in range(1, 20):
                trains[train][j] = temp[j+1]
passed = []
passed.append(trains[1])
cnt = 1
for i in range(2, n+1):
    flag = False
    for p in passed:
        if trains[i] == p:
            flag = True
            break
    if flag == False:
        passed.append(trains[i])
        cnt += 1
print(cnt)
