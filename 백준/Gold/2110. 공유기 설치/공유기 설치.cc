#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int n, c;
vector<int> vec;
int binarySearch(int start, int end){
    while(start <= end){
        int mid = (start + end) / 2;
        int cnt = 1;
        int cur = 0;
        for(int i=1; i< n; i++){
            if(vec[i]-vec[cur] >= mid){
                cnt += 1;
                cur = i;
            }
        }
        if(cnt < c) {
            end = mid - 1;
        }else{
            start = mid + 1; 
        }
    }
    return end;
}
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> n >> c;
    for(int i = 0; i < n; i++){
        int t;
        cin >> t;
        vec.push_back(t);
    }
    sort(vec.begin(), vec.end());
    int ans = 0;
    ans = binarySearch(0, vec[n-1]-vec[0]);
    cout << ans;
}
