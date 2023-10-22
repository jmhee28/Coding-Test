import sys
import heapq

input = sys.stdin.readline
T = int(input())
def getAns(heap):
    result = 0
    while 1:
        if len(heap) <= 1:
            return result
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        result += (a+b)
        heapq.heappush(heap,(a+b))
        
for t in range(T):
    K = int(input())
    datas = list(map(int, input().split()))
    heapq.heapify(datas) 
    answer = getAns(datas)   
    print(answer)
