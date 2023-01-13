def solution(cap, n, deliveries, pickups):
    answer = 0
    while len(deliveries) != 0 and deliveries[-1] == 0:
        deliveries.pop()
    while len(pickups) != 0 and pickups[-1] == 0:
        pickups.pop()
    
    while 1:
        if len(deliveries)== 0 and len(pickups)== 0:
            break
        length = max(len(deliveries), len(pickups))
        answer += length * 2

        box = 0
        while len(deliveries) > 0:
            if deliveries[-1] + box <= cap:
                box += deliveries[-1]
                deliveries.pop()
            else:
                deliveries[-1] -= cap - box
                break
        box = 0
        while len(pickups) > 0:
            if pickups[-1] + box <= cap:
                box += pickups[-1]
                pickups.pop()
            else:
                pickups[-1] -= cap - box
                break
    return answer