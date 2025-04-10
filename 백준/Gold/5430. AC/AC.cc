#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <deque>
#include <cctype>  // isdigit
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int t;
    cin >> t;

    while (t--) {
        string order, str;
        int n;
        cin >> order >> n >> str;

        deque<int> dq;
        string num = "";

        // 문자열 배열 파싱
        for (char c : str) {
            if (isdigit(c)) num += c;
            else if (!num.empty()) {
                dq.push_back(stoi(num));
                num = "";
            }
        }

        bool reverse = false, error = false;

        // 명령어 처리
        for (char cmd : order) {
            if (cmd == 'R') {
                reverse = !reverse;
            } else {  // cmd == 'D'
                if (dq.empty()) {
                    cout << "error\n";
                    error = true;
                    break;
                }
                if (reverse) dq.pop_back();
                else dq.pop_front();
            }
        }

        if (!error) {
            cout << "[";
            if (!dq.empty()) {
                if (reverse) {
                    for (auto it = dq.rbegin(); it != dq.rend(); ++it) {
                        cout << *it;
                        if (it + 1 != dq.rend()) cout << ",";
                    }
                } else {
                    for (auto it = dq.begin(); it != dq.end(); ++it) {
                        cout << *it;
                        if (it + 1 != dq.end()) cout << ",";
                    }
                }
            }
            cout << "]\n";
        }
    }

    return 0;
}
