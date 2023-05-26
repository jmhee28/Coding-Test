#include<iostream>
#include <vector>
#include <algorithm>

using namespace std;

int N, M;
int facA, facB;
vector <pair<int, pair<int, int>>> edges;
int parent[10001];
int ans;
int findParent(int x){
    if(parent[x] != x){
        parent[x] = findParent(parent[x]);
    }
    return parent[x];
}
void unionParent(int a, int b){
    a = findParent(a);
    b = findParent(b);
    if(a < b){
        parent[b] = a;
    }else{
        parent[a] = b;
    }
}
int main(){
    ans = 1000000000;
    cin >> N >> M;
    for(int i = 1; i <= N +1; i++ ){
        parent[i] = i;
    }
    for(int i = 0; i < M; i++){
        int a, b, c;
        cin >> a >> b >> c;
        edges.push_back({c, {a, b}});
    }
    int A, B;
    cin >> A >> B;
    if(A < B) {
        facA = A;
        facB = B;
    }else{
        facA = B;
        facB = A;
    }
    sort(edges.begin(), edges.end(), greater<>());
    for(int i = 0; i < edges.size(); i++){
        int cost = edges[i].first;
        int a = edges[i].second.first;
        int b = edges[i].second.second;
        if(findParent(a) != findParent(b)){
            unionParent(a, b);
        }
         if(findParent(facB) == facA) {
            ans = min(ans, cost);
            break;
        }
    }
    cout << ans;
}