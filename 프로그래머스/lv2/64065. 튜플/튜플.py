import re
used = [0] * 100001
def solution(s):
    answer = []
    s = re.split('[{|}]',s)
    
    # print(s)
    ans = []
    for i in s:
        if len(i) > 0 and i != ',' and i != '{' and i != '}':
            i = i.split(',')
            i = list(map(int, i))
            ans.append(i)
    ans.sort(key = len)
    for a in ans:
        for i in a:
            if used[i] == 0:
                answer.append(i)
                used[i] = 1

            
    return answer