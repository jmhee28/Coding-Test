#include <string>
#include <vector>
#include <iostream>
#include <limits.h>

using namespace std;

int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, 1, -1};

int rtargetx, rtargety, btargetx, btargety;
int answer = INT_MAX;
int n, m;
vector<vector<int>> mazes;

bool validPosition(int x, int y){
    if(x >= 0 && x < n && y >= 0 && y < m){
        return true;
    }
    return false;
}
bool samePosition(int x, int y,  int i, int j){
    if (x == i && y == j){
        return true;
    }
    return false;
}
void print2D( vector<vector<int>> arr) {
    for(int i = 0; i < arr.size(); i++){
        for(int j = 0; j < arr[i].size(); j++){
            cout << arr[i][j] << " ";
        }
        cout << "\n";
    }
}
void dfs( vector<vector<int>> rvisited,  vector<vector<int>> bvisited,  int rx, int ry, int bx, int by, int turn, bool redFlag, bool blueFlag, int sec){
    rvisited[rx][ry] = turn;   
    bvisited[bx][by] = turn;
    if(!redFlag && samePosition(rx, ry, rtargetx, rtargety)){
        redFlag = true;
    }
    if(!blueFlag && samePosition(bx, by, btargetx, btargety)){
        blueFlag = true;
    }
    if (redFlag && blueFlag){
        answer = min(answer, turn);
        // cout << "turn:: "<< turn <<'\n';
        // cout << "red: \n";
        // print2D(rvisited);
        // cout << "blue: \n";
        // print2D(bvisited);
        return;
    }
    int nrx, nry, nbx, nby;
    if(redFlag && !blueFlag){
        for(int j = 0; j < 4; j++) {
            nbx = bx + dx[j];
            nby = by + dy[j];
                if(validPosition(nbx, nby) && !bvisited[nbx][nby] && mazes[nbx][nby] != 5 && !samePosition(rx, ry, nbx, nby)){
                    dfs(rvisited, bvisited, rx, ry, nbx, nby, turn + 1, redFlag, blueFlag, sec);
                }
        }
    }else if(!redFlag && blueFlag){
        for(int i = 0; i < 4; i++){
            nrx = rx + dx[i];
            nry = ry + dy[i];
            if(validPosition(nrx, nry) && !rvisited[nrx][nry] && mazes[nrx][nry] != 5 && !samePosition(nrx, nry, bx, by)){
                dfs(rvisited, bvisited, nrx, nry, bx, by, turn + 1, redFlag, blueFlag, sec);   
            }
        }
    }
    else{
        if(sec == 0){
            for(int i = 0; i < 4; i++){
                nrx = rx + dx[i];
                nry = ry + dy[i];
                if(validPosition(nrx, nry) && !rvisited[nrx][nry] && mazes[nrx][nry] != 5 && !samePosition(nrx, nry, bx, by)){
                    for(int j = 0; j < 4; j++) {
                        nbx = bx + dx[j];
                        nby = by + dy[j];
                        if(validPosition(nbx, nby) && !bvisited[nbx][nby] && mazes[nbx][nby] != 5 && !samePosition(nrx, nry, nbx, nby)){
                            dfs(rvisited, bvisited, nrx, nry, nbx, nby, turn + 1, redFlag, blueFlag, sec);
                        }
                    }
                }
            }
        }else{
            for(int i = 0; i < 4; i++){
                nbx = bx + dx[i];
                nby = by + dy[i];
                if(validPosition(nbx, nby) && !bvisited[nbx][nby] && mazes[nbx][nby] != 5 && !samePosition(rx, ry, nbx, nby)){
                    for(int j = 0; j < 4; j++) {
                        nrx = rx + dx[j];
                        nry = ry + dy[j];
                        if(validPosition(nrx, nry) && !rvisited[nrx][nry] && mazes[nrx][nry] != 5 && !samePosition(nrx, nry, nbx, nby)){
                            dfs(rvisited, bvisited, nrx, nry, nbx, nby, turn + 1, redFlag, blueFlag, sec);
                        }
                    }
                }
            }
        }
        
    }
  
}


int solution(vector<vector<int>> maze) {
    mazes = maze;
    m = maze[0].size();
    n = maze.size();
    vector<vector<int>> bvisited(n, vector<int>(m, 0));
    vector<vector<int>> rvisited(n, vector<int>(m, 0));
    int rx, ry, bx, by;
    

    for (int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            switch (maze[i][j])
            {
            case 1:
                rx = i;
                ry = j;
                break;
            case 2:
                bx = i;
                by = j;
                break;
            case 3:
                rtargetx = i;
                rtargety = j;
                break;
            case 4:
                btargetx = i;
                btargety = j;
                break;
            default:
                break;
            }
        }
    }
    dfs(rvisited,bvisited, rx, ry, bx, by, 1, false, false, 0);
    dfs(rvisited,bvisited, rx, ry, bx, by, 1, false, false, 1);
    if (answer >= INT_MAX){
        answer = 0;
    }else{
        answer -= 1;
    }
    // cout << answer;
    return answer;
}

// int main() {
//     // solution({{1, 4}, {0, 0}, {2, 3}});
//     solution({{4, 3, 0, 0}, {5, 5, 5, 0}, {1, 0, 0, 0}, {2, 0, 0, 0}});
//     return 0;
// }