import sys
input = sys.stdin.readline
n, k = map(int, input().split())
children = list(map(int, input().split()))
diff = []
for i in range(n-1):
    diff.append(children[i+1]- children[i])
diff.sort()
ans = 0
for i in range((n-k)):
    ans += diff[i]
print(ans)