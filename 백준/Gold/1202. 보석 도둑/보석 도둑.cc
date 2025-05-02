#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <unordered_map>
#define MAX 300001

using namespace std;

int main(){
    
    int N, K;
    cin >> N >> K;
    pair<int, int> jewls[MAX];
    int bags[MAX];
    priority_queue<int> pq;

    for (int i = 0; i < N; i++){
        cin >> jewls[i].first >> jewls[i].second;
    }
    for (int j = 0; j < K; j++){
        cin >> bags[j];
    }
    sort(jewls, jewls + N);
    sort(bags, bags + K);
    int idx = 0;
    long long sum = 0;
    for(int i = 0; i < K; i++){
        while(idx < N && bags[i] >= jewls[idx].first){
            pq.push(jewls[idx].second);
            idx++;
        }
        if(!pq.empty()){
            sum += pq.top();
            pq.pop();
        }
    }
    cout << sum;
}
