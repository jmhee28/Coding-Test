import heapq, sys

n, m  = map(int, input().split())

lst = list(map(int, sys.stdin.readline().split()))
heapq.heapify(lst)

for i in range(m):
    one  = heapq.heappop(lst)
    two = heapq.heappop(lst)
    s = one + two
    heapq.heappush(lst, s )
    heapq.heappush(lst, s )

print(sum(lst))