#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int N, M, L;
vector <int> rest;

int binarySearch(int start, int end){
    int ans = 0;
    int mid;
    while(start <= end){
        mid = (start + end) / 2 ;
        int cnt = 0;
        for(int i = 0; i < N+1; i++){
            int dist = rest[i+1] - rest[i];
            int rcnt= dist / mid;
            if(rest[i] + (rcnt * mid) == rest[i+1]){
                rcnt -= 1;
            }
            cnt += rcnt;
        }
        if(cnt  > M){
            start = mid + 1;
        }else {
            end = mid - 1;
        }
    }
    return start;
}
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> N >> M >> L;
    rest.push_back(0);
    for(int i = 1; i <= N; i++ ){
        int r;
        cin >> r;
        rest.push_back(r);   
    }
    rest.push_back(L);
    sort(rest.begin(), rest.end());

    int ans = binarySearch(1, L-1);
    cout << ans << "\n";
    // for(int i = 0; i < N+1; i++){
    //         int dist = rest[i+1] - rest[i];
    //         int rcnt= dist / ans;
    //         for(int j = 0; j <= rcnt; j++){
    //             if(rest[i] + (ans * j) != rest[i+1]){
    //                 cout << rest[i] + ans * j << " ";
    //             }
    //         }
    //     }
}