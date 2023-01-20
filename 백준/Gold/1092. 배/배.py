

import sys

N = int(sys.stdin.readline())
crains = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
boxes= list(map(int, sys.stdin.readline().split()))
crains.sort(reverse = True)
boxes.sort(reverse = True)

ans =0
if boxes[0] > crains[0]:
    print(-1)
    sys.exit()

while len(boxes) > 0:
    ans += 1
    for crain in crains:
        for j in range(len(boxes)):
            if boxes[j] <= crain:
                del boxes[j]
                break


print(ans)