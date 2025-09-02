def add_minutes(time, minutes=10):
    h, m = divmod(time, 100)
    m += minutes
    if m >= 60:
        h += m // 60
        m %= 60
    return h * 100 + m

def solution(schedules, timelogs, startday):
    answer = 0
    day = startday
    n = len(schedules)
    m = len(timelogs[0])
    
    for i in range(n):
        timeLimit = add_minutes(schedules[i])
        flag = True
        for j in range(m): # day
            curday = (day + j - 1) % 7
            if curday >= 5:
                continue
            if timeLimit < timelogs[i][j]:
                flag = False
                break
        if flag:
            answer += 1
            
    # print(answer)
    return answer



