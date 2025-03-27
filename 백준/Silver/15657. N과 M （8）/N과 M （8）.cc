#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int N, M;
vector<int> nums;  // 입력된 숫자 저장
vector<int> seq;   // 선택한 숫자 저장 (결과)

void backtrack(int index) {
    if (seq.size() == M) {
        for (int num : seq) {
            cout << num << " ";
        }
        cout << "\n";
        return;
    }

    for (int i = index; i < N; i++) {
        seq.push_back(nums[i]);  // 숫자 선택
        backtrack(i);  // 같은 숫자를 다시 선택할 수 있음 (중복 허용)
        seq.pop_back();  // 원상 복구 (백트래킹)
    }
}

int main() {
    cin >> N >> M;
    nums.resize(N);

    for (int i = 0; i < N; i++) {
        cin >> nums[i];
    }

    sort(nums.begin(), nums.end());  // 오름차순 정렬

    backtrack(0);  // 탐색 시작

    return 0;
}
