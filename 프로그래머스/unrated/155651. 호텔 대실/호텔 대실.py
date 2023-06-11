import heapq

def getTime(timeStr):
    time = timeStr.split(":")
    return int(time[0]) * 60 + int(time[1])


def solution(book_time):
    answer = 0
    booklist = []
    n = len(book_time)
    if n == 1:
        return 1
    for book in book_time:
        startTime = getTime(book[0])
        endTime = getTime(book[1]) + 10
        heapq.heappush(booklist, (startTime, endTime))
    
    while booklist:
        answer+= 1
        curStart, curEnd = heapq.heappop(booklist)
        q = []
        while booklist:
            start, end = heapq.heappop(booklist)
            if curEnd > start:
                q.append((start, end))
            else:
                curEnd = end
        heapq.heapify(q)
        booklist = q
    return answer