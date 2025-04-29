import sys
input = sys.stdin.readline
n = int(input())
village = []
population = 0
for i in range(n):
    x, a = map(int, input().split())
    village.append((x, a))
    population += a

halfPop = (population + 1)// 2 
village.sort()
pos = 0
curPop = 0
for x, a in village:
    curPop += a
    if curPop >= halfPop:
        pos = x
        break
print(pos)