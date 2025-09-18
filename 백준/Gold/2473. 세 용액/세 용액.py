import sys
INF = sys.maxsize

n = int(input())
liquids = list(map(int, input().split()))
liquids.sort()
s = INF
answer = []
for i in range(0, n - 2):
    start = i + 1
    end = n - 1
    cur = liquids[i]
    while start < end:
        v = cur + liquids[start] + liquids[end]
        if abs(v) < s:
            answer = [cur, liquids[start],  liquids[end]]
            s = abs(v)
        if v < 0:
            start += 1
        else:
            end -= 1

for a in answer:
    print(a, end= " ")