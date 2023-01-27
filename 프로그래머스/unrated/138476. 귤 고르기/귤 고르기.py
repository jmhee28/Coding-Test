from collections import Counter
def solution(k, tangerine):
    answer = 0
    count = Counter(tangerine).most_common()
    # print(count)
    for i in range(len(count)):
        k -= count[i][1]
        answer += 1
        if k <= 0:
            break
        
    return answer