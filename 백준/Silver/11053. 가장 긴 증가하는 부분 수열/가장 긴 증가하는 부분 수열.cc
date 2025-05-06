#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];

    vector<int> lis;
    for (int i = 0; i < n; i++) {
        if (lis.empty() || arr[i] > lis.back()) {
            lis.push_back(arr[i]);
        } else {
            auto it = lower_bound(lis.begin(), lis.end(), arr[i]);
            *it = arr[i];
        }
    }

    cout << lis.size() << '\n';
    return 0;
}
