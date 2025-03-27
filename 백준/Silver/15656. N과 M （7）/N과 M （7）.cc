#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int N, M;
vector<int> nums;
vector<int> result;

void dfs(int depth) {
    if (depth == M) {
        for (int i = 0; i < M; ++i)
            cout << result[i] << ' ';
        cout << '\n';
        return;
    }

    for (int i = 0; i < N; ++i) {
        result[depth] = nums[i];
        dfs(depth + 1);
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> N >> M;
    nums.resize(N);
    result.resize(M);

    for (int i = 0; i < N; ++i)
        cin >> nums[i];

    sort(nums.begin(), nums.end());  // 사전 순 출력을 위한 정렬

    dfs(0);

    return 0;
}
