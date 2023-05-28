#include <iostream>
#include <cmath>
using namespace std;
int N, r, c, ans;
int solve(int n, int cnt ,int x, int y)
{
    if(n == 1) {
        return cnt;
    }
    pair<int, int> entry[4] = {{x, y}, {x, y + n / 2}, {x + n / 2, y}, {x + n / 2, y + n / 2}};
    for (int p = 0; p < 4; p++)
    {
        int nx = entry[p].first;
        int ny = entry[p].second;
        if(nx <= r && r < nx + n/2 && ny <= c && c < ny + n/2){
            if(n == 2){
                for(int i =nx; i < nx + n/2; i++){
                    for(int j = ny; j < ny + n/2; j++){
                        cnt++;
                        if(i == r && j == c){
                                ans = cnt;
                                return cnt;
                            }
                    }
                }
            }
            return solve(n/2, cnt, nx, ny);
        }
        else{
            cnt += n/2 * n/2;
        }
    }
    return cnt;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    // cout << pow(2, 15);
    cin >> N >> r >> c;
    ans = 0;
   int result = solve(pow(2,N),0 ,0, 0);
   cout << result-1 << "\n";
}
