def solution(files):
    answer = []
    lst =[]
    for i in range(len(files)):
        s = 0
        e = 0
        for j in range(len(files[i])):
            if files[i][j].isdigit() and s == 0:
                s = j
                e = j
                while 1:
                    if e < len(files[i]) - 1 and not files[i][e+1].isdigit():
                        break
                    if e-s >= 5:
                        break
                    else:
                        e+=1
                break

        head = files[i][0:s]
        num = files[i][s:e+1]
        lst.append((i, head.lower(), int(num)))
    
    lst.sort(key = lambda x: (x[1], x[2]))   
    
    for i in lst:
        answer.append(files[i[0]])
    return answer