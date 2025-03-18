import sys
INF = sys.maxsize

def solution(alp, cop, problems):
    answer = 0
    max_alp_req = 0
    max_cop_req = 0
    for problem in problems:
        alp_req, cop_req, alp_rwd, cop_rwd, cost = problem
        max_alp_req = max(max_alp_req, alp_req)
        max_cop_req = max(max_cop_req, cop_req)
    m = max(max_cop_req, max_alp_req) + 2
    dp = [[INF for _ in range(m)] for _ in range(m) ]
    alp = min(alp, max_alp_req)  # 둘중 하나라도 목표값을 넘어가면 안된다.
    cop = min(cop, max_cop_req)
    dp[alp][cop] = 0
    
    for i in range(alp, max_alp_req + 1):
        for j in range(cop, max_cop_req + 1):
            if i < max_alp_req:
                dp[i + 1][j] = min(dp[i][j] + 1, dp[i+1][j])
            if j < max_cop_req:
                dp[i][j + 1] = min(dp[i][j] + 1, dp[i][j+1])
            
            for problem in problems:
                alp_req, cop_req, alp_rwd, cop_rwd, cost = problem
                if i >= alp_req and j >= cop_req:
                    new_alp_rwd = min(max_alp_req, i + alp_rwd )
                    new_cop_rwd = min(max_cop_req, j + cop_rwd )
                    dp[new_alp_rwd][new_cop_rwd] = min(dp[i][j] + cost, dp[new_alp_rwd][new_cop_rwd])
    
    answer = dp[max_alp_req][max_cop_req]

    return answer
