import sys
input = sys.stdin.readline
t = int(input())

def solve(n, m, k, moneys):
    answer = 0
    left = 0
    right = m
    stolen = sum(moneys[left:right])

    while left < n:
        if stolen < k:
            answer += 1
        if n == m:
            break
        stolen -= moneys[left % n]
        stolen += moneys[right % n]
        left += 1
        right += 1
    return answer
            
for _ in range(t):
    N, M, K = map(int, input().split())
    moneys = list(map(int, input().split()))
    ret = solve(N, M, K, moneys)
    print(ret)