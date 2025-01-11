def solution(mats, park):
    n = len(park)
    m = len(park[0])
    dp = [[0] * m for _ in range(n)]
    
    max_len = 0  # 최대 정사각형 변의 길이

    # DP 테이블 채우기
    for i in range(n):
        for j in range(m):
            if park[i][j] == "-1":
                if i == 0 or j == 0:  # 테두리 처리
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                max_len = max(max_len, dp[i][j])
    
    # 정렬된 매트 크기에서 최대 정사각형 길이에 맞는 값 찾기
    mats.sort(reverse=True)
    for mat in mats:
        if mat <= max_len:
            return mat
    
    return -1
