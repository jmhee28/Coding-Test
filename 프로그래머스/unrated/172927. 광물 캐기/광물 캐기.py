n = 0
ans = 1251


def getTire(gok, rock):
    if gok == 0:
        return 1
    if gok == 1:
        if rock == "diamond":
            return 5
        else:
            return 1
    if gok == 2:
        if rock == "diamond":
            return 25
        elif rock == "iron":
            return 5
        else:
            return 1


def dfs(picks, minerals, tire, visited, idx):
    global n, ans
    if sum(visited) == n or sum(picks) == 0:
        ans = min(tire, ans)
        return tire
    for i in range(3):
        if picks[i] > 0:
            curTire = 0
            for j in range(5):
                if idx + j < n:
                    curTire += getTire(i, minerals[idx + j])
                    visited[idx + j] = 1
                else:
                    break
            picks[i] -= 1
            dfs(picks, minerals, tire + curTire, visited, idx + 5)
            picks[i] += 1
            for k in range(5):
                if idx + k < n:
                    visited[idx + k] = 0
                else:
                    break


def solution(picks, minerals):
    global n, ans
    n = len(minerals)
    visited = [0 for _ in range(n)]
    dfs(picks, minerals, 0, visited, 0)
    # print(ans)
    return ans


# picks = [0, 1, 1]
# minerals = [
#     "diamond",
#     "diamond",
#     "diamond",
#     "diamond",
#     "diamond",
#     "iron",
#     "iron",
#     "iron",
#     "iron",
#     "iron",
#     "diamond",
# ]
# solution(picks, minerals)
