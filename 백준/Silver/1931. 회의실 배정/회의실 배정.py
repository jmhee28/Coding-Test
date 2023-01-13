#[(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]
N = int(input())
lst = []
for i in range(N):
    s,e = map(int, input().split())
    diff =e - s
    lst.append((s,e, diff))

slst = sorted(lst, key = lambda x:(x[1], x[0], diff))
cnt  = 0

pstart = slst[0][0]
pend = slst[0][1]

for i in range(1, N):
    if slst[i][0] >= pend:
        # print(slst[i][0],slst[i][1])
        cnt += 1
        pstart = slst[i][0]
        pend = slst[i][1]
print(cnt+1)

    
