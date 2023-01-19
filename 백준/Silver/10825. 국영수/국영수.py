N = int(input())
lst = []
for i in range(N):
    lst.append(list(input().split()))
lst.sort(key = lambda x:(-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in lst:
    print(i[0])