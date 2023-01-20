N, L = map(int, input().split())
waters = list(map(int, input().split()))
waters.sort()
ans = 1
i = -1
c =0
while i < N:
    i+=1
    for j in range(i+1, N):
        c = j
        if waters[j] - waters[i] >= L:
            ans += 1
            break
    if c == N-1:
        break
    i = c - 1

print(ans)