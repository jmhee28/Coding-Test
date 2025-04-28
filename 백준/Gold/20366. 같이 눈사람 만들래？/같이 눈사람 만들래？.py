import sys
INF = sys.maxsize

input = sys.stdin.readline
n = int(input())
snows = list(map(int, input().split()))
snows.sort()

def solve():
    answer = INF
    for i in range(n-3):
        for j in range(n-1, i + 2 , -1):
            snowman1 = snows[i] + snows[j]
            left = i+1
            right = j-1
            while left < right:
                snowman2 = snows[left] + snows[right]
                if snowman2 < snowman1:
                    left += 1
                elif snowman2 > snowman1:
                    right -= 1
                else:
                    return 0
                answer = min(answer, abs(snowman1 - snowman2))
    return answer
answer = solve()
print(answer)