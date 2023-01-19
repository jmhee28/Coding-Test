def solution(N, stages):
    answer = []
    M = len(stages) #유저 수
    fails = []
    for i in range(1, N+1):
        fail = 0
        success = 0
        for stage in stages:
            if stage == i:
                fail += 1
            elif stage > i:
                success += 1
        failrate = 0
        if (success+fail) != 0:
            failrate = fail / (success+fail)
        fails.append(( failrate, (-1)*i))
    fails.sort(key = lambda x: (x[0], x[1]), reverse = True)
    # print(fail)
    for f in fails:
        answer.append((-1)*f[1])
    return answer