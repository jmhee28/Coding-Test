def solution(s):
    N = len(s)
    answer = N
    cut = 1
    ansstr = ''
    while 1:
        lst = []
        if cut == N + 1:
            break
        for i in range(0,N, cut):
            lst.append(s[i:i+cut])
        dict ={}
        anslst =''
        for j in range(len(lst)-1):
            
            if lst[j] == lst[j+1]:
                if lst[j] not in dict:
                    dict[lst[j]] = 2
                else:
                    dict[lst[j]] += 1
            
            elif lst[j] != lst[j+1]:
                if lst[j] in dict:
                    anslst+=lst[j]+str(dict[lst[j]])
                    dict.pop(lst[j], None)
                else:
                    anslst+=lst[j]
            
        if len(dict) != 0:
            for k, v in dict.items():
                anslst+=k + str(v)
        else:
            anslst+=lst[len(lst)-1]  
        cut += 1
        answer = min(len(anslst), answer)
    return answer

s ="aabbaccc"
print(solution(s))