#include<bits/stdc++.h>
using namespace std;

struct Trie {
    bool finish = false;
    Trie* next[10] = {};

    // 전화번호(0~9) 전용이므로 next 크기를 10으로 줄였습니다.
    // 생성자·소멸자는 기본값(=nullptr)과 delete 루프만 남기면 됩니다.
    Trie() : finish(false) {
        memset(next, 0, sizeof(next));
    }
    ~Trie() {
        for (int i = 0; i < 10; i++)
            delete next[i];
    }

    // insert 하며 prefix 충돌 체크
    // returns false if conflict detected
    bool insert_and_check(const string &s) {
        Trie* cur = this;
        for (int i = 0; i < s.size(); i++) {
            int d = s[i] - '0';
            // ① 이전 번호가 내 접두사인 경우
            if (cur->finish) return false;

            if (!cur->next[d])
                cur->next[d] = new Trie();
            cur = cur->next[d];
        }
        // ② 내가 이전에 삽입된 번호의 접두사인 경우
        if (cur->finish) return false;      // 완전히 같은 번호가 이미 있음
        for (int i = 0; i < 10; i++)
            if (cur->next[i]) return false; // 현재 노드에 자식이 있으면 내가 접두사

        cur->finish = true;
        return true;
    }
};

// main()
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t; cin >> t;
    while (t--) {
        int n; cin >> n;
        vector<string> books(n);
        for (int i = 0; i < n; i++)
            cin >> books[i];

        Trie* root = new Trie();
        bool ok = true;
        for (auto &num : books) {
            if (!root->insert_and_check(num)) {
                ok = false;
                break;
            }
        }
        cout << (ok ? "YES\n" : "NO\n");

        delete root;
    }
    return 0;
}
