import sys
N = int(input())
lst = list(map(int, sys.stdin.readline().split()))
M = int(input())

start = 0
end = max(lst)

result = 0
while (start <= end):
    total = 0
    mid = (start + end)//2
    for x in lst:
        if x <= mid:
            total += x
        else:
            total += mid
    if total <= M:
        result = mid
        start = mid + 1
    else:
        end = mid -1
print(result)