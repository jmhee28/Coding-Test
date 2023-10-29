import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0
sumDict = {0:1}
sumN = 0

for i in range(N):
    sumN += arr[i]
    if sumN-K in sumDict.keys():
        answer += sumDict[sumN-K]
    if sumN in sumDict.keys():
        sumDict[sumN] += 1
    else:
        sumDict[sumN] = 1
      

print(answer)
