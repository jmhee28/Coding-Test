import sys
input = sys.stdin.readline
MAX_INT = sys.maxsize

# C: 늘려야하는 최소 고객 수 
# N: 홍보할 수 있는 도시의 개수 
C , N = map(int, input().split())
values = []
weights = []
for i in range(N):
    cost, customers = map(int, input().split())
    values.append(cost)
    weights.append(customers)

def knapSack(capacity, val, wt, n):
    dp = [MAX_INT] * (capacity + 101)
    dp[0] = 0
    
    for i in range(n):
        for j in range(1, capacity + 101):
            if wt[i] <= j:
                dp[j] = min(dp[j], dp[j -wt[i]] + val[i])
               
                    
    print(min(dp[capacity:]))
    # return dp[capacity]

knapSack(C, values, weights, N)