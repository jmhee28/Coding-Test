def solution(numbers):
    answer = 0
    nset = set(numbers)
    for i in range(10):
        if i not in nset:
            answer+= i
    return answer