#include <iostream>
#include <string>
#include <cstring>

using namespace std;
int N;
char art[100][100];
int visited[100][100];
int dx[4] = { 1, -1, 0, 0};
int dy[4] = { 0, 0, 1, -1}; 
char curChar;

struct Colors {
    int R;
    int G;
    int B;
    int RG;
};

void dfs(int x, int y){
    visited[x][y] = 1;
    for(int i = 0; i < 4; i++){
        int nx = x + dx[i];
        int ny = y + dy[i];
        if(0 <= nx && nx < N && 0 <= ny && ny < N ){
            if(visited[nx][ny] == 0 && art[nx][ny] == curChar){
                dfs(nx, ny);
            }
        }
    }
}
void rgdfs(int x, int y){
    visited[x][y] = 1;
    for(int i = 0; i < 4; i++){
        int nx = x + dx[i];
        int ny = y + dy[i];
        if(0 <= nx && nx < N && 0 <= ny && ny < N ){
            if(visited[nx][ny] == 0 && art[nx][ny] != 'B'){
                rgdfs(nx, ny);
            }
        }
    }
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> N;
    for (int i = 0; i < N; i++)
    {
        string s;
        cin >> s;
        for(int j = 0; j < N; j++){
            art[i][j] = s[j];
        }
    }
    Colors colors = {0,0,0};
    for(int i = 0; i< N; i++){
        for(int j = 0; j < N; j++){
            if(visited[i][j] == 0){
                curChar = art[i][j];
                dfs(i, j);
                switch(curChar) {
                    case 'R': 
                        colors.R += 1;
                        break;
                    case 'G': 
                        colors.G += 1;
                        break;
                    case 'B': 
                        colors.B += 1;
                        break;    
                }
            }
        }
    }
    memset(visited, 0, sizeof(visited));
    int rg = 0;
    for(int i = 0; i< N; i++){
        for(int j = 0; j < N; j++){
            if(visited[i][j] == 0){
                if(art[i][j] != 'B')
                    {
                        rgdfs(i, j);
                        rg += 1;
                    }
            }
        }
    }
    cout << colors.R + colors.G + colors.B << ' ';
    cout << rg + colors.B;
    
}