dict = {}
def solution(n, words):
    answer = []
    idx = 0
    turn = 0
    a = words[0]
    dict[a] = 1
    
    for i in range(1, len(words)):
        b = words[i]
        if b in dict:
            if (i+1) % n == 0:
                turn = (i+1) // n
            else:
                turn = ((i+1) // n) +1
            idx = i % n + 1
            break
        
        if a[-1] != b[0]:
            if (i+1) % n == 0:
                turn = (i+1) // n
            else:
                turn = ((i+1) // n) +1
            idx = i % n + 1
            break
            
        dict[b] = 1
        a = b
        
    if idx == 0 and turn == 0:
        return [0,0]
    
    answer.append(idx)
    answer.append(turn)
    
    return answer