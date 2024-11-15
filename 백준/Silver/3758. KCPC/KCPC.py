T  = int(input())
for t in range(T):
    # N: 팀의 갯수, K: 문제의 갯수, M: 로그 엔트리 개수
    N, K, idt, M = map(int, input().split())
    # 제출 시간
    # 제출 횟수
    # team[i][j] = [s, t, c] 점수, 제출 시간, 제출 횟수
    # teamInfo[i] = [최종 점수, 마지막 제출 시간, 최종제출 횟수]
    # allTeamInfo = [ID, 최종 점수, 마지막 제출 시간, 최종제출 횟수]
    team = [[[0, 0, 0] for _ in range(K + 1)] for _ in range(N+1)]
    lastSubmits = [[0] for _ in range(N+1)]
    allTeamInfo = []
    for m in range(M):
        # 팀 ID i, 문제 번호 j, 획득한 점수 s
        i, j, s = map(int, input().split())
        team[i][j][0] = max(team[i][j][0], s)
        team[i][j][1] = m
        team[i][j][2] += 1
        lastSubmits[i] = m
    
    for n in range(1, N+1):
        totalScore = 0
        totalSubmit = 0
        for k in range(1, K + 1):
            totalScore += team[n][k][0]
            totalSubmit += team[n][k][2]
        allTeamInfo.append([n, -totalScore, lastSubmits[n], totalSubmit])
    allTeamInfo.sort(key= lambda x: (x[1], x[3], x[2]))
    rank = 1

    for teamInfo in allTeamInfo:
        if teamInfo[0] == idt:
            print(rank)
            break
        else:
            rank += 1