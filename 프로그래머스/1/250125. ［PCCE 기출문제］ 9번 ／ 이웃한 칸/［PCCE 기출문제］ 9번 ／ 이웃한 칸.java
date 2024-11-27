class Solution {
    int[] dh = {1, -1, 0, 0};
    int[] dw = {0,0,1,-1};
    public int solution(String[][] board, int h, int w) {
        int answer = 0;
        int n = 0;
        String targetColor = board[h][w];
        n = board.length;
        for(int i = 0; i < 4; i++){
            int nh = h + dh[i];
            int nw = w + dw[i];
            if(nh >= 0 && nh < n && nw >= 0 && nw < n){
                if(board[nh][nw].equals(targetColor)){
                    answer += 1;
                }
            }
        }
        return answer;
    }
}