#include <string>
#include <vector>
#include <iostream>
#include <queue>

using namespace std;


int n, m;
int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, 1, -1};
vector<vector<char>> board;

bool canEscape(int x, int y){
    
    vector<vector<bool>>visited (n+2, vector<bool>(m+2, false));
    visited[x][y] = true;
    queue<vector<int>> q;
    q.push({x, y});

    while(!q.empty()){
        vector<int> pos = q.front();
        int x = pos[0];
        int y = pos[1];
        q.pop();
        if(x <= 0 || x >= n || y <= 0 || y >= m ){
            return true;
        }
        for(int d = 0; d < 4; d++){
            int nx = x + dx[d];
            int ny = y + dy[d];
            if( 0 <= nx && nx < n+2 && 0 <= ny && ny < m+2 && !visited[nx][ny]){
                if(board[nx][ny] == '0') {
                    q.push({nx, ny});
                    visited[nx][ny] = true;
                }
            }
        } 
    }
   
    return false;
}

void getContainer(char target, vector<vector<char>> newBoard){
    for (int i = 1; i <= n; i++){
        for(int j = 1; j <= m; j++){
            if(board[i][j] == target){
                for(int d = 0; d < 4; d++){
                    int nx = i + dx[d];
                    int ny = j + dy[d];
                    if( 0 <= nx && nx < n+2 && 0 <= ny && ny < m+2 ){
                        if(board[nx][ny] == '0'){
                            if(canEscape(nx, ny)){
                                newBoard[i][j] = '0';
                                break;
                            }
                        }
                    }
                }
            }
        }
    }
    board = newBoard;
}

void getContainer2(char target){
    for (int i = 1; i <= n; i++){
        for(int j = 1; j <= m; j++){
            if(board[i][j] == target){
                board[i][j] = '0';
            }
        }
    }
}

int solution(vector<string> storage, vector<string> requests) {
    int answer = 0;
    n = storage.size();
    m = storage[0].size();
    board = vector<vector<char>> (n+2, vector<char>(m+2, '0'));

    for (int i = 1; i <= n; i++){
        for(int j = 1; j <= m; j++){
            board[i][j] = storage[i-1][j-1];
        }
    }

    for(int i  = 0; i < requests.size(); i++){
        int len = requests[i].size();
        char target = requests[i][0];
        if(len == 1){
            vector<vector<char>> newBoard = board;
            getContainer(target, newBoard);
            
        }
        else{
            getContainer2(target);
        }

    }
    for (int i = 1; i <= n; i++){
        for(int j = 1; j <= m; j++){
            if(board[i][j] != '0'){
                answer += 1;
            }
        }
    }
    // cout << answer;
    return answer;
}

// int main(){
//     solution({"AZWQY", "CAABX", "BBDDA", "ACACA"}, {"A", "BB", "A"});
// }