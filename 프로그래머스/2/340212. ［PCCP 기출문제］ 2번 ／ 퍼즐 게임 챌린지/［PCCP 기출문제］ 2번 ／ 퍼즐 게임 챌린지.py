diffs, times, limit, cnt = [], [], 0, 0
diffTimes = {}
def solution(d, t, l):
    global diffs, times, limit, diffTimes, cnt
    diffs, times, limit = d, t, l
    diffTimes = zip(diffs, times)

    answer = 0
    cnt = len(diffs)
    level_end = 100000
    level_start = 1
    answer = binary_search(level_start, level_end)
    return answer

def binary_search(start, end):
    target = 0
    while start <= end :
        mid = (start + end) // 2 
        spent = spendTime(mid)
        if spent > limit:
            start = mid + 1
        else:
            end = mid - 1
            target = mid
    return target

def spendTime(level):
    spent = 0
    firstTime = times[0]
    spent += firstTime
    for i in range(1, cnt):
        diff, time = diffs[i], times[i]
        prevDiff, prevTime = diffs[i-1], times[i-1]
        if diff <= level:
            spent += time
        else:
            errorTime = diff - level
            spent += (time + prevTime) * errorTime + time
        if spent > limit:
            return spent
    return spent
