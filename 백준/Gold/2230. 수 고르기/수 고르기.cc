#include <bits/stdc++.h>
using namespace std;

int main(){
  
    // freopen("input.txt", "r", stdin);
    // ios::sync_with_stdio(false);
    // cin.tie(nullptr);

    int n;
    long m;
    cin >> n >> m;
    vector<long>numbers (n, 0);
    for(int i = 0; i < n; i++){
        cin >> numbers[i];
    }
    sort(numbers.begin(), numbers.end());
    long answer = LONG_MAX;


    int start = 0;
    int end = 0;
    while(start < n && end < n ){
        long d = abs(numbers[start] - numbers[end]);
        if(d > m){
            answer = min(answer, d);
            start++;
        }else if(d == m){
            answer = m;
            break;
        } else { // d < m
            end++;
        }
    }
    cout << answer;
}