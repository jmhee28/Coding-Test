#include <iostream>
#include <algorithm>
#include <vector>
#include <cstring>
using namespace std;
int N;
int trees[500][500];
int dp[500][500];
int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, 1, -1};

int dfs(int x, int y)
{
    if (dp[x][y] != -1)
        return dp[x][y];
    dp[x][y] = 0;
    bool flag = false;
    int m = 0;
    for (int i = 0; i < 4; i++)
    {
        int nx = x + dx[i];
        int ny = y + dy[i];
        if (0 <= nx && nx < N && 0 <= ny && ny < N)
        {
            if (trees[x][y] < trees[nx][ny])
            {
                flag = true;
                m = max(m, dfs(nx, ny));
            }
        }
    }
    if (flag)
        dp[x][y] = 1 + m;
    return dp[x][y];
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> N;
    // vector<pair<int, pair<int, int> > > start;

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            int m;
            cin >> m;
            trees[i][j] = m;
        }
    }

    int ans = 0;
    memset(dp, -1, sizeof(dp));
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            int cnt = dfs(i, j);
            ans = max(ans, cnt);
        }
    }
    cout << ans + 1;
}