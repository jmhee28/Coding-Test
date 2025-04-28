import sys
from collections import defaultdict
input = sys.stdin.readline
n, d, k, c = map(int, input().split()) # 접시의 수 N, 초밥의 가짓수 d, 연속해서 먹는 접시의 수 k, 쿠폰 번호 c
sushis = []
window = defaultdict(int)
window[c] += 1
left, right = 0, 0
answer = 0

for i in range(n):
    sushis.append(int(input()))

while right < k:
    window[sushis[right]] += 1
    right += 1


for i in range(n):
    answer = max(answer, len(window))
    window[sushis[right % n]] += 1
    window[sushis[left % n]] -= 1
    if window[sushis[left % n]] == 0:
        window.pop(sushis[left % n])
    right += 1
    left += 1
    
print(answer)