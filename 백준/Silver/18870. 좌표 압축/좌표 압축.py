N = int(input())
lst = list(map(int, input().split()))
setlst = list(set(lst))
setlst.sort()
dict = {}

for i in range(len(setlst)):
    dict[setlst[i]] = i

for i in lst:
    print(dict[i], end = ' ')

