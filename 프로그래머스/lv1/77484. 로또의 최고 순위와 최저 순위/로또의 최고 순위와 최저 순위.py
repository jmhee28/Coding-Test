from collections import Counter
def solution(lottos, win_nums):
    maxrank = 0
    minrank = 0
    lottos = Counter(lottos)
    win_nums = Counter(win_nums)
    
    for lotto in lottos:
        if lotto in win_nums and lotto != 0:
            minrank += win_nums[lotto]
    maxrank = minrank + lottos[0]
    a = 7-maxrank
    b = 7-minrank
    if a >= 6 :
        a = 6
    if b >= 6:
        b = 6
    answer = [a, b]

    
    return answer