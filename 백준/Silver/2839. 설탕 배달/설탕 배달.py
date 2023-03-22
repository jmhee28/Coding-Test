n = int(input())
thr = 0
fiv = 0
while n >= 0:
    if n % 5 != 0:
        n -= 3
        thr += 1
    elif n % 5 == 0:
        fiv = n // 5
        break
if n < 0:
    print(-1)
else:   
    print(thr + fiv)