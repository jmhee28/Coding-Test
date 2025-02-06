def solution(n, times):
    answer = 0
    end = n * max(times)
    start = 1
    while start <= end:
        mid = (start + end) // 2
        count = 0
        for time in times:
            count += mid // time
        if count >= n:
            end = mid - 1
            answer = mid
        elif count < n:
            start = mid + 1
    return answer