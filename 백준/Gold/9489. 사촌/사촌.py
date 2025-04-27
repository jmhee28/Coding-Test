import sys
from collections import defaultdict

input = sys.stdin.readline
lines = []

    
while True:
    n, k = map(int, input().split())
    if n == 0:
        break
    nodes = list(map(int, input().split()))
    parents = defaultdict(int)
    index = 0
    for i in range(1, n):
        parents[nodes[i]] = nodes[index]
        if i < n-1 and nodes[i] + 1 < nodes[i+1]:
            index += 1
    count = 0
    if parents[parents[k]]:
        for node in nodes:
            if parents[parents[k]] == parents[parents[node]] and parents[node] != parents[k]:
                count += 1
    print(count)

        
    
    
      
    
    