def fact(num):
    arr = {}
    if num in arr:
        return arr[num]
    elif num == 0 or num ==1:
        arr[num] = 1
        return arr[num]
    else:
        factorial = num * fact(num-1)
        arr[num] = factorial
    return factorial

ts = int(input())
for t in range(ts):
    n,m= map(int, input().split()) # m개 중 n개 선택
    print(fact(m)//(fact(n)*fact(m-n)))