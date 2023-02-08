from itertools import combinations
import math
def isPrime(perm):
    psum = sum(perm)
    for i in range(2, int(math.sqrt(psum))+1):
        if psum % i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    n = len(nums)
    perm = list(combinations(nums, 3))
    
    for p in perm:
        if isPrime(list(p)):
           answer+=1
    
    # print(perm)

    return answer