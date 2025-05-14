#include<bits/stdc++.h>
#define INF 1e9

using namespace std;
vector<pair<int, int>> graph[1002];
vector<int> trace(1002, 0);
long d[1002];
void djkstra(int start){
    priority_queue<pair<int, int>> pq;
    pq.push({0, start});
    d[start] = 0;
    while(!pq.empty()){
        int dist = -pq.top().first;
        int now = pq.top().second;
        pq.pop();

        if(d[now] < dist) continue;
        for(int i = 0; i < graph[now].size(); i++){
            int cost = dist + graph[now][i].second;
            if (cost < d[graph[now][i].first]){
                trace[graph[now][i].first] = now;
                d[graph[now][i].first] = cost;
                pq.push({-cost, graph[now][i].first});
            }
        }
    }
}
int main(){
    // get input from text file
    // freopen("input.txt", "r", stdin);
    // ios::sync_with_stdio(0);
    // cin.tie(0);
    // cout.tie(0);
    int n, m;
    cin >> n;
    cin >> m;
    for(int i = 0; i < m; i++){
        int a, b, c;
        cin >> a >> b >> c;
        graph[a].push_back({b, c});
    }
    int start, end;
    cin >> start >> end;

    fill(d, d+1002, INF);
    djkstra(start);
    int cnt = 0;
    vector<int> realTrace;
    cout << d[end] << "\n";
    int cur = end;
    while(cur != start){
        cnt++;
        realTrace.push_back(cur);
        cur = trace[cur];
    }
    realTrace.push_back(start);

    cout << realTrace.size() << "\n";
    for(int i = realTrace.size() - 1; i >=0; i--){
        cout << realTrace[i] << " ";
    }

}