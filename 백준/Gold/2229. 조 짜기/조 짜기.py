n = int(input())

scores = list(map(int, input().split()))


s = [0] * (n + 1)

for i in range(n+1):# j ~ i
    for j in range(i-1, -1, -1):
        score = max(scores[j:i]) - min(scores[j:i])
        s[i] = max(s[i], s[j] + score)

print(s[n])