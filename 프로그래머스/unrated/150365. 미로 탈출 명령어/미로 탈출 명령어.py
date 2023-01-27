def solution(n, m, x, y, r, c, k):
    shortest = k - (abs(x - r) + abs(y - c))
    if shortest % 2 == 1 or shortest < 0:
        return "impossible"

    answer = ""

    # d - l - r - u 내림차순
    direction = ['d', 'l', 'r', 'u']
    move = [[1, 0], [0, -1], [0, 1], [-1, 0]]

    while k > 0:

        for i in range(4):
            dx = x + move[i][0]
            dy = y + move[i][1]
            if 0 < dx <= n and 0 < dy <= m and abs(dx - r) + abs(dy - c) < k:
                x = dx
                y = dy
                k -= 1
                answer += direction[i]
                break

    return answer