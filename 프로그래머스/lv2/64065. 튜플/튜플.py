from collections import Counter
def solution(s):
    answer = []
    s = s.replace('{','')
    s = s.replace('}','')
    # s = s.replace(',','')
    s = s.split(',')
    s = list(map(int, s))
    # print(s)
    s = list(Counter(s).most_common())
    for i in s:
        answer.append(i[0])
    # print(s)
            
    return answer