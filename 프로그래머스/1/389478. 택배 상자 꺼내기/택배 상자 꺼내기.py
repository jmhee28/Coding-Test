# 2 ≤ n ≤ 100
# 1 ≤ w ≤ 10
# 1 ≤ num ≤ n
# h = n // w + 1
# h 최데 100
MNUM = 101
def printArr(arr):
    for a in arr:
        print(a)
        
def solution(n, w, num):
    h = n // w + 1
    answer = 0
    board = [[0] * w for _ in range(h)]
    s = 1
    i = 0
    j = 0
    flag = True # 순방향
    while s <= n:
        board[i][j] = s
        s += 1
        if flag: 
            j += 1
            if j >= w:
                i += 1
                j -= 1
                flag = False
        else:
            j -= 1
            if j < 0 :
                j = 0
                i += 1
                flag = True
    # printArr(board)   
    row = (num - 1) // w
    col = 0
    for c in range(w):
        if board[row][c] == num:
            col = c
            break
    for r in range(row, h):
        cur = board[r][col]
        if cur != 0:
            answer += 1
    
    # print(answer)
    return answer
