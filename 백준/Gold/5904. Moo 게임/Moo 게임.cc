#include <bits/stdc++.h>
using namespace std;
int K, N;

vector<long long> mooSizes(30, 0);
long long mooSize = 0;
string fmoo = "moo";

long long getMooSize(int k) { 
    if(mooSizes[k] != 0) {
        return mooSizes[k];
    }
    int prev = (getMooSize(k - 1) * 2);
    mooSizes[k] =  prev + (k + 2) + 1;
    return mooSizes[k];
}

char getAnswer(int k) {
    if(k == 0){
        return fmoo[N-1];
    }
    if(N > mooSizes[k-1] && N < mooSizes[k-1] + (k + 2 + 1) + 1){
       if(N == mooSizes[k-1] + 1){
        return 'm';
       }else{
        return 'o';
       }
    }
    else if(N <= mooSizes[k-1]){
        return getAnswer(k-1);
    } else if(N >= mooSizes[k-1] + (k + 2 + 1) + 1){
        N -= mooSizes[k-1] + (k + 2 + 1);
        return getAnswer(k-1);
    }
    return '\0';
}

int main() {
    mooSizes[0] = 3;
    K = 0;
    cin >> N;

    while(true) {
        long long mooSize = getMooSize(K);
        if (mooSize >= N) {
            break;
        }
        K++;
    }
    char answer = getAnswer(K);
    cout << answer << '\n';
}