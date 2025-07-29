import sys
input = sys.stdin.readline
from collections import defaultdict

def print2D(arr):
    print("print 2d")
    for i in range(len(arr)):
        print(arr[i])
    
r, c, k = map(int, input().split())
area = []

for i in range(3):
    area.append(list(map(int, input().split())))
  
def computate(arr, row_len, col_len):
    # R 연산
    newArea = []
    maxCol = 0 
    for row in range(row_len):
        row_dict = defaultdict(int)
        for col in arr[row]:
            row_dict[col] += 1
            
        if 0 in row_dict:
            del row_dict[0]
            
        sorted_rows = sorted(row_dict.items(), key =lambda x: [x[1], x[0]])
        newRow = []
        for it in sorted_rows:
            newRow.append(it[0])
            newRow.append(it[1])
        maxCol = max(maxCol, len(newRow))
        newArea.append(newRow)

    for row in range(row_len):
        if len(newArea[row]) < maxCol:
            for j in range(maxCol - len(newArea[row])):
                newArea[row].append(0)
    return newArea

def sol():        
    global area
    for i in range(100+1):
        row_len = len(area) 
        col_len = len(area[0])
        if row_len >= r and col_len >= c: 
            if area[r-1][c-1] == k:
                return i
        if row_len >= col_len:
            area = computate(area, row_len, col_len)
        else:
            transedArea = [list(row) for row in zip(*area)]
            temp = computate(transedArea, col_len, row_len)
            area = [list(row) for row in zip(*temp)]
    return -1

answer = sol()
print(answer)