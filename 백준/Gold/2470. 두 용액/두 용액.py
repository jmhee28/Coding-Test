import sys
n = int(input())
lst = list(map(int, sys.stdin.readline().split()))
lst.sort()
tmin = 2e+9 +1
sresult = 0
eresult = 0
for i in range(n):
    start = i + 1
    end = n - 1
    while start <= end:
        mid = (start + end) // 2
        imid = lst[i] + lst[mid]
        if abs(imid) < tmin:
            sresult = i
            eresult = mid
            tmin = abs(imid)
        if imid < 0:
            start = mid + 1
        elif imid > 0:
            end = mid -1
        else:
            break

print(lst[sresult], lst[eresult])