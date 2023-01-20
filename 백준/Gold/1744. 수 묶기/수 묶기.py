N = int(input())
positive = []
negative = []
zero = 0
for i in range(N):
    data = int(input())
    if data > 0:
        positive.append(data)
    elif data < 0:
        negative.append(data)
    else:
        zero += 1

positive.sort()
negative.sort(reverse=True)

answer = 0
while 1:
    if len(positive) >= 2:
        a = positive.pop()
        b = positive.pop()
        if a == 1 or b == 1:
            answer += a+b
        else:
            answer += a*b
    elif len(positive) == 1:
        answer += positive.pop()
    else:
        break
while 1:
    if len(negative) >= 2:
        a = negative.pop()
        b = negative.pop()
        answer += a*b
    elif len(negative) == 1:
        if zero > 0:
            break
        else:
            answer += negative.pop()
    else:
        break
print(answer)