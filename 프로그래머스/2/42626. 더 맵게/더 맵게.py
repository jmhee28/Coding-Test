import heapq

def solution(scoville, K):
    answer = 0

    heapq.heapify(scoville)
    s = 0
    flag = False
    while len(scoville) >= 2:
        s = heapq.heappop(scoville)
        if s >= K:
            flag = True
            break
        ss = heapq.heappop(scoville)
        newS = s + (ss * 2)
        heapq.heappush(scoville, newS)
        answer += 1
    check = heapq.heappop(scoville)
    
    if check < K:
        answer = -1
    
    # print(answer)
    return answer

# solution([0,0,0,0], 1)