class Solution {
    int N;
    public void dfs(int x, int[][] computers, int[] visited){
        visited[x] = 1;
        for(int i = 0; i < N; i++){
            if(computers[x][i] == 1 && visited[i] == 0){
                dfs(i, computers, visited);
            }
        }
    }
    public int solution(int n, int[][] computers) {
        int answer = 0;
        N = n;
        int[] visited = new int[n];
        for(int i = 0; i < n; i++){
            if(visited[i] == 0){
                dfs(i, computers, visited);
                answer+= 1;
            }
        }
        return answer;
    }
}