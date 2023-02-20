from datetime import date
def solution(today, terms, privacies):
    answer = []
    today = list(map(int, today.split(".")))
    today = date(today[0], today[1], today[2])
    
    termdates = {} # A: 6
    for term in terms:
        term = term.split()
        termdates[term[0]] = int(term[1])
    for i in range(len(privacies)):
        year, month , day = 0,0,0
        priv = privacies[i].split(" ")
        
        term = priv[1] #약관 종류
        valid = termdates[term] #유효기간
        
        dates = list(map(int, priv[0].split('.')))
        year = dates[0]
        afterM =  dates[1] + valid 
        year += afterM // 12
        
        if dates[2] == 1:
            if afterM % 12 == 0:
                afterM = afterM % 12 - 1
                year -= 1
            else:
                afterM = afterM % 12 - 1
        else:
            afterM = afterM % 12
        
        if afterM == 0:
            afterM = 12
            year -=1
        elif afterM < 0:
            afterM = 12 + afterM
            
        if dates[2] == 1:
            day = 28
        else:
            day = dates[2] - 1
            
        # expire = [year, afterM, day]
        expire = date(year, afterM, day)
        
        print(expire) 
        if today > expire:
            answer.append(i+1)
#         for j in range(3):
#             if today[j] > expire[j]:
#                 answer.append(i+1)
#                 break
            
            
    return answer

