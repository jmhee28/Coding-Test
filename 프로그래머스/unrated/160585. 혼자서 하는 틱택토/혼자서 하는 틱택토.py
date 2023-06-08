dx = [0, 1, 1, 1]
dy = [1, 0, 1, -1]
tictack = []


def winCnt(x, y, player):
    cnt = 0
    for i in range(4):
        d = i
        win = True
        pcnt = 0
        for j in range(3):
            nx = x + dx[d] * j
            ny = y + dy[d] * j
            if 0 <= nx < 3 and 0 <= ny < 3:
                if tictack[nx][ny] != player:
                    win = False
                    break
                else:
                    pcnt += 1
        if win == True and pcnt == 3:
            cnt += 1
    return cnt


def solution(board):
    answer = -1
    winDict = {}
    cntDict = {}
    winDict["X"] = 0
    winDict["O"] = 0
    cntDict["X"] = 0
    cntDict["O"] = 0
    for i in range(3):
        tictack.append(list(board[i]))
    for i in range(3):
        for j in range(3):
            player = tictack[i][j]
            if player != ".":
                cntDict[player] += 1
                winDict[player] += winCnt(i, j, player)
    if cntDict["O"] + cntDict["X"] == 9 and cntDict["O"] - cntDict["X"] != 1:
        answer = 0
    elif cntDict["O"] - cntDict["X"] > 1 or cntDict["O"] - cntDict["X"] < 0:
        answer = 0
    elif winDict["O"] == 2 and winDict["X"] == 0 and cntDict["O"] - cntDict["X"] == 1:
        answer = 1
    elif winDict["O"] + winDict["X"] > 1:
        answer = 0
    elif winDict["O"] == 1 and cntDict["O"] - cntDict["X"] != 1:
            answer = 0
    elif winDict["X"] == 1 and cntDict["O"] != cntDict["X"]:
        answer = 0
    else:
        answer = 1
    return answer


