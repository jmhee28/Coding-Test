lst = list(map(int, input()))
groups = {}
groups[0] = 0
groups[1] = 0

pren = lst[0]
s = sum(lst)
if s == len(lst) or s == 0:
    print(0)
else:
    groups[pren] += 1
    for i in range(1, len(lst)):
        if pren != lst[i]:
            groups[lst[i]] += 1
            pren = lst[i]
    print(min(groups[0], groups[1]))