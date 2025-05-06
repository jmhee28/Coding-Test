#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> arr(n);
    for(int i = 0; i < n; i++) cin >> arr[i];

    vector<int> LIS(n, 1), LDS(n, 1);

    // 왼쪽에서부터 LIS 계산
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < i; j++) {
            if (arr[j] < arr[i]) LIS[i] = max(LIS[i], LIS[j] + 1);
        }
    }

    // 오른쪽에서부터 LDS 계산
    for (int i = n-1; i >= 0; i--) {
        for (int j = n-1; j > i; j--) {
            if (arr[j] < arr[i]) LDS[i] = max(LDS[i], LDS[j] + 1);
        }
    }

    int answer = 0;
    for (int i = 0; i < n; i++) {
        answer = max(answer, LIS[i] + LDS[i] - 1); // 중복된 i값 1번 빼기
    }

    cout << answer << '\n';
}
