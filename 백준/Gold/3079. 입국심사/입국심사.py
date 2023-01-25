n,m = map(int, input().split())
times = []
for i in range(n):
    data = int(input())
    times.append(data)

start = 0
end = min(times) * m
answer = 0

while (start <= end):
    mid = (start + end)//2
    total = 0 # 검사 받는 사람의 수
    for time in times:
        total += mid // time
    if total >= m:
        answer = mid
        end = mid-1
    else: 
        start = mid + 1
print(answer)