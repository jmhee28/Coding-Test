import sys
input = sys.stdin.readline
n = int(input())
devs = list(map(int, input().split()))
left = 0
right = n-1
answer = 0
    
# for i in range(n-1):
#     for j in range(i+1, n):
#         val = (j-i-1) * min(devs[i], devs[j])
#         answer = max(answer, val)
def getVal(l, r):
    return (r-l-1) * min(devs[l], devs[r])

while left <= right:
    answer = max(answer, getVal(left, right))
    if devs[left] < devs[right]:
        left += 1
    else:
        right -= 1
print(answer)