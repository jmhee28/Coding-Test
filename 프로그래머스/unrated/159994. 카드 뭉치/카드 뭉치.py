def solution(cards1, cards2, goal):
    oneIdx = 0
    twoIdx = 0
    one = len(cards1)
    two = len(cards2)
    n = len(goal)
    visited = [0 for _ in range(n)]

    for i in range(n):
        word = goal[i]
        flag = False
        for j in range(oneIdx, one):
            if word == cards1[j]:
                oneIdx = j + 1
                visited[i] = 1
                flag = True
                break
            else:
                break
        if flag == False:
            for k in range(twoIdx, two):
                if word == cards2[k]:
                    twoIdx = k + 1
                    visited[i] = 1
                    flag = True
                    break
                else:
                    break
        if flag == False:
            break
    if sum(visited) == n:
        return "Yes"
    else:
        return "No"