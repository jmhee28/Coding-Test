def solution(genres, plays):
    dict = {}
    playlst = {}
    gset = set(genres)
    for i in gset:
        dict[i] = 0
        playlst[i] =[]
    N = len(genres)
    
    for i in range(N):
        dict[genres[i]] += plays[i]
        playlst[genres[i]].append((i, plays[i]))
        
    dict = sorted(dict.items(), key = lambda item: item[1], reverse = True)
    
    answer = []
    for k,v in dict:
        lst = list(playlst[k])
        lst.sort(key = lambda x:x[1], reverse= True)
        if len(lst) ==1:
            answer.append(lst[0][0])
        else:
            for i in range(0,2):
                answer.append(lst[i][0])
    return answer