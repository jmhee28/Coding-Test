def solution(clothes):
    answer = 1
    dict = {}
    for i in clothes:
        if i[1] not in dict:
            dict[i[1]] = [i[0]]
        else:
            dict[i[1]].append(i[0])
    
    for key in dict:
        answer *= len(dict[key])+1
    
        
    return answer-1