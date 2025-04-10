#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int n, m;
    cin >> n >> m;

    // 최소 힙을 위한 우선순위 큐 선언
    priority_queue<long long, vector<long long>, greater<long long>> pq;

    for (int i = 0; i < n; ++i) {
        long long x;
        cin >> x;
        pq.push(x);
    }

    for (int i = 0; i < m; ++i) {
        long long one = pq.top(); pq.pop();
        long long two = pq.top(); pq.pop();
        long long sum = one + two;
        pq.push(sum);
        pq.push(sum);
    }

    // 최종 결과 계산
    long long total = 0;
    while (!pq.empty()) {
        total += pq.top();
        pq.pop();
    }

    cout << total << '\n';
    return 0;
}
