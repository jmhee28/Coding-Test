#include <bits/stdc++.h>

using namespace std;
int P = 11;
vector<vector<int>> players;
int answer;

void dfs(int depth, vector<bool> selected, int score){
    if(depth >= P){
        answer = max(answer, score);
        return;
    }

    for(int i = 0; i < P; i++){
        if(players[depth][i] != 0 && !selected[i]){
            selected[i] = true;
            score += players[depth][i];
            dfs(depth+1, selected, score);
            selected[i] = false;
            score -= players[depth][i]; 
        }
    }

}

int main(){
    int T;
    cin >> T;

    for(int i = 0; i < T; i++) {
        players = vector<vector<int>>(P, vector<int>(P, 0));
        vector<bool> selected(P, false);
        answer = 0;
        for(int j = 0; j < P; j++){
            for(int k = 0; k < P; k++){
                cin >> players[j][k];
            } 
        }
        dfs(0, selected, 0);
        cout << answer << "\n";
    }
}