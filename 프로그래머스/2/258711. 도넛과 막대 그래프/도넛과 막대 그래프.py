from collections import defaultdict
MAX = 1000001
def solution(edges):
    n = len(edges)
    outDegree = [0] * MAX
    inDegree = [0] * MAX
    answer = []
    end = 0
    for edge in edges:
        a, b = edge
        end = max(a, b, end)
        outDegree[a] += 1
        inDegree[b] += 1
        
    mainEdge = 0
    stickGragh = 0
    donaught = 0
    eight = 0
    for i in range(1, end + 1):
        if inDegree[i] == 0 and outDegree[i] >= 2:
            mainEdge = i
        if inDegree[i] >= 1 and outDegree[i] == 0:
            stickGragh += 1
        if inDegree[i] >= 2 and outDegree[i] == 2:   
            eight += 1
    donaught = outDegree[mainEdge] - (stickGragh + eight)   
    answer = [mainEdge, donaught, stickGragh, eight ]
    return answer

