def solution(friends, gifts):
    answer = 0
    n = len(friends)
    recieved = [0] * n
    gave = [0] * n
    indexs = [0] * n
    nextGifts = [0] * n
    currentGifts = [[0] * n for _ in range(n)] 
    
    dict = {}
    idx = 0
    for friend in friends:
        dict[friend] = idx
        idx += 1
        
    for gift in gifts:
        giver, reciever = gift.split()
        giverIdx = dict[giver]
        recieverIdx = dict[reciever]
        gave[giverIdx] += 1
        recieved[recieverIdx] += 1
        currentGifts[giverIdx][recieverIdx] += 1
        
    for i in range(n):
        indexs[i] = gave[i] - recieved[i]
        
    for i in range(n-1):
        for j in range(i+1, n):
            if currentGifts[i][j] > currentGifts[j][i]:
                nextGifts[i] += 1
            elif currentGifts[i][j] < currentGifts[j][i]:
                nextGifts[j] += 1
            else:
                if indexs[i] > indexs[j]:
                    nextGifts[i] += 1
                elif indexs[i] < indexs[j]:
                    nextGifts[j] += 1
    answer = max(nextGifts)
    return answer