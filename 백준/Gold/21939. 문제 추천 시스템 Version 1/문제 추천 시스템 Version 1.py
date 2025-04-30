import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline
probAsc = []
probDesc = []
probIdxStatus = [0] * 110001

N = int(input())
probIdx = 1
probInfo = defaultdict()

for i in range(N):
    P, L = map(int, input().split()) # 문제번호, 난이도
    heapq.heappush(probAsc, (L, P, probIdx))  # 오름차순, recommand -1
    heapq.heappush(probDesc, (-L, -P, probIdx)) # 내림차순, recommand 1
    probInfo[P] = probIdx
    probIdxStatus[probIdx] = 0
    probIdx += 1
    
M = int(input())
answers = []


for i in range(M):
    command = input().split()
    if command[0] == 'add':
        P, L = int(command[1]), int(command[2])
        heapq.heappush(probAsc, (L, P, probIdx))  # 오름차순
        heapq.heappush(probDesc, (-L, -P, probIdx))
        probInfo[P] = probIdx
        probIdxStatus[probIdx] = 0
        probIdx += 1
        
        
    elif command[0] == 'recommend':
        x = int(command[1])
        if x == 1:
            while True:
                problem = heapq.heappop(probDesc)
                l, p, idx = problem
                pnum = -p
                if probIdxStatus[idx] == 0:
                    print(pnum)
                    heapq.heappush(probDesc, problem)
                    # answers.append(pnum)
                    break
        else:
            while True:
                problem = heapq.heappop(probAsc)
                l, p, idx = problem
                pnum = p
                if probIdxStatus[idx] == 0:
                    print(pnum)
                    heapq.heappush(probAsc, problem)
                    # answers.append(pnum)
                    break
            
    elif command[0] == 'solved':
        P = int(command[1])
        curProbIdx = probInfo[P]
        probIdxStatus[curProbIdx] = 1
# print("answers: ", answers)